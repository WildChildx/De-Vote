from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

address = "0xb9D01573Dd1d24daB91d75f200f6A167b52B3FF8"

abi =[
	{
		"constant": False,
		"inputs": [
			{
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "greeting",
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

#calling the greet function
print(contract_instance.functions.greet().call())

"""
update the greet value

> we need to conduct transaction
> we need account to conduct so we set default_account to account[0] of ganache blockchain
> after the transaction we get the transaction hash .
> We need to wait for the transaction to be mined . After the transaction is mined we get a reciept.
> Once the transaction is mined the greet function is updated
> Check output
> In order to keep the contract intact on the ganache hit save button at the top

"""
web3.eth.default_account = web3.eth.accounts[0]

tx_hash = contract_instance.functions.setGreeting('Hello WildChild!').transact()

web3.eth.wait_for_transaction_receipt(tx_hash)

print("Updated greeting : {}".format(contract_instance.functions.greet().call()))



