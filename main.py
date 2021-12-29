from FileTool import FileTool

myft=FileTool("dosya.csv")


#myft.addNewRow(["listeOlarakEklendi",230,11])
print("----")
#myft.addNewRow({"name":"dictten eklendi","price":1200,"quantity":21})
#print(myft.elemlist)

myft.editRow(3)

#myft.readAll()

#print(myft.elemlist)