import pandas as pd
import pyautogui

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
        exit()

known_patterns = {"mini-jacks": "Mini-Jacks", "jump-jacks": "Jump-Jacks", "split-jump-jacks": "Split-Jump-Jacks", "hand-jacks": "Hand-Jacks", "anchors": "Anchors", "running-men": "Running-Men", "polyrhythms": "Polyrhythms", "jump-streams": "Jump-Streams", 'hand-streams': 'Hand-Streams', 'bursts': 'Bursts', 'trills': 'Trills', 'jump-trills': 'Jump-Trills', 'split-jump-trills': 'Split-Jump-Trills', 'one-hand-trills': 'One-Hand-Trills', 'rolls': 'Rolls', 'split-rolls': 'Split-Rolls', 'jump-gluts': 'Jump-Gluts', 'flams': 'Flams', "mini jacks": "Mini-Jacks", "jump jacks": "Jump-Jacks", "split jump jacks": "Split-Jump-Jacks", "hand jacks": "Hand-Jacks", "poly rhythms": "Polyrhythms", "jump streams": "Jump-Streams", "hand streams": "Hand-Streams", "streams": "Streams", "jumptrills": "Jump-Trills", "jump trills": "Jump-Trills", "split jumptrills": "Split-Jump-Trills", "one hand trills": "One-Hand-Trills", "split rolls": "Split-Rolls", "jump gluts": "Jump-Gluts", "minijacks": "Mini-Jacks", "mini-jacks": "Mini-Jacks", "jumpjacks": "Jump-Jacks", "jump jacks": "Jump-Jacks", "split jumpjacks": "Split-Jump-Jacks", "handjacks": "Hand-Jacks", "chordjacks": "Chord-Jacks", "chord-jacks": "Chord-Jacks", "chord jacks": "Chord-Jacks","jacks": "Jacks", "jack": "Jacks", "runningmen": "Running-Men", "running men": "Running-Men", "grace": "Flams", "irregular": "Irregular", "jumpstreams": "Jump-Streams", "stream": "Streams", "jump-stream": "Jump-Streams", "hand-stream": "Hand-Streams", "jump-trill": "Jump-Trills", "split-jump-trill": "Split-Jump-Trills", "gallops": "Gallops", "triplets": "Triplets", "jump-chains": "Jump-Chains", "jump chains": "Jump-Chains"}

labels_list = []

# Nths = ["64th", "48th", "32nd", "24th", "16th", "12th", "8th", "4th"]
# Na = ["64ths", "48ths", "32nds", "24ths", "16ths", "12ths", "8ths", "4ths"]

# Reverse the order of Nths and Na.
Nths = ["4th", "8th", "12th", "16th", "24th", "32nd", "48th", "64th"]
Na = ["4ths", "8ths", "12ths", "16ths", "24ths", "32nds", "48ths", "64ths"]

username = "sff_writer_dan"
labels = """

Misbehave (In This Cave): 16th Streams, 8th Streams | Certain
Sea of Dreams: 8th Streams, 8th Jump-Streams, 32nd Flams | Certain
pause: 4th Streams | Certain
Secret Zombie Room v2: 8th Streams, 4th Jump-Streams | Certain
Passengers [Beginner]: 4th Streams | Certain
Fastest Pointer-Finger in the West: Irregular Flams | Uncertain

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
        song_name = song_name[0]
        # Remove the song name from the data.
        data = data.replace(song_name + ":", "")

    elif len(song_name) > 2:
        # Combine all but the last item in the list.
        song_name = song_name[0] + ":" + " ".join(song_name[1:-1])
        # Remove the song name from the data.
        data = data.replace(song_name + ":", "")


    # If the song name is not found, try to separate by a dash.
    else:
        song_name = data.split("-")
        if len(song_name) == 2:
            song_name = song_name[0]
            data = data.replace(song_name + "-", "")
        else:
            # Create a variable that is the length of the song_name list - 1.
            song_name_end = len(song_name) - 2
            # Combine the first two elements in the list.
            song_name = song_name[0] + "-" + song_name[song_name_end]
            # Remove the song name from the data.
            data = data.replace(song_name + "-", "")

    # Check if the length of song_name is greater than 1.
    if type(song_name) is list and len(song_name) > 1:
        print(f"{song_name} is labeled wrong.") 

    # Check if the song name is in the dataframe. If it is, then skip the song.
    if song_name in df.values:
        print(song_name)
        break
        

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

                    # Remove any slashes and replace with a space.
                    nth_check = patterns[i].split("/")

                    # If the length of the list is greater than 1, remove the first item.
                    if len(nth_check) > 1:
                        del nth_check[0]
                        pattern = nth_check[0]

                    # Remove any words not in the known patterns or known mispellings lists.
                    temp = pattern.split(" ")
                    for word in temp:
                        # Make sure everything is checked in lowercase.
                        word = word.lower()
                        if word not in known_patterns and word not in Nths:
                            pattern = pattern.replace(word, "")
                        if word in known_patterns:
                            pattern = pattern.replace(word, known_patterns[word])
                        # Remove any extra white space.
                        pattern = pattern.strip()
                    # Make sure the pattern is capitalized.
                    patterns[i] = pattern.replace(known_pattern, known_patterns[known_pattern])

            
                       



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

        # If the song name is a list.
        if type(song_name) is list:
            final = [song_name[0]]
        else:
            final = [song_name]

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


for i in range(len(labels_list)):
    df.loc[len(df)] = labels_list[i]
print(df)
# Replace the CSV file with the new dataframe.
df.to_csv(directory, index=False) 

    




