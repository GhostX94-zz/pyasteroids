"""
    Code for interpreting a .ply file
    as a OpenGL polygon mesh
"""

from OpenGL.GL import *

from model.ply import PLYModel


class GLModel(object):
    def __init__(self, file):
        self.ply = PLYModel(file)
        
        self.setup_dl = None
        self.main_dl = None
        
        if (not 'vertex' in self.ply or not 'face' in self.ply):
            raise Exception('Invalid PLY model')
        
        self.generate_textures()
        self.generate_display_list()
    
    def generate_textures(self):
        # TODO: use texture information on the PLYMode, if existing
        pass
    
    def generate_display_list(self):
        self.main_dl = glGenLists(1)
        
        faces = self.ply['face']
        vertex_list = self.ply['vertex']
        
        glNewList(self.main_dl, GL_COMPILE)
        for f in faces:
            v_index_l = f['vertex_indices']
            
            if (len(v_index_l) == 3):
                glBegin(GL_TRIANGLES)
            else:
                glBegin(GL_QUADS)
                
            for v in (vertex_list[i] for i in v_index_l):
                glNormal3f(v['nx'],v['ny'],v['nz'])
                # TODO: use texture information on the PLYMode, if existing
                glVertex3f(v['x'],v['y'],v['z'])
            
            glEnd()
        glEndList()
        
        # send the giant model dictionary to the gc
        del self.ply
    
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        if (self.setup_dl is not None):
            glCallList(self.setup_dl)
        
        glCallList(self.main_dl)
        
        glPopMatrix()
    

# Testing
if (__name__ == '__main__'):  
    f = open('../resources/models/long-spaceship/long-spaceship.ply')
    
    try:
        model = GLModel(f)
    finally:
        f.close()