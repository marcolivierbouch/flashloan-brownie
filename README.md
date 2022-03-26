# SETUP

```
$ export WEB3_INFURA_PROJECT_ID=.....
$ export PRIVATE_KEY=....

Get some ether from faucet

$ brownie run scripts/get_weth.py --network kovan
$ brownie run scripts/deployment.py --network kovan
$ brownie run scripts/run_flash_loan.py --network kovan
```