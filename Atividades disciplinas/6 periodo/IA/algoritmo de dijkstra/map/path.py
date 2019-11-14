class Path:
    def __init__(self, conections = []):
        self._cost = 0
        self.conections = []

        if isinstance(conections, list):
            for conection in conections:
                self.__insert(conection)

    def add_conection(self, conection):
        if not self.conections:
            self.__insert(conection)
        else:
            if self.conections[-1].dest_location == conection.start_location:
                self.__insert(conection)

    
    def copy(self):
        return self.__copy__()

    @property
    def cost(self):
        return self._cost

    def __insert(self, conection):
        self._cost+=conection.cost
        self.conections.append(conection)

    def __copy__(self):
        return Path(self.conections.copy())

    def __str__(self):
        response = ""
        for conection in self.conections:
            response+=f"\n{conection.start_location.name} to {conection.dest_location.name}"
        
        response+=f"\ncost : {self.cost}"
        return response

    def __iter__(self):
        return iter(self.conections)