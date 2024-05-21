from blocks import Block
from transactions import transactions

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [Block.create_genesis_block("Initial transaction")]
        self.difficulty = difficulty

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def generate_block(self):
        prev_block = self.get_latest_block()
        prev_block_hash = prev_block.block_hash
        t_list = [t_hash for t_hash, t_data in transactions.items() if t_data['status'] == 0]

        if not t_list:
            print("No transactions to store")
            return None

        new_block = Block(prev_block_hash, t_list)
        for t_hash in t_list:
            transactions[t_hash]['status'] = 1  # Mark transactions as processed

        self.add_block(new_block)
        return new_block


