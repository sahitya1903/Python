class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

class HashTableSeparateChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return


ht_oa = HashTableOpenAddressing(10)
ht_oa.insert(1, 'one')
print(ht_oa.search(1))  # Output: 'one'
ht_oa.delete(1)
print(ht_oa.search(1))  # Output: None

ht_sc = HashTableSeparateChaining(10)
ht_sc.insert(1, 'one')
print(ht_sc.search(1))  # Output: 'one'
ht_sc.delete(1)
print(ht_sc.search(1))  # Output: None