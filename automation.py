import pyautogui
import time
import sys
import os

# --- CONFIGURATION ---
# 1. Open the text file
try:
    with open("continue_credentails.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: credentials.txt not found!")
    sys.exit()

# 2. Clean lines (remove empties)
lines = [line.strip() for line in lines if line.strip()]
# 3. Define Coordinates (From your request)
login_button_coords = (1370, 109)        # Click to open login modal / Open user menu
email_field_coords = (521, 464)         # Email input
password_field_coords = (546, 557)      # Password input
chose_number_of_vote = (396, 397)       # Select quantity
confirm_vote = (1012, 484)              # Confirm popup
logout_button_coords = (1348, 176)      # Logout button (inside menu)
vote_button=(1252,894)
profile_button = (417, 860)               
# --- START AUTOMATION ---

# Open Chrome once at the beginning
os.system('open -a "Safari"')
time.sleep(1) # Wait for Chrome to open

for line in lines:
    # 1. Parse Email and Password
    # Assumes format is "email:password" or "email|password" or "email password"
    # We will try to split by the first non-alphanumeric separator found
    if ":" in line:
        email, password = line.split(":", 1)
    elif "|" in line:
        email, password = line.split("|", 1)
    else:
        # Fallback: Split by space
        parts = line.split()
        if len(parts) >= 2:
            email = parts[0]
            password = parts[1]
        else:
            print(f"Skipping invalid line format: {line}")
            continue

    print(f"Processing: {email}")

    # 2. Click Login Button (Mở nút đăng nhập)
    #pyautogui.click(login_button_coords)
    #time.sleep(1) # Wait for login form to appear
    pyautogui.hotkey('command', 'l')
    pyautogui.write('https://giaithuongngoisaoxanh.1vote.vn/dang-nhap')
    pyautogui.press('enter')

    time.sleep(3)
    # 3. Enter Email
    pyautogui.click(email_field_coords)
    # Select all and delete (in case something is already there)
    pyautogui.hotkey('command', 'a') 
    pyautogui.press('backspace')
    pyautogui.write(email)
    time.sleep(0.5)

    # 4. Enter Password
    pyautogui.click(password_field_coords)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('backspace')
    pyautogui.write(password)
    time.sleep(0.5)

    # 5. Press Enter to Login
    pyautogui.press('enter')
    time.sleep(3) # Wait for page to reload/login to complete
    
    try:
    # --- CHECK FOR UNVERIFIED ALERT ---
        pyautogui.locateOnScreen('alert_popup.png', confidence=0.8) 
        print(f"⚠️ Account {email} is NOT VERIFIED. Skipping...")

        # 1. Click on a "safe" empty spot to dismiss the popup
        # (I used x=200, y=200 assuming it's empty background space)
        pyautogui.click(700, 700) 
        time.sleep(1)

        pyautogui.hotkey('command', 'l')
        pyautogui.write('https://giaithuongngoisaoxanh.1vote.vn/dang-nhap')
        pyautogui.press('enter')
        continue 
    # ----------------------------------
    except pyautogui.ImageNotFoundException:
        # The image was NOT found. This is good! 
        # It means the account is verified. We do nothing and continue down.
        pass




    #print("Scrolling down...")
    #scroll_end_time = time.time() + 1.3
    #while time.time() < scroll_end_time:
        # On Mac: Positive is usually UP, Negative is DOWN. 
        # If this scrolls UP, change -10 to 10.
        #pyautogui.scroll(-10) 
        #time.sleep(0.5)
# # 6. Scroll Until Vote Button is Found
#     print("Looking for Vote button...")
    
#     vote_btn_location = None
#     max_scroll_attempts = 20  
#     attempts = 0

#     while vote_btn_location is None and attempts < max_scroll_attempts:
#         try:
#             # Check if button is visible
#             vote_btn_location = pyautogui.locateCenterOnScreen('vote_button.png', confidence=0.8)
            
#             if vote_btn_location:
#                 print("Found Vote button!")
#                 break # Exit the loop immediately
            
#         except pyautogui.ImageNotFoundException:
#             pass # Not found yet, keep going

#         # Not found yet? Scroll down and wait
#         print("Not found, scrolling down...")
#         pyautogui.scroll(-15) # Adjust speed if needed (negative is down)
#         time.sleep(0.5)       # Wait for page to render
#         attempts += 1

#     # 7. Click the Button (if found)
#     if vote_btn_location:
#         # Optional: sometimes the button is at the very bottom edge
#         # and clicking fails. It helps to scroll a TINY bit more just in case.
#         pyautogui.scroll(-5) 
#         time.sleep(0.5)
        
#         # Recalculate position in case the extra scroll moved it
#         try:
#             vote_btn_location = pyautogui.locateCenterOnScreen('vote_button.png', confidence=0.8)
#             pyautogui.click(vote_btn_location)
#         except:
#              # If recalculation fails, try clicking the old spot
#             pyautogui.click(vote_btn_location)
            
#         time.sleep(1.5)
#     else:
#         print(f"❌ Error: Could not find vote button for {email}. Skipping...")
#         # You might want to add logout logic here if it fails
#         continue 

    
  # Click profile Button
    #pyautogui.click(profile_button)
    #time.sleep(1)


    time.sleep(0.5)

    pyautogui.hotkey('command', 'l')
    pyautogui.write('https://giaithuongngoisaoxanh.1vote.vn/thi-sinh/lifkt/lam-thanh-my-(vai-nguyen-thi-nhai---phim-khe-uoc-ban-dau)-pzK4')
    pyautogui.press('enter')
    time.sleep(4)
    # 7. Click vote Button
    pyautogui.click(vote_button)
    time.sleep(2)
    # 8. Choose Number of Vote
    pyautogui.click(chose_number_of_vote)
    time.sleep(1)

    # 9. Confirm Vote
    pyautogui.click(confirm_vote)
    time.sleep(2) # Wait for vote to process

    pyautogui.hotkey('command', 'r')
    time.sleep(3)
    # 11. Log Out Process
    # Click the avatar/login area again to open menu
    pyautogui.click(login_button_coords) 
    time.sleep(0.5)
    # Click Logout
    pyautogui.click(logout_button_coords)
    print(f"Finished {email}. Logging out...")
    
    # Wait for logout to complete before starting next loop
    time.sleep(5) 

print("All accounts processed.")
