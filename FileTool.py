from io import TextIOWrapper
from os import path
class FileTool:
    def __init__(self,path,fields):
        self.path=path
        self.fields=fields
    
    def openFile(self,appendMode=False):
        """
        FileTool Method
        openFile(appendMode: bool) \n
        When appendMode=True, file opens in a+ mode, 
        appendMode=False, file opens in r+ mode.
        """
        mod=""
        if path.exists(self.path):
            mod="a+" if appendMode==True else "r+"
        else:
            mod="w+"
        return open(self.path,mod)

    def readAll(self, file :TextIOWrapper):
        """
        Takes "file" as argument:  \n
        Arg. Type: TextIOWrapper \n
        You can give returned value from openFile as an argument.
        """
        for row in file.readlines():
            print(row)
        print("\n")
        file.seek(0)
    
    def readRange(self,file :TextIOWrapper,start :int,end :int):
        """
        First Argument is an opened file :TextIOWrapper\n
        start: first row to read
        end: last row to read
        """
        for row in file.readlines()[start:end+1]:
            print(row)

        
        







        
