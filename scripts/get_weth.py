from brownie import accounts, config, network, interface

def main():
    """
    Mints WETH by depositing ETH.
    """
    acct = accounts.add(
        config["wallets"]["from_key"]
    )  # add your keystore ID as an argument to this call
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth"])
    tx = weth.deposit({"from": acct, "value": 1000000000000000})
    print("Received 1 WETH")
    return tx


if __name__ == "__main__":
    main()