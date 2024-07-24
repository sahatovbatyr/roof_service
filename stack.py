

class Stack():
    def __init__(self):
        self.elemens = []
        self.min_nums = []

    # add element to end
    def push(self, number: int) -> int:
        self.elemens.append(number)
        if self.min_nums:
            self.min_nums.append(min(number, self.min_nums[-1]))
        else:
            self.min_nums.append(number)

        return len(self.elemens )-1

    # delete last element and return it
    def pop(self):
        res = self.elemens.pop()
        self.min_nums.pop()
        return res

    # get last element without delete
    def top(self):
        return self.elemens[-1]


    def get_min(self):
        return self.min_nums[-1]

    def get_elemnts(self):
        return self.elemens



stack = Stack()

stack.push(5)
stack.push(4)
stack.push(7)
stack.push(2)
stack.pop()
stack.push(1)
stack.pop()
stack.pop()
print(stack.get_elemnts())
print(stack.get_min())










