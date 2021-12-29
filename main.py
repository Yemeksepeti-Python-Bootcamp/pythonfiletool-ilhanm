from FileTool import FileTool

myft=FileTool("dosya.csv",["name","price","quantity"])


#myft.addNewRow(["yeni","122","25"])
print("----")
#myft.addNewRow({"name":"webcam2","price":300,"quantity":11})
#myft.readAll()
myft.deleteRow()
myft.readRange(5,10)