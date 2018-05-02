"""Join two hash tables on the same key."""

from .hash_table import HashTable


def left_join(left_hash, right_hash):
    """Join the right hash table to the left hash table on shared keys."""
    joined = [[null, null, null]] * len(left_hash.buckets)
    index = -1

    for bucket in left_hash.buckets:
        if bucket.head.key:
            index += 1
            joined[index[0]] = bucket.key
            joined[index[1]] = bucket.val
            if right_hash.get(key):
                joined[index[2]] = right_hash.get(key)
    return joined
