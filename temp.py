import pyautogui

x, y = 180, 457
expected_color = (75, 219, 106)

while True:
    color = pyautogui.pixel(x, y)
    print(color)
    if color == expected_color:
        pyautogui.click()
        break;
