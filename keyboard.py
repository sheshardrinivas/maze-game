import curses

import pyautogui
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
try:
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
          elif char==32:
              print("space")
        

finally:
     curses.nocbreak();screen.keypad(0);curses.echo();curses.endwin()
     pyautogui.hotkey("enter")
     