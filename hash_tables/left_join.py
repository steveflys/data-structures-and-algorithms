"""Join two hash tables on the same key."""

from .hash_table import HashTable


def left_join(left_hash, right_hash):
    """Join the right hash table to the left hash table on shared keys."""
    joined = []

    for bucket in left_hash.buckets:
        # print(bucket)
        if bucket.head:
            left_keys = [None, None, None]
            print('\nadding word:', bucket.head.key)
            left_keys[0] = bucket.head.key
            print('\tleft val:', bucket.head.val)
            left_keys[1] = bucket.head.val
            if right_hash.get(bucket.head.key):
                print('\tright val:', right_hash.get(bucket.head.key))
                left_keys[2] = right_hash.get(bucket.head.key)[0]
            else:
                print('\tright val: None')
            print('\n\trow:', left_keys)
            joined.append(left_keys)
    return joined
