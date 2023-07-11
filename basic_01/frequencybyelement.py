from setFile import *

class FrequencyByElement(SetFilesToJson):
    def __init__(self, iterable, file_name = 'default'):
        super().__init__(file_name)
        self.__target = iterable
        self.__frequencies = {}

    def set_fqcy(self):
        it = self.__target
        try:
            for item in it:
                if item in self.__frequencies:
                    self.__frequencies[item] += 1
                else:
                    self.__frequencies[item] = 1
        except TypeError:
            print("Fallo al crear frecuencia")
        self.setContent(self.__frequencies)
    
    def getFrequencies(self):
        return self.__frequencies
    