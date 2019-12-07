class NodesPriorityQueue():

    #Start Queue
    def __init__(self):
        self.queue = []
    
    #Insert a node into the queue, from the biggest to the smaller
    def push (self, node):
        index = None
        if self.queue == []:
            self.queue.append(node)
        else:
            for i in range(len(self.queue)):
                if node.value <= self.queue[i].value:
                    index = i+1
            if index == None:
                self.queue.insert(0,node)
            else:
                self.queue.insert(index,node)
    
    #Check if the queue is empty
    def isEmpty(self):
        if self.queue == [] or self.queue == None:
            return True
        else:
            return False
    
    #Return the smallest value in the queue
    def smallest (self):
        max_value = self.queue[-1]     
        return max_value
    
    def pop (self):
        if self.queue == [] or self.queue == None:
            return None
        else:
            min_value_index = 0
            for i in range(len(self.queue)):
                if self.queue[i].value <= self.queue[min_value_index].value:
                    min_value_index = i
            del self.queue[i]



    def toString(self):
        string = ""
        for i in range(len(self.queue)):
            string += str(self.queue[i].value) + " "
        return string
            
        