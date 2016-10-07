import bpy, mathutils, bmesh

def MaillageVide():
    m = bmesh.new()
    return m    

def AjouterSommet(bm, p):
    return bm.verts.new(p)
        
def AjouterArrete(bm, v1, v2):
    bm.edges.new((v1,v2))
 
def AjouterFace(bm, P):
    bm.faces.new(P)

def FinaliserBmesh(bm):
    me = bpy.data.meshes.new("Grille")
    bm.to_mesh(me)
    bm.free()
    scene = bpy.context.scene
    obj = bpy.data.objects.new("Object", me)
    scene.objects.link(obj)

def rectangle(bm,x,y,z,h,l, inclinaison, flipVertex = False):
    if (inclinaison == "FACE"):
        v1 = mathutils.Vector((x, y, z))
        v2 = mathutils.Vector((x + l, y, z))
        v3 = mathutils.Vector((x + l, y, z - h))
        v4 = mathutils.Vector((x, y, z - h))
    elif (inclinaison == "COUCHE"):
        v1 = mathutils.Vector((x, y, z))
        v2 = mathutils.Vector((x, y + h, z))
        v3 = mathutils.Vector((x + l, y + h, z))
        v4 = mathutils.Vector((x + l, y, z))
    elif (inclinaison == "COTE"):
        v1 = mathutils.Vector((x, y, z))
        v2 = mathutils.Vector((x, y + l, z))
        v3 = mathutils.Vector((x, y + l, z - h))
        v4 = mathutils.Vector((x, y, z - h))
        
    s1 = AjouterSommet(bm, v1)
    s2 = AjouterSommet(bm, v2)
    s3 = AjouterSommet(bm, v3)
    s4 = AjouterSommet(bm, v4)
    
    P = [s1, s2, s3, s4]
    
    if flipVertex : P.reverse
    
    AjouterArrete(bm, s1, s2)
    AjouterArrete(bm, s2, s3)
    AjouterArrete(bm, s3, s4)
    AjouterArrete(bm, s4, s1)
    
    AjouterFace(bm, P) 

def tige(bm,x,y,z,e,d,sens,inclinaison, flipVertex = False):
    if sens == "DROITE":
        rectangle(bm, x, y, z, e, e, inclinaison, flipVertex)
        rectangle(bm, x + e, y, z, e, d, inclinaison, flipVertex)
        rectangle(bm, x + e + d, y, z, e, e, inclinaison, flipVertex)
        
    if sens == "BAS":
        rectangle(bm, x, y, z, e, e, inclinaison,flipVertex)
        rectangle(bm, x, y, z - e, d, e, inclinaison,flipVertex)
        rectangle(bm, x, y, z - e - d, e, e, inclinaison,flipVertex)

def cadre(bm,x,y,z,e,d,flipVertex = False):
    tige(bm,x,y,z,e,d, "DROITE", "FACE",flipVertex)
    tige(bm,x + e + d,y,z,e,d, "BAS", "FACE",flipVertex)
    tige(bm,x,y,z -e - d,e,d, "DROITE", "FACE",flipVertex)
    tige(bm,x,y,z,e,d, "BAS", "FACE",flipVertex)
    
def contour(bm, x, y, z, e, d):
    tige(bm,x,y,z,e,d, "DROITE", "COUCHE")
    tige(bm, x + 2.0 * e + d,y,z,e,d, "BAS", "COTE")
    tige(bm,x,y,z - 2 * e - d,e,d, "DROITE", "COUCHE", True)
    tige(bm, x,y,z,e,d, "BAS", "COTE", True)

def carre(bm, x,y,z,e,d):
    cadre(bm, x,y,z, e, d)
    cadre(bm, x, y + e, z, e, d, True)
    contour(bm, x,y,z,e,d)
    rectangle(bm,x + e,y,z - e,e,d, "COUCHE", True)
    rectangle(bm,x + e + d,y,z - e,d,e, "COTE", True)
    rectangle(bm,x + e,y,z - e - d,e,d, "COUCHE")
    rectangle(bm,x + e,y,z - e,d,e, "COTE")

def grille(m,n,d,e):
    bm = MaillageVide()
    x = 0.0 
    y = 0.0
    z = 0.0
    for i in range(0,m):
        z = i * (e + d)
        for j in range(0,n):
            x = j * (e + d)
            carre(bm, x,y,z,e,d)
                    
    FinaliserBmesh(bm)
    
if __name__ == "__main__":
    grille(3,4,1.0,0.1)