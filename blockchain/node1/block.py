import hashlib

class Block:

    def __init__(self, index, timestamp, data, prev_hash, nonce, num_zeros, signed=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.num_zeros = num_zeros
        self.hash = self.hash_block()
        self.signed = signed


    def hash_block(self):
        sha_protocol = hashlib.sha256()
        sha_protocol.update(
            str(self.index).encode('utf-8')+
            str(self.timestamp).encode('utf-8')+
            str(self.data).encode('utf-8')+
            str(self.prev_hash).encode('utf-8')+
            str(self.nonce).encode('utf-8')+
            str(self.num_zeros).encode('utf-8'))
        return sha_protocol.hexdigest()

    def fetch_block_data(self):
        block_data = {'index': self.index, 'timestamp':self.timestamp,
                        'data':self.data, 'prev_hash':self.prev_hash,
                        'nonce':self.nonce, 'num_zeros':self.num_zeros,
                        'hash':self.hash, 'signed':self.signed}

        return block_data
