from ..sort import Sort

class InsertionSort(Sort):
    def __init__(self):
        super().__init__()


    def _sort(self, elements):
        for i in range(1, len(elements)): 
  
            key = elements[i] 
    
            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >=0 and key < elements[j] : 
                    elements[j+1] = elements[j] 
                    j -= 1

                    self.number_comparations += 1
                    self.number_writes += 1
            elements[j+1] = key

            self.number_writes += 2

        return elements