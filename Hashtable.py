# Blake Sutton  -- Student ID: 001109490 

#Implements the hash table to fulfill requirement E
class HashTable:
    # Initializes the hash table with 10 buckets
    # O(N)
    def __init__(self, capacity=10):
        self.root = []
        for i in range(capacity):
            self.root.append([])
    
    # Basic function to hash the data into the buckets
    # O(1)
    def hash_bucket(self, key):
        bucket = int(key) % len(self.root)
        return bucket

    # O(N)
    def add(self, key, item):
        # Gets the bucket ID/key from the hash
        bucket = self.hash_bucket(key)
        key_item = [key, item]
        # Appends the current value to the bucket

        if self.root[bucket] is None:
            self.root[bucket] = list([bucket])
            return True
        else:
            for pair in self.root[bucket]:
                if pair[0] == key:
                    pair[1] = bucket
                    return True
            self.root[bucket].append(key_item)
            return True
        # self.root[bucket].append(item)

    # O(N)
    def update(self, key, value):
        bucket = self.hash_bucket(key)
        if self.root[bucket] is not None:
            for pair in self.root[bucket]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # O(N)
    def get(self,key):
        bucket = self.hash_bucket(key)
        if self.root[bucket] is not None:
            for pair in self.root[bucket]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    # O(N)
    def remove(self, key):
        # Gets the bucket ID/key from the hash
        bucket = self.hash_bucket(key)
        # Gets the items currently in the bucket
        bucket_items = self.root[bucket]

        # If the key is found in the bucket, it's removed
        for item in bucket_items:
            if item.package_id == key:
                bucket_items.remove(item)
                return True
            else:
                return False