class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def add(self, i, val):

        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def update(self, index, val):

        diff = val - self.nums[index]
        self.nums[index] = val

        self.add(index + 1, diff)

    def prefixSum(self, i):

        total = 0

        while i > 0:
            total += self.tree[i]
            i -= i & -i

        return total

    def sumRange(self, left, right):

        return (
            self.prefixSum(right + 1)
            - self.prefixSum(left)
        )
