from eth_utils import encode_hex, is_checksum_address, to_canonical_address
from airdrop import get_balance, get_item, to_items
from load_csv import load_airdrop_file
from merkle_tree import build_tree, compute_merkle_root, create_proof

def root(airdrop_file_name: str) -> None:

    airdrop_data = load_airdrop_file(airdrop_file_name)
    merkle_root = compute_merkle_root(to_items(airdrop_data))

    print(f"Merkleroot : {encode_hex(merkle_root)}")
    
root("airdrop.csv")