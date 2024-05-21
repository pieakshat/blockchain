import hashlib
import time 

class Block:
    def __init__(self, prev_block_hash, transaction_list, nonce=0):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list
        self.nonce = nonce
        self.block_hash = self.generate_block_hash()

    def generate_block_hash(self):
        block_data = self.prev_block_hash + "-".join(self.transaction_list)
        return hashlib.sha256(block_data.encode()).hexdigest()
    
    # def mine_block(self, difficulty):            # SHA256(block_hash + nonce) = solution[shold start with difficulty number of zeroes]
    #     question = self.block_hash + str(self.nonce)
    #     prefix = '0' * difficulty
    #     solution = hashlib.sha256(question.encode()).hexdigest()
    #     print("mininig block...")
    #     while not solution.startswith(prefix):  
    #         question = self.block_hash + str(self.nonce) 
    #         solution = hashlib.sha256(question.encode()).hexdigest()
    #         self.nonce += 1

    def mine_block(self, difficulty):             # SHA256(block_hash + nonce) = solution[shold start with difficulty number of zeroes]
        prefix = '0' * difficulty
        print("Mining block...")
        start_time = time.time()
        while True:
            question = self.block_hash + str(self.nonce)
            solution = hashlib.sha256(question.encode()).hexdigest()
            if solution.startswith(prefix):
                print(f"Block mined! Nonce: {self.nonce}, Hash_solution: {solution}")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"mined in {elapsed_time} seconds")
                return solution
                
            self.nonce += 1
    


    # def mine_block(self, difficulty):
    #     prefix = '0' * difficulty
    #     while not self.block_hash.startswith(prefix):   
    #         self.nonce += 1
    #         self.block_hash = self.generate_block_hash()    

    @staticmethod
    def create_genesis_block(transaction):
        return Block("genesis block", [transaction])

