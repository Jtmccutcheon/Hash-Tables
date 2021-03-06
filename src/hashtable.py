# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.size = 0
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        if self.size is self.capacity:
            self.resize()

        index = self._hash_mod(key)
        node = self.storage[index]

        if node is None:
            # Create node, add it, return

            self.storage[index] = LinkedPair(key, value)
            self.size += 1
            return
        # 4. Collision! Iterate to the end of the linked list at provided index

        # prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value

        prev.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none

        if node is None:
            # Key not found
            return None
        else:
            # The key was found.

            self.size -= 1
            result = node.value
            # Delete this element in linked list

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted result

            return result

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)

        node = self.storage[index]

        while node is not None and node.key is not key:
            node = node.next
        # Now, node is the requested key/value pair or None

        if node is None:
            # Not found
            return
        else:
            # Found - return the data value
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        # for node in self.storage:
        #     if node is not None:
        #         new_index = self._hash_mod(node.key)
        #         new_storage[new_index] = LinkedPair(node.key, node.value)

        # self.storage = new_storage

        for i in range(self.size):
            new_storage[i] = self.storage[i]
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

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("")


# '''
# Linked List hash table key/value pair
# # '''
# class LinkedPair:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


# class HashTable:
#     '''
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     '''

#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity

#     def _hash(self, key):
#         '''
#         Hash an arbitrary key and return an integer.
#         You may replace the Python hash with DJB2 as a stretch goal.
#         '''
#         return hash(key)

#     def _hash_djb2(self, key):
#         '''
#         Hash an arbitrary key using DJB2 hash
#         OPTIONAL STRETCH: Research and implement DJB2
#         '''
#         pass

#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity

#     def insert(self, key, value):
#         '''
#         Store the value with the given key.
#         Hash collisions should be handled with Linked List Chaining.
#         Fill this in.
#         '''
#         index = self._hash_mod(key)
#         if self.storage[index] is not None:
#             print(f"WARNING:  Collision has occured at {index}")
#         else:
#             self.storage[index] = (key, value)
#         return

#     def remove(self, key):
#         '''
#         Remove the value stored with the given key.
#         Print a warning if the key is not found.
#         Fill this in.
#         '''
#         index = self._hash_mod(key)
#         if self.storage[index] is not None:
#             if self.storage[index][0] == key:
#                 self.storage[index] = None
#             else:
#                 print(f"WARNING:  Collision has occured at {index}")
#         else:
#             print(f"Warning key ({key}) not found.")
#         return

#     def retrieve(self, key):
#         '''
#         Retrieve the value stored with the given key.
#         Returns None if the key is not found.
#         Fill this in.
#         '''
#         index = self._hash_mod(key)
#         if self.storage[index] is not None:
#             if self.storage[index][0] == key:
#                 return self.storage[index][1]
#             else:
#                 print(f"WARNING:  Collision has occured at {index}")
#         else:
#             return None
#         return

#     def resize(self):
#         '''
#         Doubles the capacity of the hash table and
#         rehash all key/value pairs.
#         Fill this in.
#         '''
#         old_storage = self.storage
#         self.capacity *= 2
#         self.storage = [None] * self.capacity
#         for item in old_storage:
#             self.insert(item[0], item[1])


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)
#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))
#     print("")
