>>> from web3 import Web3
>>> w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
>>> w3.eth.get_transaction_count('0x1234567890123456789012345678901234567890')
10
