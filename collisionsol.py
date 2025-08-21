class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert_chaining(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def insert_linear_probing(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def insert_quadratic_probing(self, key, value):
        index = self.hash_function(key)
        i = 1
        while self.table[index] is not None:
            index = (index + i ** 2) % self.size
            i += 1
        self.table[index] = (key, value)

    def hash_function2(self, key):
        return 7 - (key % 7)

    def insert_double_hashing(self, key, value):
        index = self.hash_function(key)
        step_size = self.hash_function2(key)
        while self.table[index] is not None:
            index = (index + step_size) % self.size
        self.table[index] = (key, value)

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Example usage
hash_table = HashTable(10)
hash_table.insert_chaining(10, 'A')
hash_table.insert_chaining(20, 'B')
hash_table.insert_linear_probing(10, 'C')
hash_table.insert_quadratic_probing(10, 'D')
hash_table.insert_double_hashing(10, 'E')
hash_table.display()