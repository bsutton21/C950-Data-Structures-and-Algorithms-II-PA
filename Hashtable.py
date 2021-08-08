# Blake Sutton  -- Student ID: 001109490 

#Implements the hash table to fulfill requirement E
class HashTable:
    # Initializes the hash table with 10 buckets
    def __init__(self, capacity=10):
        self.root = []
        for i in range(capacity):
            self.root.append([])
    
    # Basic function to hash the data into the buckets
    def hash_bucket(self, key):
        bucket = int(key) % len(self.root)
        return bucket

    def add(self, key, item):
        # Gets the bucket ID/key from the hash
        bucket = self.hash_bucket(key)
        # Appends the current value to the bucket
        self.root[bucket].append(item)

    def get(self,key):
        # Gets the bucket ID/key from the hash
        bucket = self.hash_bucket(key)
        # Gets the items currently in the bucket
        bucket_items = self.root[bucket]
        for item in bucket_items:
            if item.package_id == key:
                # Finds the index and returns the item at the index
                index = bucket_items.index(item)
                return bucket_items[index]
        else:
            return None
    
    def remove_item(self, key):
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