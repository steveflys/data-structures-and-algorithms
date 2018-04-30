def hash_key(self, key):
        """Make a hash key from a string"""
        if type(key) is not str:
            raise TypeError

        first = md5(key.encode('utf-8')).hexdigest()
        num = 0
        for char in first:
            num += ord(char)

        return num % len(self.buckets)