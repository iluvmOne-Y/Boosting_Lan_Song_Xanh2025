
import pyautogui
import time
import sys
import os   

profile_button = (417, 860)                # Main Vote button
login_button_coords = (1372, 234)       
# Click to open login modal / Open user menu
logout_button_coords = (1337, 286)      # Logout button (inside menu)
os.system('open -a "Safari"')
print("Scrolling down...")
scroll_end_time = time.time() + 1.3
while time.time() < scroll_end_time:
        # On Mac: Positive is usually UP, Negative is DOWN. 
        # If this scrolls UP, change -10 to 10.
    pyautogui.scroll(-10) 
    time.sleep(0.1)

    # 7. Click profile Button
pyautogui.click(profile_button)
time.sleep(1)
