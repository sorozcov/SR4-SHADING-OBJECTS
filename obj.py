# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 20/07/2020
# obj.py

# Class to load a obj file
class Obj(object):
    

   #Initializer, takes as param the filename of obj that is reading
   def __init__(self,filename):
       #Initialize variables needed to store an obj file
       self.fileLines=[];
       self.vertexIndexes = []
       self.vertexTextureIndexes = []
       self.vertexNormalIndexes = []
       self.faces = []
       try:
           #Read file with its lines
           with open(filename,'r') as objFile:
               self.fileLines = objFile.read().splitlines()
               #We parse object to our obj class
               self.parseObject()

       except:
            print("El filename no ha sido encontrado para crear el obj.")
            return

   #Parse obj file properties to my class obj
   def parseObject(self):
        for line in self.fileLines:
            try:
                splitLine = line.split(None,1)
                type= splitLine[0]
                
                values=[]
                if(type[0]=='v'):

                    values=[float(val) for val in splitLine[1].split()]
                else:
                    
                    for f in splitLine[1].split():
                        if(len(f)!=0):
                            values.append([(int(val) if val!='' else 0) for val in f.split("/")])
                    
                #You can also do list(map(float, splitLine[1])) parses completely to float
                #Now we save them in our object properties
                
                #Vertex Indexes
               
                if(type=='v'):
                    
                    self.vertexIndexes.append(values)
                #Vertex Normal Indexes    
                elif(type=='vn'):
                    self.vertexNormalIndexes.append(values)
                #Vertex Texture Indexes    
                elif(type=='vt'):
                    self.vertexTextureIndexes.append(values)
                elif(type=='f'):
                     self.faces.append(values)
            except:
                #Manage error if needed but most likely is just a line with another info not needed right now
                pass


