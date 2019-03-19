"""

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定
nums = [2, 7, 11, 15]
target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
import time
class Solution():
    def __init__(self):
        self.s=Solution
    def twoSum(self,nums,target):
        map_a=dict()
        for index ,num in enumerate(nums):
            temp=target-num
            if temp in map_a:
                print(map_a[temp],index)
            map_a[num]=index





if __name__ == '__main__':
    s=Solution()

    nums = [2, 7, 11, 15]
    # nums=[3,3]
    target = 18

    start=time.time()
    s.twoSum(nums,target)
    end=time.time()
    print("Total time ",end-start)