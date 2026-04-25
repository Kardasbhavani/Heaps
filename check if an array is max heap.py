#geeksforgeeks
class Solution:
    def isMaxHeap(self, arr):
        # code here
        n=len(arr)
        for ind in range(0,n//2):
            lchild=2*ind+1
            rchild=2*ind+2
            if(lchild<n and arr[lchild]>arr[ind]):
                return False
            if(rchild<n and arr[rchild]>arr[ind]):
                return False
        return True
