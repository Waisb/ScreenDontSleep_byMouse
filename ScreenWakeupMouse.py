import win32api
import time

MOUSE_MOVE_TIMEOUT = 120 # Таймаут для мува
MOUSE_PX_SPREAD = 100 #Целое положительное или отрицательное число для отдаления

def get_mouse_position():
    # Получить текущую позицию курсора
    x, y = win32api.GetCursorPos()
    return x, y
def move_mouse(x, y):
    # Изменить позицию курсора
    win32api.SetCursorPos((x, y))

try:
    while True:
        x, y = get_mouse_position()
        print(f"[+] Current mouse position: X={x}, Y={y}")
        move_mouse(x+MOUSE_PX_SPREAD, y+MOUSE_PX_SPREAD)
        x, y = get_mouse_position()
        print(f"[+] Moved to position: X={x}, Y={y}")
        time.sleep(MOUSE_MOVE_TIMEOUT)
except KeyboardInterrupt:
    pass

