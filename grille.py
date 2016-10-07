import bpy, mathutils

def MaillageVide():
    m = bpy.data.meshes.new(name="Grille")
    ob = bpy.data.objects.new("Grille", m)
    ob.show_name = True
    bpy.context.scene.objects.link(ob)
    return m    

def AjouterSommet(mesh, p):
    mesh.vertices.add(1)
    mesh.vertices[-1].co = p
        
def AjouterArrete(mesh, idx1, idx2):
    mesh.edges.add(1)
    mesh.edges[-1].vertices = [idx1, idx2]
    mesh.loops.add(1)
    mesh.loops[-1].edge_index = len(mesh.edges) - 1
    mesh.loops[-1].vertex_index = idx1
 
def AjouterFace(mesh, P):
    mesh.polygons.add(1)
    mesh.polygons[-1].vertices = P

def grille(m,n,d,e):
    m = MaillageVide()
    v1 = mathutils.Vector((0.0, 0.0, 0.0))
    v2 = mathutils.Vector((-1.0, 0.0, 0.0))
    v3 = mathutils.Vector((-1.0, 1.0, 0.0))
    v4 = mathutils.Vector((0.0, 1.0, 0.0))
    
    P = [0, 1, 2, 3]
    
    AjouterSommet(m, v1)
    AjouterSommet(m, v2)
    AjouterSommet(m, v3)
    AjouterSommet(m, v4)
    
    AjouterArrete(m, 0, 1)
    AjouterArrete(m, 1, 2)
    AjouterArrete(m, 2, 3)
    AjouterArrete(m, 3, 4)
    
    AjouterFace(m, P)
    
    m.update()
    m.validate(True)

if __name__ == "__main__":
    grille(3,4,0.1,1.0)