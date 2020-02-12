class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * self.capacity

    def _hash(self, key):

        return hash(key)

    def _hash_mod(self, key):

        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            print(f"WARNING: Overwriting data at {index}")

        self.storage[index] = LinkedPair(key, value)

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:

            if self.storage[index].key == key:
                return self.storage[index].value

            else:
                print(f"WARNING: Key doesn't match")
                return None
        else:
            return None

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print(f"WARNING: Key not found")

        self.storage[index] = None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket_item in self.storage:
            if bucket_item is not None:
                new_index = self._hash_mod(bucket_item.key)
                new_storage[new_index] = LinkedPair(
                    bucket_item.key, bucket_item.value)

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
