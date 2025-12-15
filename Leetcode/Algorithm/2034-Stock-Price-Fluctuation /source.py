# Name: 2034. Stock Price Fluctuation
# URL:  https://leetcode.com/problems/stock-price-fluctuation/description/

import heapq

class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))


    def current(self) -> int:
        return self.timestamps[self.latest_timestamp]

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.max_heap)

        while -price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.max_heap)

        heapq.heappush(self.max_heap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_heap)

        while price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, (price, timestamp))
        return price

