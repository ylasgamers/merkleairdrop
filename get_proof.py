from eth_utils import encode_hex, is_checksum_address, to_canonical_address
from airdrop import get_balance, get_item, to_items
from load_csv import load_airdrop_file
from merkle_tree import build_tree, compute_merkle_root, create_proof

def log(txt):
    f = open('listproof.txt', "a")
    f.write(txt + '\n')
    f.close()

def proof(address: bytes, airdrop_file_name: str) -> None:
    airdrop_data = load_airdrop_file(airdrop_file_name)
    try:
        # Create the proof using the Merkle tree
        proof = create_proof(
            get_item(address, airdrop_data), build_tree(to_items(airdrop_data))
        )
        
        # Convert each proof element to a hex string and store in a list
        getproof = [f"0x{encode_hex(hash_)[2:]}" for hash_ in proof]
        
        # Print and log the result
        print(f"Address : 0x{address.hex().lower()}")
        print(f"Proof : {getproof}")
        print(f"-----------------------------------------------")
        log(f"Address : 0x{address.hex().lower()}")
        log(f"Proof : {getproof}")
        log(f"-----------------------------------------------")
    except KeyError as e:
        print(f"Error: {e}")

# Load addresses from file and generate proofs for each
with open('addrlist.txt', 'r') as file:
    listaddr = file.read().splitlines()
    for addrlist in listaddr:
        addr = bytes.fromhex(addrlist[2:])  # Strip '0x' and convert to bytes
        proof(addr, 'airdrop.csv')
