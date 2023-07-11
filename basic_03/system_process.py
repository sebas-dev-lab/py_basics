import subprocess

class SystemProcess:
    def programExecute(self, commands):
        process = subprocess.run(commands, shell=True, capture_output=True, encoding='utf-8')
        return process.stdout