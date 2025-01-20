from pynput.mouse import Listener

def on_move(x, y):
    print(f"Pointer moved to ({x}, {y})")

# 마우스 움직임을 감지하는 리스너를 설정합니다.
with Listener(on_move=on_move) as listener:
    listener.join()
