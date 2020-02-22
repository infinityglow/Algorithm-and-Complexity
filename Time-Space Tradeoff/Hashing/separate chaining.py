"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of hashing
# the purpose is to split items into hash table evenly,
# and minimize collisions as fewer as possible
# table size is typically 1.5 larger than the number of items
# modulo operation is chosen as a hash function
# collision resolution mechanism: separate chaining
# average attempts for (un)successful search is calculated to evaluate efficiency of each mechanism

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(size)]
    def function(self, key):
        return key % self.size
    def put(self, key):
        value = self.function(key)
        node = Node(key)
        # table value is None
        if not self.table[value]:
            self.table[value] = node
        else:
            p = self.table[value]
            while p.next:
                p = p.next
            p.next = node
    def get(self, key):
        value = self.function(key)
        cnt = 1  # one attempt in a minimum
        p = self.table[value]
        while p:
            if p.value == key:
                return True, cnt
            p = p.next
            cnt += 1
        return False, cnt


keys = [58, 19, 75, 38, 29, 4, 60, 94, 84]
table_size = 13  # prime number is recommended
hashtable = HashTable(table_size)

# build hash table
print("Put items into hash table:\n", keys)
for key in keys:
    hashtable.put(key)

# search
print("Get items from hash table:")
search_keys = [60, 84, 22]
for key in search_keys:
    status, attempt = hashtable.get(key)
    if status:
        print("\tKey {} has been found, with {} attempt(s).".format(key, attempt))
    else:
        print("\tKey {} has not been found.".format(key))

# average case: success
counter_success = 0
for key in keys:
    _, attempt = hashtable.get(key)
    counter_success += attempt
print("Average attempts for successful search is %.2f." % (counter_success/len(keys)))

# average case: fail
counter_fail = 0
failure_keys = [26, 1, 67, 42, 82, 31, 97, 59, 21, 87, 75, 63, 116]  # failure keys for each position of hash table
for key in failure_keys:
    _, attempt = hashtable.get(key)
    counter_fail += attempt
print("Average attempts for unsuccessful search is %.2f." % (counter_fail/len(failure_keys)))
