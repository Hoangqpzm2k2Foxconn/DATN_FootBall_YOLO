# from pynput import mouse, keyboard

# last_event = None
# check = False
# # Khởi tạo controller cho bàn phím
# keyboard_controller = keyboard.Controller()

# def on_click(x, y, button, pressed):
#     global last_event
#     global check
#     if pressed:
#         last_event = f"Chuột nhấn {button} tại ({x}, {y})"
#         print(last_event)
#     else:
#         last_event = f"Chuột thả {button} tại ({x}, {y})"
#         print(last_event)
#         check = True  # Chuột đã thả, sẵn sàng thực hirrện click
#         print("Chuột đã thả, sẵn sàng click lại.")
        
#         # Nếu check = True, nhấn phím 'r'
#         if check:
#             keyboard_controller.press('r')
#             keyboard_controller.release('r')
#             print("Phím 'r' đã được nhấn.")
# print("test")
# listener = mouse.Listener(on_click=on_click)
# listener.start()  # Bắt đầu lắng nghe sự kiện chuột trong nền


       
# import pyautogui
# import keyboard
# x, y = 1877,338 


# def click_at_position():
#     pyautogui.click(x, y)

# # Chạy chương trình và chờ người dùng nhấn 'r'
# print("1Nhấn 'r' để click chuột vào tọa độ (100, 200) và quay lại vị trí ban đầu.")
# while True:
#     if keyboard.is_pressed('r'):  # Kiểm tra nếu phím 'r' được nhấn
#         click_at_position()  # Click chuột vào tọa độ
#         print(f"Chuột đã click tại tọa độ ({x}, {y})")
#         pyautogui.moveTo(1000, 520)
#     if keyboard.is_pressed('esc'):
#         listener.stop
#     if keyboard.is_pressed('r'):
#         listener = mouse.Listener(on_click=on_click)
#         listener.start()  # Bắt đầu lắng nghe sự kiện chuột trong nền
    


    
    












############################

import pyautogui
import keyboard

# Tọa độ đã được chỉ định trước
x, y = 1877,338  # Thay đổi tọa độ theo mong muốn của bạn

# Lưu vị trí chuột ban đầu
initial_x, initial_y = pyautogui.position()

# Hàm để click chuột vào tọa độ đã chỉ định
def click_at_position():
    pyautogui.click(x, y)

# Chạy chương trình và chờ người dùng nhấn 'r'
print("1Nhấn 'r' để click chuột vào tọa độ (100, 200) và quay lại vị trí ban đầu.")
while True:
    if keyboard.is_pressed('Alt'):  # Kiểm tra nếu phím 'r' được nhấn
        click_at_position()  # Click chuột vào tọa độ
        print(f"Chuột đã click tại tọa độ ({x}, {y})")
        # Quay lại vị trí chuột ban đầu
        pyautogui.moveTo(1000, 520)
        print(f"Chuột đã quay lại vị trí ban đầu ({initial_x}, {initial_y})")
    if keyboard.is_pressed('esc'):
        break

################################
# import pyautogui
# import time

# print("Di chuyển chuột để lấy tọa độ. Nhấn Ctrl+C để dừng chương trình.")
# #1877 338
# #1000.520
# try:
#     while True:
#         # Lấy tọa độ hiện tại của con trỏ chuột
#         x, y = pyautogui.position()
        
#         # In tọa độ lên màn hình (xóa dòng trước đó)
#         print(f"Tọa độ hiện tại: ({x}, {y})", end="\r", flush=True)
        
#         # Đợi một chút để giảm tải CPU
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     print("\nChương trình đã dừng.")
