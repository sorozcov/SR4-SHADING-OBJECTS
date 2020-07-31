# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 30/07/2020
#  mathgl.py

#class MathGl for mathematical operations needed for gl
class MathGl(object):
    #Function to calculate a triangle barycentric coordinates of a point 
    def triangleBarycentricCoordinates(self,vertexList, pointP):
        pointA = vertexList[0]
        pointB = vertexList[1]
        pointC = vertexList[2]
        
        try:
            #Calculate u,v and w then return it
            u = ( ((pointB[1] - pointC[1])*(pointP[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointP[1] - pointC[1]) ) /
                ((pointB[1] - pointC[1])*(pointA[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointA[1] - pointC[1])) )

            v = ( ((pointC[1] - pointA[1])*(pointP[0] - pointC[0]) + (pointA[0] - pointC[0])*(pointP[1] - pointC[1]) ) /
                ((pointB[1] - pointC[1])*(pointA[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointA[1] - pointC[1])) )

            w = 1 - u - v
        except:
            return -1, -1, -1

        return u, v, w
    
    #Function to substract two vectors
    def subtractVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return
        vectorResult=[None] * len(vectorA)
        for i in range(len(vectorA)):
            vectorResult[i]=vectorA[i]-vectorB[i]
        return vectorResult
    
    #Function to do product cross two vectors
    def crossVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return
        ux,uy,uz=vectorA
        vx,vy,vz=vectorB
        wx=uy*vz-uz*vy
        wy=uz*vx-ux*vz
        wz=ux*vy-uy*vx
        return [wx,wy,wz]
    
    #Function to do product cross two vectors
    def normalizeVector(self,vectorA):
        vectorValue=self.valueVector(vectorA)
        normalized=[0]*len(vectorA)
        if(vectorValue>0):
            normalized = [coord/vectorValue for coord in vectorA]

        return normalized
    
    #Function get the value of a vector
    def valueVector(self,vectorA):
        vectorValue=0
        for i in range(len(vectorA)):
            vectorValue=vectorValue+vectorA[i]**2
        vectorValue=vectorValue**(1/2)
        return vectorValue

    #Function to do product cross two vectors
    def dotProductVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return
        vectorDotResult=0
        for i in range(len(vectorA)):
            vectorDotResult=vectorDotResult+vectorA[i]*vectorB[i]
        return vectorDotResult