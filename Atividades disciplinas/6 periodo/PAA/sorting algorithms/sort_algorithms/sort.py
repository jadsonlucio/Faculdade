from time import clock

def is_orded(array):
    order = array[0] > array[1]

    for i in range(len(array) - 1):
        if (array[i] > array[i+1]) != order:
            return False

    return True

class Sort:
    def __init__(self):
        self.time_to_sort = None
        self.number_comparations = 0
        self.number_writes = 0
        self.quant_elements = 0
        self.run = False
    
    def sort(self, elements, *args, **kwargs):
        self.reset()
        self.quant_elements = len(elements)

        time_ini = clock()

        elements = self._sort(elements, *args, **kwargs)

        self.time_to_sort = clock() - time_ini
        self.run = True

        if len(elements) != self.quant_elements:
            print(elements)
            raise Exception(f"error in quant elements, quant_passed : {self.quant_elements}, quant_recived : {len(elements)} ")

        if not is_orded(elements):
            raise Exception("elements not orded")

        return elements

    def _sort(self, elements, *args, **kwargs):
        raise NotImplementedError("Sort algorithm not implemented")

    @property
    def info(self):
        complement_info = self._info()
        info = {
            "time to run" : self.time_to_sort,
            "number comparations" : self.number_comparations,
            "Número de escritas" : self.number_writes, 
            "size" : self.quant_elements
        }
        
        info.update(complement_info)

        return info

    
    def _info(self):
        return {}

    def reset(self):
        self.number_comparations = 0
        self.number_writes = 0