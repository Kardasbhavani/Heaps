#geeksforgeeks
class Solution:
    def heapSort(self, arr):
        #code here
        def heapifydown(arr,index,n):
            largest=index
            lchild=2*index+1
            rchild=2*index+2
            if(lchild<n and arr[lchild]>arr[largest]):
                largest=lchild
            if(rchild<n and arr[rchild]>arr[largest]):
                largest=rchild
            if(largest!=index):
                arr[largest],arr[index]=arr[index],arr[largest]
                heapifydown(arr,largest,n)
        n=len(arr) # (n) is size
        #step1:convert arr to max-heap
        for index in range(n//2-1,-1,-1): 
            heapifydown(arr,index,n)
        #step2:swap 0th index and last index and do last-- and heapify down arr[0]
        last=n-1
        while(last>0):
            arr[0],arr[last]=arr[last],arr[0]
            last-=1
            if(last>0):
                heapifydown(arr,0,last+1)
        return arr
