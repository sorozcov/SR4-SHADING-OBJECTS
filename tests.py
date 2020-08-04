# Laboratorio 3 Tests.py

#Import our gl library
import math
from gl import Render,colorScale
from mathgl import MathGl
from obj import Obj
import numpy as np

#Prubas mathgl
# math=MathGl()
# vectorA=[3,5,8]
# vectorB=[7,8,9]
# print(np.subtract(vectorA,vectorB))
# print(math.subtractVector(vectorA,vectorB))
# print(np.cross(vectorA,vectorB))
# print(math.crossVector(vectorA,vectorB))
# print(math.normalizeVector(vectorA / np.linalg.norm(vectorA)))
# print(math.normalizeVector(vectorA))
# print(np.dot(vectorA,vectorB))
# print(math.dotProductVector(vectorA,vectorB))

#We draw our models and our models zbuffer
mainGl3=Render(1400,1400)
mainGl3.loadObjModel('trex.obj',700,200,4,4)
mainGl3.glFinish('graphic1.bmp')
mainGl3.glFinishZbuffer('graphic1zbuffer.bmp')

mainGl3=Render(1400,1400)
mainGl3.loadObjModel('rock.obj',700,700,3,3)
mainGl3.glFinish('graphic2.bmp')
mainGl3.glFinishZbuffer('graphic2zbuffer.bmp')


