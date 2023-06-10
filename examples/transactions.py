from web3 import Web3

# connected to the local private blockchain
ganache_url = "http://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

#send ether from account01 to account 02

account1 = "0x079Eec9BC0a077A8490b798A4e7Bf807C093E55c"
account2 = "0xF2e9D95d4a433F6386E1FA504e62e8360528D29E"

account1PrivateKey = "67fc5201da1c5a6cc8c30f74fc10e75bf96a0776bc6aa8e3aeb9f8b08fecdf99"

# steps to execute transcations

#nounce is transaction count by that account
nonce = web3.eth.getTransactionCount(account1)

#build a transaction
tx = {
    'nonce':nonce,
    'to':account2,
    'value':web3.toWei(1,'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei('50','gwei')
}

# sign a transactions
signed_tx = web3.eth.account.signTransaction(tx,account1PrivateKey)

# send a transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# get transaction hash
print(web3.toHex(tx_hash))