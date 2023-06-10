from django.http import HttpResponse , Http404
from django.shortcuts import render
from web3 import Web3

# connected to the local private blockchain
ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))



def index(request):
    return render(request,'polls/index.html')


def vote(request):
    voterAddress = request.GET['voterAddress']
    candidateAddress = request.GET['candidateAddress']
    voterKey = request.GET['voterKey']
    nonce = web3.eth.getTransactionCount(voterAddress)
    tx = {
        'nonce':nonce,
        'to':candidateAddress,
        'value':web3.toWei(10,'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('50','gwei')
    }
    signed_tx = web3.eth.account.signTransaction(tx,voterKey)
    web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    balance = web3.fromWei(web3.eth.get_balance(candidateAddress),'ether')
    return render(request,'polls/vote.html',{"candidate":candidateAddress,"votes":(balance-100)/10})

# Create your views here.
