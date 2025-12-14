# Name: 981. Time Based Key-Value Store
# URL:  https://leetcode.com/problems/time-based-key-value-store/description/


class TimeMap:
    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items:
            self.items[key] = []

        self.items[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items:
            return ""

        arr = self.items[key]
        left, right = 0, len(arr) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            t, v = arr[mid]

            if t == timestamp:
                return v
            elif t < timestamp:
                res = v
                left = mid + 1
            else:
                right = mid - 1

        return res







