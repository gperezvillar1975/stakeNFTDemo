from eth_account import Account
import time
import getopt
import json
import sys
from eth_utils import address
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import wrapper
import time
import asyncio
from event_loop import log_loop, check_round



def event_catch(web3,contract,maxrounds):
    loop = asyncio.get_event_loop()
    print('Starting Event Loop')
    try:
        loop.run_until_complete(
                asyncio.gather(log_loop(2,web3,contract),
                check_round(2,maxrounds,contract)
            )            
        )
    finally:
        loop.close()

def main(args):

    token_address = ""
    pauseContract = False
    HoneyPot = False
    start_process = False
    h_defined = False
    p_defined = False

    taxWallet = ""

    opts, args = getopt.getopt(args,"t:p:h:s:w:",["bucket=","input_file="])
    for opt, arg in opts:
      if opt == '-t':
        start_process = True
        token_address = arg
      elif opt == "-p":
        p_defined = True          
        start_process = False
        if arg.capitalize() == "True":
            pauseContract = True
        else:
            pauseContract = False

      elif opt == "-h":
        h_defined = True
        start_process = False
        if arg.capitalize() == "True":
            HoneyPot = True
        else:
            HoneyPot = False
      elif opt == "-w":
          taxWallet = arg

    if not token_address:
        print("Must define token address contract -t <address>")
        exit(1)

    if (not taxWallet and start_process) :
        print("Must define tax wallet address -w <address>")
        exit(1)

    #TOKEN CONFIGURATION
    #BSC ENDPOINT
    blockchain_address = 'https://rinkeby.infura.io/v3/26763e533f734041b01ddfc8c90d8824'
    #LOCAL ENDPOINT
    #blockchain_address = 'http://10.10.12.40:8545'
    #BSC WALLET
    wallet_pk = '0x24979d4a19bcdc60a1d4a592c58f7b755858fcdea5a54c916fe0fa10d9c20ec7'
    #LOCAL WALLET
    #wallet_pk = '5e374e569bc09a3dd1705b6d2c0c8ef4174a1cf680c6b13fbe8c32320808acdf'
    #token_address = '0xF7f022B88d112366C05d1F91Fd90B01e8AC508D7'
    maxrounds = 2
    buyLimit = 5000000
    roundTime = 90
    sellTax = 5 
    buyTax = 5 
    # **** WHITELISTED WALLETS
    wallets = [
        ["0x7555269ea68ba6Bb5Bc8F11E48157Dda6ea741eA",1],
        ["0x8dc859B2BDCA84C069E05a4A57f7804d7418F52c",2],
        ["0xfa70A6217478Cb0cCe9144612a1A9E0C41024C23",2]
    ]

    web3 = Web3(HTTPProvider(blockchain_address))
    mainWallet = web3.eth.account.privateKeyToAccount(wallet_pk)
    print(mainWallet.address)
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.defaultAccount = mainWallet.address
    print("Owner Wallet: " + mainWallet.address)
    print("Token address: " + token_address)
    with open('../build/contracts/WNFTDemo.json') as file:
        contract_json = json.load(file)      # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=token_address, abi=contract_abi)


    #wrapper.mint(web3,mainWallet,contract)
    #wrapper.reveal(web3,mainWallet,contract)
    print(contract.functions.tokenURI(2).call())


if __name__ == "__main__":
    main(sys.argv[1:])

