import pandas as pd
import sys
import time
import pyautogui

known_patterns = {"jacks": "jacks", "mini-jacks": "mini-jacks", "jump-jacks": "jump-jacks", "split-jump-jacks": "split-jump-jacks", "hand-jacks": "hand-jacks", "anchors": "anchors", "streams": "streams", "running-men": "running-men", "polyrhythms": "polyrhythms", "jump-streams": "jump-streams", 'hand-streams': 'hand-streams', 'bursts': 'bursts', 'trills': 'trills', 'jump-trills': 'jump-trills', 'split-jump-trills': 'split-jump-trills', 'one-hand-trills': 'one-hand-trills', 'rolls': 'rolls', 'split-rolls': 'split-rolls', 'jump-gluts': 'jump-gluts', 'flams': 'flams', "jack": "jacks", "mini jacks": "mini-jacks", "jump jacks": "jump-jacks", "split jump jacks": "split-jump-jacks", "hand jacks": "hand-jacks", "poly rhythms": "polyrhythms", "jump streams": "jump-streams", "hand streams": "hand-streams", "jumptrills": "jump-trills", "jump trills": "jump-trills", "split jumptrills": "split-jump-trills", "one hand trills": "one-hand-trills", "split rolls": "split-rolls", "jump gluts": "jump-gluts", "minijacks": "mini-jacks", "mini jacks": "mini-jacks", "jumpjacks": "jump-jacks", "jump jacks": "jump-jacks", "split jumpjacks": "split-jump-jacks", "handjacks": "hand-jacks", "runningmen": "running-men", "running men": "running-men", "grace": "flams", "irregular": "irregular"}

labels_list = []

Nths = ["64th", "48th", "32nd", "24th", "16th", "12th", "8th", "4th"]
Na = ["64ths", "48ths", "32nds", "24ths", "16ths", "12ths", "8ths", "4ths"]

username = "Laplace"
labels = """
Entrance [Deemo Cut] - 12th Jacks, 12th Hand-Jacks, 12th Jump-Streams | Certain

Sunshine rainy [Heavy] - 24th Bursts, 16th Jump-Streams, 16th Mini-Jacks | Certain
"""
contents = labels.split("\n")

# Remove empty lines.
contents = [x for x in contents if x != ""]

for data in contents:

    # Check how many times the word "Certain" or "Uncertain" appears in the data


    certain_count = data.count("Certain")
    uncertain_count = data.count("Uncertain")
    # If the word "Certain" appears more than once, then there is multiple labels.
    if certain_count > 1 and uncertain_count > 1:
        # Add a \n after the word "Certain" or "Uncertain".
        data = data.replace("Certain\n", "Certain ")

        data = data.replace("Uncertain\n", "Uncertain ")

        # Split the data into lists of labels.
        data_list = data.split("\n")

    # Separate the song name from the rest of the data.
    song_name = data.split(":")
    if len(song_name) == 2:
        song_name = song_name[0].title()
        # Remove the song name from the data.
        data = data.replace(song_name + ":", "")

    # If the song name is not found, try to separate by a dash.
    else:
        song_name = data.split("-")
        if len(song_name) == 2:
            song_name = song_name[0].title()
            data = data.replace(song_name + "-", "")

    # Check if the length of song_name is greater than 1.
    if type(song_name) is list and len(song_name) > 1:
        print(f"{song_name} is labeled wrong.") 
    else:
        print("Can't find song name.")
        
        

    # Separate the patterns from the certainty.
    certainty = data.split("|")
    if len(certainty) == 2:
        certainty = certainty[1]
        # Remove the certainty from the data.
        data = data.replace("|" + certainty, "")
    else:
        print(f"Can't find certainty. of {song_name}")
        exit()



    # Separate the patterns from the data.
    patterns = data.split(",")
    for i in range(len(patterns)):
        # Remove white space from the beginning of the string.
        patterns[i] = patterns[i].lstrip()
        # Remove any periods from the string.
        patterns[i] = patterns[i].replace(".", "")
    if len(patterns) > 0:
        for i in range(len(patterns)):
            pattern = patterns[i]
            # Checks if any known patterns are in the data.
            for known_pattern in known_patterns:
                # Make sure the pattern is in lowercase.
                pattern = pattern.lower()
                if known_pattern in pattern:
                    # Make sure the pattern is in lowercase.
                    pattern = pattern.lower()

                    # Remove any words not in the known patterns or known mispellings lists.
                    temp = pattern.split(" ")
                    for word in temp:
                        # Make sure everything is checked in lowercase.
                        word = word.lower()
                        if word not in known_patterns and word not in Nths:
                            pattern = pattern.replace(word, "")
                            # Remove any extra white space.
                            pattern = pattern.strip()
                    # Add dashes between the words.
                    pattern = pattern.replace(" ", "-")
                    # Remove the first dash.
                    pattern = pattern.replace("-", " ", 1)
                    # Make sure the pattern is capitalized.
                    patterns[i] = pattern.replace(known_pattern, known_pattern.title())

                    break

        # Download the Google Sheet as a CSV.
        # # Clicks the Chrome.png image.
        # CHROME = pyautogui.locateOnScreen('Chrome.png')
        # pyautogui.click(CHROME)
        # time.sleep(.5)

        # # Clicks the "Tab" button.
        # TAB = pyautogui.locateOnScreen('Tab.png')
        # pyautogui.click(TAB)
        # time.sleep(.5)

        # # Clicks the "File" button.
        # FILE = pyautogui.locateOnScreen('File.png')
        # pyautogui.click(FILE)
        # time.sleep(.5)

        # # Clicks the "Download" button.
        # DOWNLOAD = pyautogui.locateOnScreen('Download.png')
        # pyautogui.click(DOWNLOAD)
        # time.sleep(.5)

        # # Clicks the "csv" button.
        # CSV = pyautogui.locateOnScreen('csv.png')
        # pyautogui.click(CSV)
        # time.sleep(.5)

        # Read the CSV file with pandas.
        directory = r'C:\Users\Raptor\Downloads\PLP - PLP - S1.csv'
        # Create a loop that will run until the file is found.
        loop = True
        while loop:
            try:
                df = pd.read_csv(directory)
                loop = False
            except FileNotFoundError:
                print("File not found.")
            
        final = [song_name[0]]

        if len(patterns) < 5:
            temp = 5 - len(patterns)
            for i in range(temp):
                patterns.append(None)
        if len(patterns) > 5:
            # Remove the extra patterns.
            patterns = patterns[:5]

        for pattern in patterns:
            final.append(pattern)

        final.append(username)
        final.append(certainty)

        labels_list.append(final)
        print(df)

for i in range(len(labels_list)):
    df.loc[len(df)] = labels_list[i]
    print(df)
# Replace the CSV file with the new dataframe.
df.to_csv(directory, index=False) 

    




