nums = [] #одномерный список
class ThreeStack:
    def __init__(self):
        self.nums = []
        self.border1 = 0
        self.border2 = 0

    def insert(self, num_of_stack, num):
        if (num_of_stack == 1):
            self.border1 += 1
            self.border2 += 1
            self.nums.insert(self.border1 - 1, num)
        elif (num_of_stack == 2):
            self.border2 += 1
            self.nums.insert(self.border2 - 1, num)
        elif (num_of_stack == 3):
            nums.append(num)

    def printinfo(self):
        print(self.nums)

stack = ThreeStack()
stack.insert(1, 1)
stack.insert(1, 2)
stack.insert(1, 3)
stack.insert(2, 6)
stack.insert(2, 9)
stack.insert(3, 1)
stack.insert(1, 7)
stack.printinfo()
