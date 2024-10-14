from eth_utils import encode_hex, is_checksum_address, to_canonical_address
from airdrop import get_balance, get_item, to_items
from load_csv import load_airdrop_file
from merkle_tree import build_tree, compute_merkle_root, create_proof

def proof(address: bytes, airdrop_file_name: str) -> None:
    airdrop_data = load_airdrop_file(airdrop_file_name)
    hash_ = []
    try:
        proof = create_proof(
            get_item(address, airdrop_data), build_tree(to_items(airdrop_data))
        )
        getproof = ", ".join(encode_hex(hash_) for hash_ in proof)
        print(f"Address : 0x{address.hex()}")
        print(f"Proof : [{getproof}]")
        print(f"-----------------------------------------------")
    except KeyError as e:
        print(e)

with open('addrlist.txt', 'r') as file:
        listaddr = file.read().splitlines()
        for addrlist in listaddr:
            addr = bytes.fromhex(addrlist[2:])
            proof(addr, 'airdrop.csv')