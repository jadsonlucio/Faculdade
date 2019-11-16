from ..sort import Sort

class SelectionSort(Sort):
    def __init__(self):
        super().__init__()

    
    def selection_sort(self, A):
        for i in range(len(A)):

            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(A)): 
                if A[min_idx] > A[j]: 
                    min_idx = j
                    self.number_writes += 1
                
                self.number_comparations += 1
                    
            # Swap the found minimum element with  
            # the first element         
            A[i], A[min_idx] = A[min_idx], A[i] 

            self.number_comparations += 1
            self.number_writes += 3

    def _sort(self, elements):
        self.selection_sort(elements)

        return elements