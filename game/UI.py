#UI.py
from data_exch import *
from OpenGL.GL import *
import freetype
import glfw
import os
import numpy as np

class Text:
    def __init__(self, text, position, font, color=(1.0, 1.0, 1.0)):
        self.text = text
        self.x, self.y = position
        self.color = color
        
        if not os.path.isfile(font):
            raise FileNotFoundError(f"Font file not found: {font}")
            
        self.face = freetype.Face(font)
        self.face.set_char_size(48*64)  # 48pt font
        
        # Pre-render all characters to textures
        self.char_textures = {}
        self.char_info = {}
        self._preload_characters()
    
    def _preload_characters(self):
        """Pre-render characters to OpenGL textures"""
        for ch in self.text:
            if ch in self.char_textures:
                continue
                
            self.face.load_char(ch)
            bitmap = self.face.glyph.bitmap
            
            if bitmap.width == 0 or bitmap.rows == 0:
                continue
            
            # Convert bitmap to numpy array
            data = np.array(bitmap.buffer, dtype=np.ubyte).reshape(bitmap.rows, bitmap.width)
            
            # Create RGBA texture (white text with alpha)
            rgba_data = np.zeros((bitmap.rows, bitmap.width, 4), dtype=np.ubyte)
            rgba_data[:, :, 0] = 255  # Red
            rgba_data[:, :, 1] = 255  # Green  
            rgba_data[:, :, 2] = 255  # Blue
            rgba_data[:, :, 3] = data  # Alpha from bitmap
            
            # Generate OpenGL texture
            texture_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, bitmap.width, bitmap.rows, 0, 
                        GL_RGBA, GL_UNSIGNED_BYTE, rgba_data)
            
            self.char_textures[ch] = texture_id
            self.char_info[ch] = {
                'width': bitmap.width,
                'height': bitmap.rows,
                'bearing_x': self.face.glyph.bitmap_left,
                'bearing_y': self.face.glyph.bitmap_top,
                'advance': self.face.glyph.advance.x >> 6
            }

    def draw(self):
        """Draw text using OpenGL textures"""
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_TEXTURE_2D)
        
        glColor3f(*self.color)
        
        pen_x = self.x
        pen_y = self.y
        
        for ch in self.text:
            if ch not in self.char_textures:
                continue
                
            texture_id = self.char_textures[ch]
            info = self.char_info[ch]
            
            # Calculate positions
            xpos = pen_x + info['bearing_x']
            ypos = pen_y - (info['height'] - info['bearing_y'])
            w = info['width']
            h = -info['height']
            
            # Bind texture and draw quad
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0); glVertex2f(xpos, ypos + h)
            glTexCoord2f(1.0, 0.0); glVertex2f(xpos + w, ypos + h)
            glTexCoord2f(1.0, 1.0); glVertex2f(xpos + w, ypos)
            glTexCoord2f(0.0, 1.0); glVertex2f(xpos, ypos)
            glEnd()
            
            # Advance to next character position
            pen_x += info['advance']