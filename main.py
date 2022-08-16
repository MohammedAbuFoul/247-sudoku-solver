import pyautogui
import keyboard
import win32api, win32con
from time import sleep

def possible(y, x, n):
    global grid
    for i in range (0, 9):
        if grid[y][i] == n:
            return False
    for i in range (0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range (0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range (1, 10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for g in grid:
        print(g)
        for a in g:
            ans.append(a)



def enter_key(x,y,k):
    xpos = int(sudku_left+x*square_size+.5*square_size)
    ypos = int(sudku_top+y*square_size+.5*square_size)
    win32api.SetCursorPos((xpos,ypos))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    sleep(.1)
    keyboard.press_and_release(k)
    sleep(.1)

    
def sudku_onscreen():
    # convert the game to array
    sudku_grid = []
    for y in range (9):
        row = []
        for x in range (9):
            for num in range (1,10,1):
                not_found = True
                if pyautogui.locateOnScreen(f'pic//{num}.png', region=(sudku_left+x*square_size, sudku_top+y*square_size, square_size, square_size), grayscale=True, confidence=0.85) !=None:
                    row.append(num)
                    not_found = False
                    break
            if not_found:
                row.append(0)
        sudku_grid.append(row)
    return sudku_grid


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

# read the game on screen solve it then enter the correct solution
ans = []
grid = sudku_onscreen()
for g in grid:
    print(g)

solve()

for y in range (9):
    for x in range (9):
        if grid[y][x] == 0:
            enter_key(x,y,str(ans[y*9+x]))
            