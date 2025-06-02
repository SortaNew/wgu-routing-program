class HashTable:
    #constructor with optional initial capcity parameter
    def __init__(self, initial_capacity=40):
        #initialize hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    # inserts and updates
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key value if it already exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # insert key value pair if it doesn't exist
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        # bucket list will hold all key value pairs stored in that index
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

