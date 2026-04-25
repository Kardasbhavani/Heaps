#geeksforgeeks
class Solution:
    def convertMinToMaxHeap(self, n, arr):
        def heapifydown(arr,index):
            largest=index
            lchild=2*index+1
            rchild=2*index+2
            if(lchild<n and arr[lchild]>arr[largest]):
                largest=lchild
            if(rchild<n and arr[rchild]>arr[largest]):
                largest=rchild
            if(largest!=index):
                arr[largest],arr[index]=arr[index],arr[largest]
                heapifydown(arr,largest)
        for index in range(n//2-1,-1,-1):
            heapifydown(arr,index)
        return arr
