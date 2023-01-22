import pyautogui
import time

# First iterate the data

time.sleep(3)

file_to_automation = open('emission_2020.csv', 'r')

data = []

for line in file_to_automation:
    value = line.split('.')[0]
    data.append(int(value) * 10)


# Second parse the data to the Ableton file
MouseX = 350
MouseY = 250

step_increase_px = 14

i = 227


sleep_time = .1

print(f"Length: {len(data)}")

pyautogui.moveTo(MouseX, MouseY)


"""
while True:
    print(pyautogui.position())
"""

for _ in range(75):
    pyautogui.moveTo(MouseX, MouseY)
    time.sleep(sleep_time)

    pyautogui.rightClick()
    time.sleep(sleep_time)

    pyautogui.moveTo(MouseX + 5, MouseY + 5)
    time.sleep(sleep_time)

    pyautogui.press('return')
    time.sleep(sleep_time)

    pyautogui.write(str(data[i]))
    time.sleep(sleep_time)

    pyautogui.press('return')
    time.sleep(sleep_time)

    MouseY = pyautogui.position()[1]
    time.sleep(sleep_time)

    MouseX += step_increase_px    
    i += 1
    time.sleep(sleep_time)


print(f"Done! Next iteration start at {i}")
