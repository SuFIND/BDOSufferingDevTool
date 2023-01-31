import random
import time
import sys
import keyboard
import mouse
from ctypes import windll

if sys.platform == "win32":
    # 只有windows 才可以导入
    import win32api, win32con

# 定义使用keyboard库仿真但是未能达到预期的按键
VK_CODE = {
    '/': 191,
}

keybd_event = windll.user32.keybd_event


class HumanSimulate:
    MinOpDelay = 60
    MaxOpDelay = 80

    @classmethod
    def human_delay(cls) -> None:
        time.sleep(random.randint(cls.MinOpDelay, cls.MaxOpDelay) / 1000)


class MouseSimulate(HumanSimulate):
    MinOpDelay = 80
    MaxOpDelay = 140
    LEFT = mouse.LEFT
    RIGHT = mouse.RIGHT
    SCROLLUP = 1
    SCROLLDOWN = -1

    @classmethod
    def move(cls, x, y, absolute=True, duration=0) -> bool:
        mouse.move(x, y, absolute=absolute, duration=duration)
        cls.human_delay()
        return True

    @classmethod
    def click(cls, button=LEFT) -> bool:
        mouse.press(button=button)
        cls.human_delay()
        mouse.release(button=button)
        cls.human_delay()
        return True

    @classmethod
    def press(cls, button=LEFT) -> bool:
        mouse.press(button=button)
        cls.human_delay()
        return True

    @classmethod
    def release(cls, button=LEFT) -> bool:
        mouse.release(button=button)
        cls.human_delay()
        return True

    @classmethod
    def scroll(cls, x, y, scroll_type=SCROLLDOWN) -> bool:
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, scroll_type, 0)
        cls.human_delay()
        return True


class KeyboardSimulate(HumanSimulate):
    MinOpDelay = 50
    MaxOpDelay = 80

    @classmethod
    def press_and_release(cls, key) -> bool:
        if key in VK_CODE:
            hex_vk_code = VK_CODE[key]
            scan_code = keyboard.key_to_scan_codes(key)[1]
            keybd_event(hex_vk_code, scan_code, 0, 0)
            keybd_event(hex_vk_code, scan_code, 2, 0)
        else:
            keyboard.press_and_release(key)
        cls.human_delay()
        return True

    @classmethod
    def press(cls, key) -> bool:
        if key in VK_CODE:
            hex_vk_code = VK_CODE[key]
            scan_code = keyboard.key_to_scan_codes(key)[1]
            keybd_event(hex_vk_code, scan_code, 0, 0)
        else:
            keyboard.press(key)
        cls.human_delay()
        return True

    @classmethod
    def release(cls, key) -> bool:
        if key in VK_CODE:
            hex_vk_code = VK_CODE[key]
            scan_code = keyboard.key_to_scan_codes(key)[1]
            keybd_event(hex_vk_code, scan_code, 2, 0)
        else:
            keyboard.release(key)
        cls.human_delay()
        return True
