from tkinter import *
from collections import deque

sizeHash = 198953
hashtable = [0] * sizeHash

class Node:
    def __init__(self, x, y):
        self.x = x  
        self.y = y
  
def insertHT(x,y):
  global hashtable
  s = str(x)+':'+str(y)
  
  h = hash(s)

  no = Node(x,y)

  hashtable[h] = no

def dynamicPrimes():
  ans = []
  n = 40
  prime = [True for i in range(n + 1)]
  p = 2

  while (p * p <= n):
    if (prime[p] == True):
      for i in range(p ** 2, n + 1, p):
        prime[i] = False
    p += 1

  prime[0]= False
  prime[1]= False

  for p in range(n + 1):
    if prime[p]:
      ans.append(p)
    
  return ans


def hash(s):
  h = 0
  a = 31415
  b = 27183

  array = dynamicPrimes()

  for i in s:
    a = a * b % (sizeHash - 1);
    h = (a * h + array[ord(i)-48]) % sizeHash;
  return h;

def checkIfNot(x,y):
  global hashtable
  s = str(x)+','+str(y)
  
  h = hash(s)

  if hashtable[h] == 0:
    return True


  if hashtable[h].x == x and hashtable[h].y == y:
    return False
  else:
    return True

 

def changeColor(newColor):
    global new_color
    new_color = newColor


def locate_xy(event):
    global selected_x, selected_y
    selected_x, selected_y = event.x, event.y
    fill(selected_x, selected_y)





def fill(x, y):
    areaColor = image.get(x, y)

    if new_color == areaColor:
        return

    q = deque()
    q.append((x, y))


    v = {}

    while q:
        px, py = q.popleft()

        if px - 1 >= 0 and image.get(px-1, py) == areaColor and checkIfNot(px - 1, py):
              insertHT(px-1,py)
              q.append((px-1, py))
              image.put(new_color, (px-1, py))

        if px + 1 < w and image.get(px+1, py) == areaColor  and checkIfNot(px + 1, py):
              insertHT(px + 1,py)
              q.append((px+1, py))
              image.put(new_color, (px+1, py))

        if py - 1 > 0 and image.get(px, py-1) == areaColor  and checkIfNot(px, py - 1):
              insertHT(px, py - 1)
              q.append((px, py-1))
              image.put(new_color, (px, py-1))
              
        if py + 1 < w and image.get(px, py+1) == areaColor  and checkIfNot(px, py + 1):
              insertHT(px, py + 1)
              q.append((px, py+1))
              image.put(new_color, (px, py+1))


new_color = 'red'
w = 444
h = 444


selected_x, selected_y = 0, 0

root = Tk()
root.title('Jogo Colorir projeto Final!')
image = PhotoImage(file="pa.ppm")

canvas = Canvas(root, background='white', width=w, height=h)
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', locate_xy)
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_command(
    label='Vermelho', command=lambda: changeColor('red'))
menubar.add_command(label='Verde', command=lambda: changeColor('green'))
menubar.add_command(label='Azul', command=lambda: changeColor('blue'))
menubar.add_command(label='Roxo', command=lambda: changeColor('purple'))
menubar.add_command(label='Marrom', command=lambda: changeColor('brown4'))
menubar.add_command(label='Amarelo', command=lambda: changeColor('yellow'))

root.mainloop()
