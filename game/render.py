#render.py
from data_exch import *
from UI import Text

from OpenGL.GL import *
from OpenGL.GL import glMatrixMode, glLoadIdentity, GL_PROJECTION, GL_MODELVIEW
from OpenGL.GLU import gluOrtho2D
import glfw
import os

def render():
    if not glfw.init():
        return

    shared_data['window'] = window = glfw.create_window(*shared_data['screen'][:2], "16-bit Blue", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    root = shared_data['path']['root']

    # Separate positions for text and square
    text_x, text_y = 100, 100  # Move text away from square
    square_x, square_y, size = 50, 50, 50

    # Try multiple font paths
    font_paths = [
        'C:\\Windows\\Fonts\\arial.ttf',  # Note: lowercase
        'C:\\Windows\\Fonts\\Arial.ttf',
        f'{root}\\game\\data\\fonts\\HomeVideoBold-R90Dv.ttf',
        # Add fallback system fonts
        '/System/Library/Fonts/Arial.ttf',  # macOS
        '/usr/share/fonts/truetype/arial.ttf',  # Linux
    ]
    
    font_path = None
    for path in font_paths:
        try:
            if os.path.exists(path):
                font_path = path
                break
        except:
            continue
    
    if not font_path:
        print("No font file found! Text will not render.")
    
    font_path = "c:/Games/MEMorU/game/data/fonts/HomeVideo-BLG6G.ttf"

    try:
        PAUSE_TEXT = Text("PAUSE", (text_x, text_y), font_path, COLORS.WHITE)
        print(f"Successfully loaded font: {font_path}")
    except Exception as e:
        print(f"Error creating text: {e}")
        return

    width, height = shared_data['screen'][:2]

    while not glfw.window_should_close(window):
        glClearColor(*COLORS.BLUE, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Set up orthographic projection for 2D rendering
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, width, height, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Draw text first (so it appears on top)
        try:
            PAUSE_TEXT.draw()
        except Exception as e:
            print(f"Error drawing text: {e}")

        

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

render()