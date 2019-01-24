
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,255)
w = (0 ,255 ,0)
g = (255,169,169)

x =1
y =1



def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    
    if 1 < pitch < 179 and x!= 0:
        new_x -= 1
        
    elif 359 > pitch > 181 and x != 7:
        new_x +=1
        
    if 1 < roll < 179 and y!= 7:
        new_y += 1
        
    elif 359 > roll > 181 and y != 0:
        new_y -=1
    
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y

def check_wall(x,y,new_x,new_y):
    
    if maze[new_y][new_x] != r:
        return new_x, new_y
    
    elif maze[new_y][x] != r:
        return x, new_y
    
    elif maze[y][new_x]!= r:
        return new_x, y
    else:
        
        return x,y



maze =[[r,r,r,r,r,r,r,r],
       [r,b,b,b,b,b,b,r],
       [r,r,r,b,r,b,b,r],
       [r,b,r,b,r,r,r,r],
       [r,b,b,b,b,b,b,r],
       [r,b,r,r,r,r,b,r],
       [r,g,b,r,b,b,b,r],
       [r,r,r,r,r,r,r,r]]


game_over = False


while game_over == False:
    
    
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch,roll,x,y)
    if maze[y][x] == g:
        sense.show_message("win!")
        game_over = true
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.05)
    maze[y][x] = b
    


