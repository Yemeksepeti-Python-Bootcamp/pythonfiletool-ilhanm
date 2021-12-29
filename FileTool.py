import csv
import json

class FileTool:
    elemlist=[]
    isFileHasHeaders=True #inserting,deleting depends on whether csv file has headers by default or not
    
    def __init__(self,path,fields=[]):
        self.path=path
        if fields==[]: self.setHeaders() 
        else: self.fields=fields
        self.csvToList()

    def setHeaders(self):      
        self.file=open(self.path,"r+")
        csv_reader = list(csv.reader(self.file, delimiter=','))        
        self.fields=csv_reader[0]
        
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
        for id,row in enumerate(f.readlines()):
            print(f"ID:{id} | {row}")
  
    def readRange(self,start :int,end :int):
        """
        Reads part of the given file.
        start: first row to read\n
        end: last row to read\n
        """
        f=open(self.path,"r")
        i=0
        for i,row in enumerate(f.readlines()[start:end+1]):            
            print(f"ID:{start+i} | {row}")

    def addNewRow(self, element):
        """
        Adds new row to file with dict or list type.\n
        Iterable argument, list or dict type accepted
        """
        f=open(self.path,'a', newline='\n')
        if(isinstance(element,dict)): #add new row by using dict data type
            _dictwriter=csv.DictWriter(f,self.fields)
            _dictwriter.writerow(element)
            self.elemlist.append(list(element.values())) #append values of dict type input to general list
        if(isinstance(element,list)): #add new row by using list data type
            _writer=csv.writer(f)
            _writer.writerow(element)
            self.elemlist.append(element)

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
            self.elemlist.pop()
        else:
            print(f"{rowId} id numaralı {lines[rowId]} silindi")
            lines.pop(rowId)
            self.elemlist.pop(rowId-1)
        f=open(self.path,"w+")
        f.writelines(lines)

    def editRow(self,rowId: int):
        """
        Edit data by RowId
        To change specific row, pass rowId as argument\n        
        """
        _new=[]
        for i,field in enumerate(self.fields):
            _new.append(input(f"{field} icin yeni degeri giriniz:"))
        self.elemlist.insert(rowId,_new)
        self.saveChanges()

    def saveChanges(self):
        f=open(self.path,'w', newline='\n',encoding="UTF-8")
        _writer=csv.writer(f)
        _writer.writerow(self.fields)
        _writer.writerows(self.elemlist)



        
