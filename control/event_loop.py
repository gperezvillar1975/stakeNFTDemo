from datetime import datetime
import asyncio
import json
from web3 import Web3


async def check_round(poll_interval,maxRounds,contract):
    lastRound = 0
    while True:
        currentRound = contract.functions.getCurrentRound().call()    
        if currentRound != lastRound:
            if currentRound != 0:
                print('Round ' + str(currentRound) + ' Started...')
            else:
                print('Launch Finished...')

            lastRound = currentRound                     

        await asyncio.sleep(poll_interval)

async def handle_event(event):    
    print(Web3.toJSON(event))    

async def log_loop(poll_interval,web3,contract):


    event_filter = [evt.createFilter(fromBlock='latest',toBlock="pending") for evt in contract.events]
    print('Listening token contract events...')
    while True:
        for evt in event_filter:
            for single_event in evt.get_new_entries():
                await handle_event(single_event)

        await asyncio.sleep(poll_interval)