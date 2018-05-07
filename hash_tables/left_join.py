"""Join two hash tables on the same key."""

from .hash_table import HashTable


def left_join(left_hash, right_hash):
    """Join the right hash table to the left hash table on shared keys."""
    joined = []

    for bucket in left_hash.buckets:
        if bucket.head:
            left_keys = [None, None, None]
            left_keys[0] = bucket.head.key
            left_keys[1] = bucket.head.val
            if right_hash.get(bucket.head.key):
                left_keys[2] = right_hash.get(bucket.head.key)[0]
            else:
            joined.append(left_keys)
    return joined
