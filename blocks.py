import hashlib

class Block:
    def __init__(self, prev_block_hash, transaction_list, nonce=0):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list
        self.nonce = nonce
        self.block_hash = self.generate_block_hash()

    def generate_block_hash(self):
        block_data = self.prev_block_hash + "-".join(self.transaction_list) + str(self.nonce)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        while not self.block_hash.startswith(prefix):   
            self.nonce += 1
            self.block_hash = self.generate_block_hash()    

    @staticmethod
    def create_genesis_block(transaction):
        return Block("genesis block", [transaction])

