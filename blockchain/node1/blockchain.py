import os, json, hashlib, time, sys, pika, threading, random
from random import randint


from block import Block
from pow import proof_of_work

## TODO: ADD BALANCE: DONE!
## TODO: verify incoming BLOCK: DONE!
## TODO: Verifiers get rewards: DONE!
## TODO: ADD CONSENSUS:

with open('BALANCE.txt') as target:
    BALANCE = target.readlines()[-1]
    print(BALANCE)
    print(type(BALANCE))
    BALANCE = json.loads(BALANCE)
    target.close()

BALANCE_s = BALANCE
CHAIN = 'chain.txt'

VERIFIER_BAL = 0

class Blockchain:
    def __init__(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        self.chain_file = os.path.join(directory, CHAIN)

        self._create_chain_if_not_exist()

        if os.stat(self.chain_file).st_size == 0:
            self._create_genesis_block()
        self._validate_chain
        self.data = []


    def _create_chain_if_not_exist(self):
        if not os.path.isfile(self.chain_file):
            file = open(self.chain_file, 'w')
            file.close()
        return

    def _create_genesis_block(self):
        if os.stat(self.chain_file).st_size == 0:
            with open('gen_block.txt', 'r') as target:
                genesis_block = target.readlines()[-1]
                genesis_block = json.loads(genesis_block)
                target.close()
            self._update_chain(genesis_block)
            return

    def _update_chain(self, block_dict):
        with open(self.chain_file, 'a') as file:
            file.write(json.dumps(block_dict) + '\n')
            file.close()
        return

    def _validate_hash(self, v_hash, num_zeros):
        if str(v_hash[:num_zeros]) != '0' * num_zeros:
            raise ValueError('Invalid Chain!')
        else:
            return True

    def _validate_chain(self, _chain = ''):
        num_gen_block = 0
        counter = 0

        if not _chain:
            _chain = self.chain_file

        with open(_chain, 'r') as file:
            for line in file:
                if not line.startswith('-'):
                    block_to_validate = json.loads(line)
                    nonce = block_to_validate['nonce']
                    index = block_to_validate['index']
                    num_zeros = block_to_validate['num_zeros']
                    prev_hash = block_to_validate['prev_hash']

                    if index == 0:
                        num_gen_block += 1
                    else:
                        if not v_hash == prev_hash:
                            #raise ValueError('Broken Chain! Hash Mismatch!')
                            if index != counter:
                                with open(_chain,'r+') as target:
                                    del_chain = target.readlines()
                                    del del_chain[index + 1 :]
                                    target.write('-'*10 + ' Broken Chain! Consensus Has Not Been Met! Switching a New Branch ' + '-'*10 + '\n')
                                    print('Broken Chain! Consensus Has Not Been Met! Creating a New Branch')
                                    for index in del_chain:
                                        index1 = json.loads(index)
                                        target.write(index)
                                    target.close()
                        else:
                            pass
                    counter += 1
                    v_hash = block_to_validate['hash']
                    v_hash_to_validate = self._return_hash(prev_hash, nonce)
                    self._validate_hash(v_hash_to_validate, num_zeros)

        # if num_gen_block > 1:
        #     raise ValueError('More than one genesis_block')


    def _return_hash(self, prev_hash, nonce):
        sha_protocol = hashlib.sha256()
        sha_protocol.update(
            str(prev_hash).encode('utf-8')+
            str(nonce).encode('utf-8'))
        return sha_protocol.hexdigest()


    def create_new_block(self):
        with open(self.chain_file, 'r') as file:
            prev_block = file.readlines()[-1] # we are disregarding the '\n'
            prev_block = json.loads(prev_block)
            file.close()
        index = prev_block['index'] + 1
        prev_hash = prev_block['hash']
        timestamp = str(time.time())
        nonce, num_leading_z = proof_of_work(prev_hash)

        self.block = Block(
            index = index,
            timestamp = timestamp,
            data = self.data,
            prev_hash = prev_hash,
            nonce= nonce,
            num_zeros = num_leading_z,
            signed = 'False')
        #self._update_chain(self.block.fetch_block_data())
        self._send_block(self.block.fetch_block_data())
        self.data = []
        return

    def add_data_to_block(self, new_transaction):
        self.data.append(str(new_transaction))

    def _send_block(self, block_data):
        # RabbitMQ!
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs',
                                 exchange_type='fanout')

        # print(block_data)
        block = json.dumps(block_data)#str(block_data)#.encode('utf-8') # ' '.join(sys.argv[1:])
        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body=block)
        print(" [x] Block Sent!\n")
        # print(block)
        connection.close()

    def balance_update(self, input):
        BALANCE_S = BALANCE
        if not BALANCE[input['from']] > input['amount'] :
            BALANCE_s[input['from']] = int(BALANCE[input['from']]) - int(input['amount'])
            BALANCE_s[input['to']] = int(BALANCE[input['to']]) + int(input['amount'])
            print('Balance update!\n')
            return True

        else:
            print('Insufficient Balance!')
            print(BALANCE)
            return False

    def balance_update_rcvd(self, body):
        input = body['data']
        input = input[0]
        input = json.dumps(input)
        print (input)
        import ast
        input = ast.literal_eval(input)
        input = ast.literal_eval(input) # for some reason I needed to do this twice.
        if BALANCE[input['from']] > input['amount']:
            BALANCE[input['from']] = int(BALANCE[input['from']]) - int(input['amount'])
            BALANCE[input['to']] = int(BALANCE[input['to']]) + int(input['amount'])
            print('Balance update!\n')
            self.print_balance(BALANCE)
            return True
        else:
            print('Insufficient Balance!')
            print(BALANCE)
            return False

    def print_balance(self,bal):
        print('Node_1: ', BALANCE['n1'])
        print('Node_2: ', BALANCE['n2'])
        print('Node_3: ', BALANCE['n3'])


    def _verify_block(self, block_to_verify, ver_bal):
        nonce = block_to_verify['nonce']
        index = block_to_verify['index']
        num_zeros = block_to_verify['num_zeros']
        prev_hash = block_to_verify['prev_hash']
        hash = block_to_verify['hash']
        hash_to_validate = self._return_hash(prev_hash, nonce)
        if self._validate_hash(hash_to_validate, num_zeros):
            self.signing_block(block_to_verify)
            print('Got Reward for Verifying!')
            ver_bal += 1
            return True
        else: return False

    def signing_block(self, body):
        body['signed'] = True
        print('Block signed with sufficient Proof of Stake')

    def _reach_consensus(self):
        # request length of chain info from all other nodes and compare
        # longest chain wins!
        pass

    def clear_blockchain(self):
        #self._create_chain_if_not_exist()
        os.remove(self.chain_file)
        self._create_chain_if_not_exist()
        self._create_genesis_block()


