from raytracer import Raytracer
from sphere import *

r = Raytracer(400,600)

#materials
snow = Material(diffuse=color(255,255,255)) #white
eye = Material(diffuse=color(200,200,200)) #bright gray
black = Material(diffuse=color(0,0,0)) #black
mouth= Material(diffuse=(color(128,128,128))) #dark gray
nose = Material(diffuse=(color(255,166,0))) #orange
#body
r.scene.append( Sphere(V3(0, -2.0, -10), 2.2, snow) )
r.scene.append( Sphere(V3(0, 0.8,  -10), 1.7, snow) )
r.scene.append( Sphere(V3(0, 3.0, -10), 1.1, snow) )
#buttons
r.scene.append( Sphere(V3(0, 1.0, -7), 0.2, black) )
r.scene.append( Sphere(V3(0, 0, -7), 0.3, black) )
r.scene.append( Sphere(V3(0, -1.4, -7), 0.5, black) )
#eyes
r.scene.append( Sphere(V3(0.40, 3.1, -9), 0.2, eye) )
r.scene.append( Sphere(V3(-0.40, 3.1, -9), 0.2, eye) )
r.scene.append( Sphere(V3(0.37, 3.15, -8.9), 0.1, black) )
r.scene.append( Sphere(V3(-0.43, 3.15, -8.9), 0.1, black) )
#nose
r.scene.append( Sphere(V3(0, 2.7, -9), 0.25, nose) )
#mouth
r.scene.append( Sphere(V3(0.4, 2.4, -9), 0.1, mouth) )
r.scene.append( Sphere(V3(0.16, 2.2, -9), 0.1, mouth) )
r.scene.append( Sphere(V3(-0.16, 2.2, -9), 0.1, mouth) )
r.scene.append( Sphere(V3(-0.4, 2.4, -9), 0.1, mouth) )

r.render()
r.write("snowman.bmp")