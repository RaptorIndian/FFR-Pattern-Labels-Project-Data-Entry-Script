import pyautogui
import pandas as pd
import time

# Clicks the Chrome.png image.
CHROME = pyautogui.locateOnScreen('Chrome.png')
pyautogui.click(CHROME)
time.sleep(.5)

# Opens a new Chrome window.
pyautogui.hotkey('command', 'n')
time.sleep(.5)

# Clicks the "Tab" button.
TAB = pyautogui.locateOnScreen('Tab.png')
pyautogui.click(TAB)
time.sleep(.5)

# Clicks the "File" button.
FILE = pyautogui.locateOnScreen('File.png')
pyautogui.click(FILE)
time.sleep(.5)

# Clicks the "Download" button.
DOWNLOAD = pyautogui.locateOnScreen('Download.png')
pyautogui.click(DOWNLOAD)
time.sleep(.5)

# Clicks the "csv" button.
CSV = pyautogui.locateOnScreen('csv.png')
pyautogui.click(CSV)
time.sleep(.5)

# Read the CSV file with pandas.
directory = r'C:\Users\Raptor\Downloads\_FFR Pattern Labeling Project - Sheet1.csv'
# Create a loop that will run until the file is found.
loop = True
while loop:
    try:
        df = pd.read_csv(directory)
        loop = False
    except FileNotFoundError:
        print("File not found.")


# Create a new row in the CSV file.
df.loc[len(df.index)] = []

print(df)
