#geeksforgeeks
class minHeap:
    def __init__(self):
        # Initialize your data members
        self.arr=[]
        self.count=0
        
    def heapifyup(self,arr,index):
        if(index>0):
            parent=(index-1)//2
            if(arr[index]<arr[parent]):
                arr[index],arr[parent]=arr[parent],arr[index]
                self.heapifyup(arr,parent)
                
    def heapifydown(self,arr,index):
        smallest=index
        lchild=2*index+1
        rchild=2*index+2
        if(lchild<self.count and arr[lchild]<arr[smallest]):
            smallest=lchild
        if(rchild<self.count and arr[rchild]<arr[smallest]):
            smallest=rchild
        if(smallest!=index):
            arr[smallest],arr[index]=arr[index],arr[smallest]
            self.heapifydown(arr,smallest)
        
    # Insert x into the heap
    def push(self, x: int):
        # code here
        self.arr.append(x)
        self.heapifyup(self.arr,self.count)
        self.count+=1

    # Remove the top (minimum) element
    def pop(self):
        # code here
        self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        self.heapifydown(self.arr,0)

    # Return the top element or -1 if empty
    def peek(self) -> int:
        # code here
        if(self.count==0):
            return -1
        return self.arr[0]

    # Return the number of elements in the heap
    def size(self) -> int:
        # code here
        return self.count
