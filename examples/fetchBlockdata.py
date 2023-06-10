import json
from web3 import Web3 

#connection to chain
infura_url = "https://mainnet.infura.io/v3/4d01ff006dee448c8c4779788234975b"
web3 = Web3(Web3.HTTPProvider(infura_url))

# latest = web3.eth.block_number

# print(latest)

# print(web3.eth.get_block(latest))

# for i in range(0,10):
#     print(web3.eth.getBlock(latest - i))
#     print("~~~~~~~~~~~~~~~~~***************************************************************~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

hash = '0xe94442f8bbe4c2e38fb29ac5f4221cee0c8addd07bc43001f331b6efe0b00890'

print(web3.eth.getTransactionByBlock(hash,2))