class ListenBlock:
    def __init__(self):
        # threading.Thread.__init__(self)
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs',
                                 exchange_type='fanout')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='logs',
                           queue=queue_name)

        print(' [*] Constantly listening for blocks. [*]')

        def callback(ch, method, properties, body):
            print(" [x] Received Block!\n %r \n" % body)
            blockchain = Blockchain()
            body=json.loads(body)
            if not body == 'New Transaction!':
                if blockchain._verify_block(body, VERIFIER_BAL):
                    blockchain.balance_update_rcvd(body)
                    with open('BALANCE.txt', 'a') as target:
                        target.write(json.dumps(BALANCE) + '\n')
                        target.close()
                    blockchain._update_chain(body)
                else:
                    raise ValueError('Cannot be verified!')

            else:
                pass

        channel.basic_consume(callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()


if __name__ == '__main__':
    BCoin = Blockchain()
    # IMPLEMENT LISTEN AS A THREAD
    listen_thread = ListenBlock()
    # listen_thread.start()
    # listen_thread.join()
    print('################################################\n')
    print('###########    Blockchain Started    ###########\n')
    print('################################################\n')

    ##### SEND CLEAR COMMAND AS WELL!!
    while True:
        BCoin._create_chain_if_not_exist()
        BCoin._create_genesis_block()
        nodes =['n1', 'n2', 'n3']
        while True:
            first_n = random.choice(nodes)
            second_n = random.choice(nodes)
            amount = random.randint(1,5)
            if not first_n == second_n:
                break
        input = {'from': first_n, 'to': second_n, 'amount': amount}
        sleep_time = random.randint(5, 15)
        time.sleep(sleep_time)
        a = random.random()
        a_str = str(a)
        print('with ' + a_str + ' probability, create a new transaction')
        if a < 0.2:
            new_t = 'New Transaction!'
            print('\n' + new_t + '\n')
            BCoin._send_block(new_t)
            print(input)
            BCoin.add_data_to_block(input)
            BCoin._validate_chain()
            BCoin.create_new_block()
        # with open('BALANCE.txt', 'a') as target:
        #     target.write(json.dumps(BALANCE) + '\n')
        #     target.close()

        # if input[0] != 'exit' and input[0] != 'print_blockchain' and input[0] == 'clear':
        #     BCoin._send_block(input)
        #     #BCoin.clear_blockchain()
        #
        # elif input[0] != 'exit' and input[0] != 'clear' and input[0] == 'print_blockchain':
        #     with open('chain.txt', 'r') as file:
        #         chain = file.readlines()
        #         file.close()
        #     chain = str(chain)
        #     print chain
        # elif input[0] == 'exit':
        #     break
        #
        # else:
        #     pass
