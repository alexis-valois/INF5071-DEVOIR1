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

def grille(m,n,d,e):
    bm = MaillageVide()
    v1 = mathutils.Vector((0.0, 0.0, 0.0))
    v2 = mathutils.Vector((-1.0, 0.0, 0.0))
    v3 = mathutils.Vector((-1.0, 1.0, 0.0))
    v4 = mathutils.Vector((0.0, 1.0, 0.0))
    
    s1 = AjouterSommet(bm, v1)
    s2 = AjouterSommet(bm, v2)
    s3 = AjouterSommet(bm, v3)
    s4 = AjouterSommet(bm, v4)
    
    P = [s1, s2, s3, s4]
    
    AjouterArrete(bm, s1, s2)
    AjouterArrete(bm, s2, s3)
    AjouterArrete(bm, s3, s4)
    AjouterArrete(bm, s4, s1)
    
    AjouterFace(bm, P)
    
    FinaliserBmesh(bm)
    
if __name__ == "__main__":
    grille(3,4,0.1,1.0)