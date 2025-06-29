import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "16-bit Blue", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # 16-bit blue (RGB565): 0x001F -> (0, 0, 31)
    # Normalize to [0,1]: (0/31, 0/63, 31/31) = (0, 0, 1)
    blue_color = (0.0, 0.0, 1.0, 1.0)

    while not glfw.window_should_close(window):
        glClearColor(*blue_color)
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()