class MyHashMap:
    # Easiest question of my life lowkey????
    def __init__(self):
        self.hashmap : list = []

    def put(self, key: int, value: int) -> None:
        if self.hashmap:
            for idx,num in enumerate(self.hashmap):
                if num[0] == key:
                    self.hashmap[idx][1] = value
                    return
        self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        if self.hashmap:
            for num in self.hashmap:
                if num[0] == key:
                    return num[1]
        return -1

    def remove(self, key: int) -> None:
        for idx,num in enumerate(self.hashmap):
            if num[0] == key:
                self.hashmap.pop(idx)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)