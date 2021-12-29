import csv
import json

class FileTool:
    elemlist=[]
    
    def __init__(self,path,fields=[]):
        self.path=path
        self.fields=fields        
        
    def csvToList(self):
        """
        Transfer csv row elements to a python iterable object.
        """
        self.file=open(self.path,"r+")
        csv_reader = list(csv.reader(self.file, delimiter=','))
        for row in csv_reader[1:]:
            self.elemlist.append(row)
    
    def readAll(self):
        """
        Reads all rows of given file.
        """
        f=open(self.path,"r")
        for row in f.readlines():
            print(row)
    

    def readRange(self,start :int,end :int):
        """
        Reads part of the given file.
        start: first row to read\n
        end: last row to read\n
        """
        f=open(self.path,"r")
        for row in f.readlines()[start:end+1]:            
            print(row)

    def addNewRow(self, element):
        """
        Adds new row to file with dict or list type.\n
        Iterable argument, list or dict type accepted
        """
        f=open(self.path,'a', newline='\n')
        if(isinstance(element,dict)): #add new row by using dict data type
            _dictwriter=csv.DictWriter(f,self.fields)
            _dictwriter.writerow(element)
        if(isinstance(element,list)): #add new row by using list data type
            _writer=csv.writer(f)
            _writer.writerow(element)

    def deleteRow(self,rowId=-1):
        """
        Delete Row, optionally by id
        To remove specific row, pass rowId as argument\n
        If row id is not specified, last row will be deleted.
        """
        f=open(self.path,"r+")
        lines=f.readlines()
        if rowId==-1:
            lines.pop() #if row id is not specified , then remove last row.
        else: 
            lines.pop(rowId)
        f=open(self.path,"w+")
        f.writelines(lines)




        
