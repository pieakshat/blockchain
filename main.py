import argparse
from blockchain import Blockchain
from transactions import record_transaction

def main():
    blockchain = Blockchain(difficulty=4) 
    
    while True:
        print("\nOptions:")
        print("1. Add a new transaction")
        print("2. Generate a new block")
        print("3. View the blockchain")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            sender = input("Enter the sender: ").strip()
            receiver = input("Enter the receiver: ").strip()
            amount = float(input("Enter the amount: ").strip())
            transaction_hash = record_transaction(sender, receiver, amount)
            print(f"Transaction recorded with hash: {transaction_hash}")
        
        elif choice == '2':
            new_block = blockchain.generate_block()
            if new_block:
                print(f"New block generated with hash: {new_block.block_hash}")
            else:
                print("No transactions to store in a block.")
        
        elif choice == '3':
            for block in blockchain.chain:
                print(f"Block Hash: {block.block_hash}")
                print(f"Previous Block Hash: {block.prev_block_hash}")
                print(f"Transactions: {block.transaction_list}")
                print(f"Nonce: {block.nonce}\n")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
