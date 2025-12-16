# Name: 146. LRU Cache
# URL:  https://leetcode.com/problems/lru-cache/description/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []
        self.db = {}

    def get(self, key: int) -> int:
        if self.exists(key):
            self.items.remove(key)
            self.items.append(key)
            return self.db[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        length = len(self.items)
        if length < self.capacity:
            try:
                self.items.remove(key)
            except ValueError:
                pass
            self.items.append(key)
            self.db[key] = value
        else:
            if self.exists(key):
                self.items.remove(key)
                self.items.append(key)
                self.db[key] = value
            else:
                self.items.pop(0)
                self.items.append(key)
                self.db[key] = value

    def exists(self, key: int) -> bool:
        return key in self.items



