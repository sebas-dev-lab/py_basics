class FileManager:
    def writeFile(self, filename, extension, data):
        with open(f"{filename}.{extension}", "w") as file:
            file.write(data)