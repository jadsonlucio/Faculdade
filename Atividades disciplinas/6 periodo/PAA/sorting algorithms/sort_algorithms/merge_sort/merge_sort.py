from ..sort import Sort


class MergeSort(Sort):
    def __init__(self):
        super().__init__()

    # Merges two subarrays of arr[]. 
    # First subarray is arr[l..m] 
    # Second subarray is arr[m+1..r] 
    def merge(self, arr, l, m, r): 
        n1 = m - l + 1
        n2 = r- m 
    
        # create temp arrays 
        L = [0] * (n1) 
        R = [0] * (n2) 

        self.number_writes += 4
    
        # Copy data to temp arrays L[] and R[] 
        for i in range(0 , n1): 
            L[i] = arr[l + i]
            self.number_comparations += 1
            self.number_writes += 1
    
        for j in range(0 , n2): 
            R[j] = arr[m + 1 + j]
            self.number_comparations += 1
            self.number_writes += 1
    
        # Merge the temp arrays back into arr[l..r] 
        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = l     # Initial index of merged subarray 
    
        while i < n1 and j < n2 :
             
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
                self.number_writes += 2
            else: 
                arr[k] = R[j] 
                j += 1
                self.number_writes += 2
            k += 1

            self.number_comparations += 2
            self.number_writes += 1
    
        # Copy the remaining elements of L[], if there 
        # are any 
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1

            self.number_comparations += 1
            self.number_writes += 3
    
        # Copy the remaining elements of R[], if there 
        # are any 
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1

            self.number_comparations += 1
            self.number_writes += 3
    
    # l is for left index and r is right index of the 
    # sub-array of arr to be sorted 
    def mergeSort(self, arr,l,r): 
        if l < r: 
            self.number_comparations += 1
            # Same as (l+r)/2, but avoids overflow for 
            # large l and h 
            m = int((l+(r-1))/2)

            self.number_writes += 1
            # Sort first and second halves 
            self.mergeSort(arr, l, m) 
            self.mergeSort(arr, m+1, r) 
            self.merge(arr, l, m, r) 
    
    def _sort(self, elements):
        n = len(elements) 
        self.mergeSort(elements, 0, n-1)

        return elements

