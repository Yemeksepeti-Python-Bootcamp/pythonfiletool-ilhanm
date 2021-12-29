import csv
import json

class FileTool2:
    elemlist=[]
    id=0
    idList=[]
    elemDict=[]
    hasDefaultHeaders=True #inserting,deleting depends on whether csv file has headers by default or not
    
    def __init__(self,path,fields=[]):
        self.path=path
        if fields==[]:
            self.setHeaders()
        else:
            self.fields=fields
        self.csvToDict()

    def setHeaders(self):      
        self.file=open(self.path,"r+")
        csv_reader = list(csv.reader(self.file, delimiter=','))        
        self.fields=csv_reader[0]
        
    def csvToDict(self):
        """
        Transfer csv row elements to a python iterable object.
        """
        self.file=open(self.path,"r+")
        csv_reader = list(csv.reader(self.file, delimiter=','))        
        for row in csv_reader[1:]:
            self.elemlist.append(row)
            self.idList.append(self.id)
            self.id=self.id+1
        self.elemDict=dict(zip(self.idList,self.elemlist))
    
    def getAll(self):
        """
        Reads all rows of given file.
        """
        for id, element in self.elemDict.items():
            print(f"ID: {id} | {element}")
  
    def getRange(self,start :int,end :int):
        """
        Reads part of the given file.
        start: first row to read\n
        end: last row to read\n
        """
        for id, element in list(self.elemDict.items())[start:end+1]:
            print(f"ID: {id} | {element}")

    def getByID(self,rowID):
        print(self.elemDict[rowID])

    def addRow(self, element):
        """
        Adds new row to file with dict or list type.\n
        Iterable argument, list or dict type accepted
        """        
        if(isinstance(element,dict)): #add new row by using dict data type            
            self.elemDict[self.id]=list(element.values())
            self.id+=1
        if(isinstance(element,list)): #add new row by using list data type
            self.elemDict[id]=element
            self.id+=1
        self.saveChanges()

    def deleteRow(self,rowId=-1):
        """
        Delete Row, optionally by id
        To remove specific row, pass rowId as argument\n
        If row id is not specified, last row will be deleted.
        """
        if(rowId==-1): self.elemDict.popitem()
        else: del self.elemDict[rowId]
        self.saveChanges()

    def editByID(self,rowId: int):
        """
        # Edit data by RowId
        # To change specific row, pass rowId as argument\n        
        # """
        # print(f"Değiştirmek istediğiniz değerler {self.elemDict[rowId]}")
        # for i,field in enumerate(self.fields):
        #     _new.append(input(f"{field} icin yeni degeri giriniz:"))
        # self.elemlist.insert(rowId,_new)
        # self.saveChanges()

    def saveChanges(self):
        f=open(self.path,'w', newline='\n',encoding="UTF-8")
        _writer=csv.writer(f)
        _writer.writerow(self.fields)
        _writer.writerows(list(self.elemDict.values()))



        
