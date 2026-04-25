#leetcode215
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[] #T.C:-O(n logk) #S.C:-O(k)
        n=len(nums)
        for index in range(0,k):
            heapq.heappush(heap,nums[index])
        for index in range(k,n):
            if(nums[index]>heap[0]):
                heapq,heappop(heap)
                heapq.heappush(heap,nums[index])
        return heap[0]
