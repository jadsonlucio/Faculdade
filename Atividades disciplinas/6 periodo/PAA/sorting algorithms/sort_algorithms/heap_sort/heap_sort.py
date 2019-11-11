from ..sort import Sort

class HeapSort(Sort):
    def __init__(self):
        super().__init__()

    def _sort(self, elements):
        n = len(elements) 

        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self.heapify(elements, n, i) 

        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            elements[i], elements[0] = elements[0], elements[i]   # swap 
            self.number_writes += 3
            self.heapify(elements, i, 0) 
        
        return elements

    def heapify(self, arr, n, i): 
        largest = i  # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
    
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]:
            self.number_comparations += 1 
            largest = l 
    
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            self.number_comparations += 1 
            largest = r 
    
        # Change root, if needed 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i]  # swap 
            self.number_writes += 3
            # Heapify the root. 
            self.heapify(arr, n, largest)