# pylint: disable=missing-docstring

from datetime import datetime
from cryptography.hazmat.primitives import hashes
from src.jktest import format_date_time, hash_with_sha3_512


def test_format_date_time():
    assert format_date_time(datetime(2011, 11, 11, 11, 11, 11)) == "2011-11-11T11:11:11"

def test_hash_with_sha3_512():
    assert hash_with_sha3_512("2011-11-11T11:11:11".encode()) == \
        "6532eaedc4a63ca5f1f20dfa18f2fa8d45ec55ae16b00afbc1d5e1d995837b89aaa0835d14dea0c2436ce9cd5749060472921f46ff7700267fb7381b6872bbc0"
