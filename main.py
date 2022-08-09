import pyautogui
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    
def number_detact(x,y):
    for num in range (1, 10, 1):
        if pyautogui.locateOnScreen(f'pic//{num}.png', region=(sudku_left+x*square_size, sudku_top+y*square_size, square_size, square_size), grayscale=True, confidence=0.85) !=None:
            return num
    return 0


# gets the edge of the sudoku puzzle
ul = pyautogui.locateOnScreen('pic//ul.png', grayscale=True, confidence=0.8)
dr = pyautogui.locateOnScreen('pic//dr.png', grayscale=True, confidence=0.8)

# if the game is not found exit the script
if ul == None or dr == None:
    print('not found')
    exit()

# the diminsions of the game
sudku_left = ul[0]+16
sudku_top = ul[1]+16
sudku_width = dr[0]-ul[0]-16
sudku_length = dr[1]-ul[1]-16
square_size = int(sudku_width/9)

# convert the game to array
sudku_grid = []
for y in range (9):
    row = []
    for x in range (9):
        row.append(number_detact(x,y))
    sudku_grid.append(row)

    
