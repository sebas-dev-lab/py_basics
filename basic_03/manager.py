from file_manger import FileManager
from system_process import SystemProcess

class Manager(FileManager, SystemProcess):
    def __init__(self):
        super().__init__()
        self.__command = "pip list"
        self.__filename = "./buckup"
        self.__extension = "txt"
    
    def setBuckup(self):
        list  = self.programExecute(self.__command)
        self.writeFile(self.__filename, self.__extension, list)
