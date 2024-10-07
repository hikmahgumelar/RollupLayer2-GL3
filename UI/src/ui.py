
from web3 import Web3

# Ganti dengan URL RPC lo sendiri
rpc_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Alamat smart contract lo di Sepolia
contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# ABI dari smart contract lo (copy dari file ABI Hardhat)
contract_abi = [
    {
      "inputs": [],
      "name": "getCurrentGasPriceETH",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getCurrentGasPriceWei",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]

# Buat object contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Panggil fungsi untuk mendapatkan gas price dalam wei
gas_price_wei = contract.functions.getCurrentGasPriceWei().call()
print(f"Gas Price in Wei: {gas_price_wei}")

# Panggil fungsi untuk mendapatkan gas price dalam ETH
gas_price_eth = contract.functions.getCurrentGasPriceETH().call()
print(f"Gas Price in ETH: {gas_price_eth}")

