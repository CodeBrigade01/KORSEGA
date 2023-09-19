import pyautogui
import time

# Adjust these coordinates based on your screen resolution and browser window size
search_box_x = 300
search_box_y = 100

# Open your web browser (e.g., Mozilla Firefox)
pyautogui.hotkey('win', 's')
pyautogui.write('Mozilla Firefox')
pyautogui.press('enter')

# Wait for Firefox to open (adjust the sleep time as needed)
time.sleep(3)

# Go to YouTube
pyautogui.write('youtube.com')
pyautogui.press('enter')

# Wait for YouTube to load (adjust the sleep time as needed)
time.sleep(5)

# Click the search box
pyautogui.click(search_box_x, search_box_y)

# Type the search query
pyautogui.write('how to cook')

# Press Enter to perform the search
pyautogui.press('enter')

# Wait for the search results to load (adjust the sleep time as needed)
time.sleep(5)

# Click on the first video in the search results
pyautogui.hotkey('tab', 'tab')  # Navigate to the first search result
pyautogui.press('enter')  # Open the selected video

# Wait for the video page to load (adjust the sleep time as needed)
time.sleep(5)

# Extract the URL of the video from the browser's address bar
pyautogui.hotkey('ctrl', 'l')  # Select the address bar
pyautogui.hotkey('ctrl', 'c')  # Copy the URL
video_url = pyautogui.hotkey('ctrl', 'v')  # Paste the URL into a variable

# Print the video URL
print("First YouTube Video URL:", video_url)