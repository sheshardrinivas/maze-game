#from neopixel import Neopixel
import map
import datetime

#pixels = Neopixel(100, 0, 6, "RGB")
import curses

import pyautogui
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
b=0
def render_map():
    for i , value in enumerate(reversed(map.game_map_level1)):
        if value == 1:
            #pixels.set_pixel(i, (255, 255, 255)) 
            print(f"white {i+1}")
        elif value == 5:
            #pixels.set_pixel(i, (0, 255, 0))  
            print(f"green {i+1}")
        elif value == 4:
            #pixels.set_pixel(i, (0, 0, 255))  
            print(f"blue {i+1}")
        elif value == 3:
            #pixels.set_pixel(i, (255, 0, 0))
            print(f"red {i+1}")
        elif value == 0:
            #pixels.set_pixel(i, (0, 0, 0))  
            print(f"black {i+1}")
        elif value == 6:
            #pixels.set_pixel(i, (0, 0, 0))  
            print(f"hitbox {i+1}")
        elif value == 7:
            #pixels.set_pixel(i, (255, 255, 255))  
            print(f"door {i+1}")

try:
     b=0
     while True:
          char=screen.getch()
          if char==curses.KEY_F2:

               break
          elif char==curses.KEY_UP or char==119:
               print("up")
          elif char==curses.KEY_DOWN or char==115:
            print("down")
          elif char==curses.KEY_RIGHT or char==100:
                 print("right")
          elif char==curses.KEY_LEFT or char==97:
              print("left")
          if char==114:
              print("r")
              b=1
              break 
          
             
        

finally:
     curses.nocbreak();screen.keypad(0);curses.echo();curses.endwin()
     if b==1:
          render_map()
     else:
           pyautogui.hotkey("enter")
     


#pixels.setBrightness(0.1)  
#pixels.show()  
