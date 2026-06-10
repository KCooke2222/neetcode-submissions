class StockSpanner:
    # O(n)
    # monotonic dec stack
    # maintan (price, span) pairs
    # for each value check stack if price >: pop add to span; <: span = 1 
        # then add this new val to stack


    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)