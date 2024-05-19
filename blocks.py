import hashlib

class Block:
    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list
        self.block_hash = self.generate_block_hash()

    def generate_block_hash(self):
        block_data = self.prev_block_hash + "-".join(self.transaction_list)
        return hashlib.sha256(block_data.encode()).hexdigest()

    @staticmethod
    def create_genesis_block(transaction):
        return Block("genesis block", [transaction])
