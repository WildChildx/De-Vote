from web3 import Web3

ganache_url = "HTTP://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# check connection
# print(web3.isConnected())

address = "0xB7F40Ea953045D3A4302b743A3041bfB8F3AD5cB"

abi = [
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "helloWorld",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]

contract_instance = web3.eth.contract(address=address, abi=abi)

print(contract_instance.functions.helloWorld().call())
