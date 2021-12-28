from FileTool import FileTool
ftObj=FileTool("dosya.csv",["isim","soyisim","numara"])

myfile=ftObj.openFile()

#ftObj.readAll(myfile)
ftObj.readRange(myfile,1,3)