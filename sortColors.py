"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
"""
import time
class Solution():
    def sortColors(self,nums):
        hash_map=dict()
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        nums.clear()
        for k,v in hash_map.items():
            for i in range(v):
                nums.append(k)


        nums.insert(0,0)
        length=len(nums)-1
        first=int(length/2)
        for i in range(first):
            self.just(nums,first-i,length)

        for i in range(length-1):
            self.swap(nums,1,length-i)
            self.just(nums,1,length-1-i)
        nums.pop(0)
        print(nums)




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

    nums = [2,0,2,1,1,0,2,1,2,1,0,2,0,1,0,2,0]

    #--->output: [0,0,1,1,2,2]



    start=time.time()
    s.sortColors(nums)
    end=time.time()
    print("Total time ",end-start)