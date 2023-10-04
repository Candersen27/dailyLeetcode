"""
Problem 706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

 - MyHashMap() initalizes the object with an empty map.

 - void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.

 - int get(int key) returns the value to which the specified key is mapped, or -1 if the map contains no mapping for the key.

 - void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.

Implementation

my init method will create a list I will use to begin my hashtable.  I could make my list have one million entries to avoid any collision handling, because the constraints on the values are at one million, but that sort of defeats the purpose of being efficient with hashing.  Instead I will make my list 101 elements long, a largeish prime number, and will use separate chaining to handle collision.


"""

class MyHashMap:

    def __init__(self) -> None:
        # This initializes a hash table as a list of 101 empty arrays
        self.hash_table = [[] for _ in range(101)]

    def put(self, key, value):
        # We want to place the key value pair into the hash table.  Using modulo will allow us to get a consistent entry 
        index = key % 101

        # Use a for loop to check to see if the key has been used already.  If so we update the new key value pair
        for i, kvp in enumerate(self.hash_table[index]):
            if key == kvp[0]: 
                self.hash_table[index][i] = ((key, value))

                return # Exit the method
        # If the key has not yet been used, we add it to the hash table.
        self.hash_table[key % 101].append((key, value))

    def get(self, key):
        # First get the result of the hashing function for the given key so we know which element of the table to access.
        index = key % 101
        
        # Check the list of key value pairs for a key match, then return the value asociated with the key
        for kvp in self.hash_table[index]:
            # Use indexing to access the key part of the key value tuple, then to return the value on a match.
            if key == kvp[0]:
                return kvp[1]
        # If there isn't a match in the table for the given key, we return negative one.
        return -1


    def remove(self, key):
        # First get the result of the hashing function for the given key so we know which element of the table to access.
        index = key % 101

        # Iterate over the list with an index using enumerate.  Look for a match on the input key and if we find one, pop the tuple entry in the list.  Then break out of the loop.
        for i, kvp in enumerate(self.hash_table[index]):
            if key == kvp[0]:
                self.hash_table[index].pop(i)

                break




Q1a = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
Q1b = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]


for command, args in zip(Q1a, Q1b):

    if command == "MyHashMap":
        newMap = MyHashMap()

    elif command == "put":
        newMap.put(args[0], args[1])

    elif command == "get":
        result = newMap.get(args[0])
        print(result)

    elif command == "remove":
        newMap.remove(args[0])



    