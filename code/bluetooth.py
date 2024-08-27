import pygame
import time

# Initialize pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Assuming the PS5 controller is the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Connected to {joystick.get_name()}")

# Run the loop to check directional inputs
try:
    while True:
        pygame.event.pump()

        # Axis 0 and 1 correspond to the left stick's x and y axes
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        # Dead zone threshold
        threshold = 0.1

        # Determine direction
        if x_axis < -threshold:
            print("Left")
        elif x_axis > threshold:
            print("Right")

        if y_axis < -threshold:
            print("Up")
        elif y_axis > threshold:
            print("Down")

        # Add a small delay to avoid flooding the console
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Quit pygame
    pygame.quit()
