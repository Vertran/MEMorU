import json
import os

__all__ = ['shared_data', 'root', 'deep_s', 'COLORS']

def root(iter):
    if iter > 1:
        path = os.path.dirname(os.path.abspath(__file__))
        for _ in range(iter - 1):
            path = os.path.dirname(path)
    elif iter == 1:
        path = os.path.dirname(os.path.abspath(__file__))
    else:
        path = os.path.abspath(__file__)
    
    return path

def deep_s(arr, path):
    keys = path.split('.')
    for key in keys:
        arr = arr[key]
    return arr

root = root(2)

class COLORS:
    BLACK      = (0, 0, 0)
    WHITE      = (255, 255, 255)
    RED        = (255, 0, 0)
    LIME       = (0, 255, 0)
    BLUE       = (0, 0, 255)
    YELLOW     = (255, 255, 0)
    CYAN       = (0, 255, 255)
    MAGENTA    = (255, 0, 255)
    SILVER     = (192, 192, 192)
    GRAY       = (128, 128, 128)
    MAROON     = (128, 0, 0)
    OLIVE      = (128, 128, 0)
    GREEN      = (0, 128, 0)
    PURPLE     = (128, 0, 128)
    TEAL       = (0, 128, 128)
    NAVY       = (0, 0, 128)

shared_data = {
    'screen': [640, 480, 'fullscreen'],
    'window': None,
    'UI': {
        'menu': None,
        'submenu': None,
        'draw_q': {
            'buttons': [],
            'overlays': [],
            'text': [],
            'images': []
        }
    },
    'path': {
        'root': root,
        'data': os.path.join(root, 'data'),
        'fonts': os.path.join(root, 'data', 'fonts'),
    }
}