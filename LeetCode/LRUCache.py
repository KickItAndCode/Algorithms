# LRUCache
# 146. LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

from collections import OrderedDict


class LRUCache (OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        # adjust the order
        if key in self:
            self.move_to_end(key)

        # put item in cache
        self[key] = value

        # at capacity we must evict
        if len(self) > self.capacity:
            self.popitem(last=False)


# another way
# def __init__(self, capacity):
#     self.dic = collections.OrderedDict()
#     self.remain = capacity

# def get(self, key):
#     if key not in self.dic:
#         return -1
#     v = self.dic.pop(key)
#     self.dic[key] = v   # set key as the newest one
#     return v

# def set(self, key, value):
#     if key in self.dic:
#         self.dic.pop(key)
#     else:
#         if self.remain > 0:
#             self.remain -= 1
#         else:  # self.dic is full
#             self.dic.popitem(last=False)
#     self.dic[key] = value

        # Your LRUCache object will be instantiated and called as such:
        obj = LRUCache(capacity)
        param_1 = obj.get(key)
        obj.put(key, value)
