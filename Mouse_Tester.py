import keyboard
import mouse
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            print(f'Left mouse button clicked at ({x}, {y})')
        elif button == mouse.Button.right:
            print(f'Right mouse button clicked at ({x}, {y})')
        elif button == mouse.Button.x1:
            print(f'X1 (side) button clicked at ({x}, {y})')
        elif button == mouse.Button.x2:
            print(f'X2 (side) button clicked at ({x}, {y})')
        else:
            print(f'Other button clicked at ({x}, {y}) with {button}')
    else:
        print(f'Mouse released at ({x}, {y}) with {button}')

def on_scroll(x, y, dx, dy):
    print(f'Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})')

def test_mouse():
    print("Mouse Tester: Move the mouse, click, or scroll (press 'Esc' to exit).")
    
    listener = mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll
    )
    
    listener.start()
   
    keyboard.wait('esc')
    
    listener.stop()
    print("Exiting mouse tester.")

if __name__ == "__main__":
    test_mouse()
