from ..sort import Sort

class QuickSort(Sort):
    def __init__(self):
        super().__init__()

    def partition(self, arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low , high): 
            self.number_comparations += 1
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        self.number_writes += 5

        return ( i+1 ) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low  --> Starting index, 
    # high  --> Ending index 
    
    # Function to do Quick sort 
    def quickSort(self, arr, low, high): 
        if low < high: 
            self.number_comparations += 1
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

    def _sort(self, elements):
        n = len(elements) 
        self.quickSort(elements, 0, n-1)

        return elements