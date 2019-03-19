"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4]
      k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

"""
import time
class Solution():
    def __init__(self):
        self.s=Solution
    def findKthLargest(self,nums,target):
        nums.insert(0,0)
        length=len(nums)-1
        first=int(length/2)
        for i in range(first):
            s.just(nums,first-i,length)

        for i in range(length-1):
            s.swap(nums,1,length-i)
            s.just(nums,1,length-1-i)
        print(nums[-target])


    def just(self,nums,start,end):

        temp=nums[start]
        i=start
        j=i*2

        while j<=end:
            if j<end and nums[j]<nums[j+1]:
                j+=1
            if temp<nums[j]:
                nums[i]=nums[j]
                i=j
                j=i*2
            else:
                break
        nums[i]=temp
        return nums

    def  swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]
        return nums





if __name__ == '__main__':
    s=Solution()

    nums = [3,2,1,5,6,4]
    target = 2

    # nums=[3, 2, 3, 1, 2, 4, 5, 5, 6]
    # target= 4
    total_time=0

    start=time.time()
    s.findKthLargest(nums,target)
    end=time.time()
    print("Total time ",end-start)