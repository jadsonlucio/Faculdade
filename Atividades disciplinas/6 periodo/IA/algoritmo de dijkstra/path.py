class Path:
    def __init__(self, conections = []):
        self._cost = 0
        self.conections = conections

        if isinstance(conections, list):
            for conection in conections:
                self.__insert(conection)

    def add_conection(self, conection):
        if not self.conections:
            self.__insert(conection)
        else:
            if self.conections[-1].dest_location == conection.start_location:
                self.__insert(conection)

    
    @property
    def cost(self):
        return self._cost

    def __insert(self, conection):
        self._cost+=conection.cost
        self.conections.append(conection)

    
    def __copy__(self):
        return Path(self.conections.copy())