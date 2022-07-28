class StockSpanner:
    stack = []
    def __init__(self):
        stack = []
        return    

    def next(self, price: int) -> int:
        s=1
        while(self.stack and price>=self.stack[-1][0]):
            s+=self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price,s))
        return s 
if __name__ == '__main__':
    obj = StockSpanner()
    print(obj.next(85))
    print(obj.next(76))
    print(obj.next(43))
    print(obj.next(26))
    print(obj.next(52))
    print(obj.next(75))
    print(obj.next(85))





    