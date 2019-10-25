class Path:
    def __init__(self, conections = None):
        self.cost = 0
        self.conections = []

        if isinstance(conections, list):
            for conection in conections:
                self.__insert(conection)

    def add_conection(self, conection):
        if not self.conections:
            self.__insert(conection)
        else:
            if self.conections[-1].dest_city == conection.start_city:
                self.__insert(conection)

    def __insert(self, conection):
        self.cost+=conection.cost
        self.conections.append(conection)

    
    def __copy__(self):
        return Path(self.conections.copy())