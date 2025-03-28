class MathDojo:
    def __init__(self, result=0):
        self.result = result

    def add(self, num, *nums):
        self.result =num+sum(nums)
        return self

    def subtract(self, num, *nums):
        self.result=num-sum(nums)
        return self
    

