import hashlib

transactions = {}

def record_transaction(sender, receiver, amount):
    transaction_data = f"{sender} pays {receiver} {amount} BTC"
    transaction_hash = hashlib.sha256(transaction_data.encode()).hexdigest()
    transactions[transaction_hash] = {'data': transaction_data, 'status': 0}
    return transaction_hash
