from ..sort import Sort

class BubbleSort(Sort):
    def __init__(self):
        super().__init__()

    def _sort(self, elements):
        for i in range(0, len(elements)):
            for j in range(i + 1, len(elements)):
                if elements[i] > elements[j]:
                    aux = elements[i]
                    elements[i] = elements[j]
                    elements[j] = aux
        
                    self.number_writes += 3
                self.number_comparations += 1

        return elements