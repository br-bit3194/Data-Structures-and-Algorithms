'''
Implementing max heap from scratch using python
        x
      /   \   
    y<=x   z<=x

Insert operation: O(LogN) -> heapify_up
Get operation: O(LogN) -> heapify_down
'''

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def heapify_up(self, idx):
        while idx > 0:
            parent = (idx-1)//2
            if self.heap[parent] < self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        idx = self.size - 1
        self.heapify_up(idx)
    
    def down_heapify(self):
        if self.size==0:
            return None
        
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop()
        self.size-=1

        idx = 0
        while idx < self.size:
            left = 2*idx + 1
            right = 2*idx + 2
            smallest = idx
            if left < self.size and self.heap[left] > self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] > self.heap[smallest]:
                smallest = right
            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

    def get(self):
        if self.size == 0:
            return None
        ans = self.heap[0]
        self.down_heapify()
        return ans
    

if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(2)
    max_heap.insert(4)
    max_heap.insert(1)
    print(max_heap.get()) # 5
    print(max_heap.get()) # 4