from eth_account import Account
import json
from eth_utils import address
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

def mint(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.mint().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def reveal(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.reveal().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)


def configure(web3,wallet,contract,maxrounds,buyLimit,roundTime,sellTax,buyTax,taxWallet):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.configure(maxrounds,buyLimit,roundTime,sellTax,buyTax,taxWallet).buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)
   
def whiteListAddress(web3,wallet,contract,walletAddress,allowedRound):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.whiteListAddress(walletAddress,allowedRound).buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def roundStart(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.roundStart().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def roundStop(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.roundStop().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def pauseContract(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.pauseContract().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def resumeContract(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.resumeContract().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)


def pauseSell(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.pauseSell().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def resumeSell(web3,wallet,contract):
    nonce = web3.eth.getTransactionCount(wallet.address)
    txn = contract.functions.resumeSell().buildTransaction({
        'chainId':4,'gas': 100000, 'gasPrice': web3.toWei(10,'gwei'), 'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn,private_key=wallet.privateKey )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)
    
