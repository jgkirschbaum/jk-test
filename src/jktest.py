#!/usr/bin/env python3
"""
This is test program
"""

from datetime import datetime
from time import sleep
from cryptography.hazmat.primitives import hashes

def hash_with_sha3_512(data: bytes) -> str:
    """
    Hash the given data using SHA3-512
    """

    digest = hashes.Hash(hashes.SHA3_512())
    digest.update(data)
    return digest.finalize().hex()

def format_date_time(t: datetime = None) -> str:
    """
    Format date time
    """

    return t.strftime("%Y-%m-%dT%T")

def endless_loop():
    """
    Endless sleep
    """

    print("Endless sleep")
    # Sleep forever
    while True:
        fDate = format_date_time(datetime.now())
        fDateHash = hash_with_sha3_512(fDate.encode())
        print(fDate)
        print(fDateHash)
        sleep(1)

# Main
if __name__ == "__main__":
    endless_loop()
