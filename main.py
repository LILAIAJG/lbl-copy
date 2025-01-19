import pyperclip
import keyboard
import time

def paste_clipboard_line_by_line():
    clipboard_content = pyperclip.paste()
    lines = clipboard_content.split('\n')
    
    for line in lines:
        keyboard.write(line)
        keyboard.press_and_release('enter')
        time.sleep(0.1)  # 可根据需要调整延迟时间

# 监听快捷键（例如 Ctrl+Shift+V）
keyboard.add_hotkey('shift+v', paste_clipboard_line_by_line)

print("按下 Ctrl+Shift+V 逐行粘贴剪贴板内容")
keyboard.wait('esc')  # 按下 Esc 键退出程序