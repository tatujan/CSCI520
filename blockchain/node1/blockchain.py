import os, json, hashlib, time, sys, pika, threading

from block import Block
from pow import proof_of_work

CHAIN = 'chain.txt'

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

            # with open(self.chain_file, 'r') as file:
            #     prev_block = file.readlines()[-1] # we are disregarding the '\n'
            #     prev_block = json.loads(prev_block)
            #     file.close()

            self._update_chain(genesis_block)
            return

    def _update_chain(self, block_dict):
        with open(self.chain_file, 'a') as file:
            # print("here")
            # print(block_dict)
            # print("here2")
            # print(json.dumps(block_dict))
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

        if not _chain:
            _chain = self.chain_file

        with open(_chain, 'r') as file:
            for line in file:
                block_to_validate = json.loads(line)
                print('here4')
                print(block_to_validate)
                print(type(block_to_validate))
                nonce = block_to_validate['nonce']
                index = block_to_validate['index']
                num_zeros = block_to_validate['num_zeros']
                prev_hash = block_to_validate['prev_hash']

                if index == 0:
                    num_gen_block += 1
                else:
                    if not v_hash == prev_hash:
                        raise ValueError('Broken Chain! Hash Mismatch!')
                v_hash = block_to_validate['hash']
                v_hash_to_validate = self._return_hash(prev_hash, nonce)
                self._validate_hash(v_hash_to_validate, num_zeros)

        if num_gen_block > 1:
            raise ValueError('More than one genesis_block')


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
        #prev_block = prev_block[1:-1]
        print('here3')
        print(prev_block)
        # import ast
        # prev_block = ast.literal_eval(prev_block)
        print(type(prev_block))
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
            num_zeros = num_leading_z)
        #self._update_chain(self.block.fetch_block_data())
        self._send_block(self.block.fetch_block_data())
        self.data = []
        return

    def add_data_to_block(self, new_transaction):
        self.data.append(str(new_transaction))

    def _send_block(self, block_data):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs',
                                 exchange_type='fanout')

        print(block_data)
        block = json.dumps(block_data)#str(block_data)#.encode('utf-8') # ' '.join(sys.argv[1:])
        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body=block)
        print(" [x] Block Sent!\n")
        print(block)
        connection.close()


    def _reach_consensus(self):
        # Node that has the longest chain wins
        pass

    def clear_blockchain(self):
        self._create_chain_if_not_exist()
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
            if body == 'clear':
                blockchain.clear_blockchain()
            # UPDATE CHAIN IF INDEX is INDEX + 1
            body=json.loads(body)
            blockchain._update_chain(body)
            #
            # with open('chain.txt', 'a') as file:
            #     written_block = file.readlines()[-1]
            #     written_block = written_block[1:-1]
            #     file.write(written_block)
            #     file.close()





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
        input = str(raw_input("Add transaction by simply typing it. To clear chain type clear or exit to exit.\n"))
        input = input.lower()
        if input != 'exit' and input != 'clear' and input != 'print_blockchain':
            BCoin.add_data_to_block(input)
            BCoin.create_new_block()
            BCoin._validate_chain()


        elif input != 'exit' and input != 'print_blockchain' and input == 'clear':
            BCoin._send_block(input)
            BCoin.clear_blockchain()

        elif input != 'exit' and input != 'clear' and input == 'print_blockchain':
            with open('chain.txt', 'r') as file:
                chain = file.readlines()
                file.close()
            chain = str(chain)
            print chain

        else:
            break
