#from neopixel import Neopixel
import map


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
            print(f"white {i}")
        elif value == 5:
            #pixels.set_pixel(i, (0, 255, 0))  
            print(f"green {i}")
        elif value == 4:
            #pixels.set_pixel(i, (0, 0, 255))  
            print(f"blue {i}")
        elif value == 3:
            #pixels.set_pixel(i, (255, 0, 0))
            print(f"red {i}")
        elif value == 0:
            #pixels.set_pixel(i, (0, 0, 0))  
            print(f"black {i}")
        elif value == 6:
            #pixels.set_pixel(i, (0, 0, 0))  
            print(f"hitbox {i}")
        elif value == 7:
            #pixels.set_pixel(i, (255, 255, 255))  
            print(f"door {i}")

try:
     b=0
     while True:
          char=screen.getch()
          if char==curses.KEY_F2:

               break
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
