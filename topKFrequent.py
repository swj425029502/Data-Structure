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
    def __init__(self):
        self.s=Solution
    def topKFrequent(self,nums,target):
        hash_map=dict()
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        new_nums=[]
        for k,v in hash_map.items():
            new_nums.append(v)


        new_nums.insert(0,0)
        length=len(new_nums)-1
        first=int(length/2)
        for i in range(first):
            s.just(new_nums,first-i,length)

        for i in range(length-1):
            s.swap(new_nums,1,length-i)
            s.just(new_nums,1,length-1-i)

        top_k=new_nums[-target:]
        result=[]
        for i in top_k:
            for k,v in hash_map.items():
                if v==i:
                    result.append(k)
        print(result)


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

    # nums = [1,1,1,2,2,3,3,3,3,3]
    # target = 2

    nums=[1]
    target= 1
    total_time=0

    start=time.time()
    s.topKFrequent(nums,target)
    end=time.time()
    print("Total time ",end-start)