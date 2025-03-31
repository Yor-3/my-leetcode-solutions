class StockSpanner:
    def __init__(self):
        self.s = []  # Stack to store (price, span)

    def next(self, price: int) -> int:
        span = 1

        # Pop all smaller/equal prices and add their span
        while self.s and price >= self.s[-1][0]:
            span += self.s.pop()[1]

        # Push current price and its span onto the stack
        self.s.append((price, span))
        return span
