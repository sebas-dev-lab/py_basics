import json

class SetFilesToJson:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__content = None

    def setContent(self, content):
        self.__content = content

    def getContent(self):
        return self.__content

    def generateJson(self):
        data = self.__content
        try:

            json_data = json.dumps(data)
            with open(f'{self.__file_name}.json', 'w') as file:
                file.write(json_data)
        except TypeError:
            print("Falla al generar josn")

    def getJsonFileContent(self):
        data = None
        try:
            with open(f'{self.__file_name}') as file:
                data = json.load(file)
            return data
        except TypeError:
            print("Falla al obtener el archivo")