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

known_patterns = {"mini-jacks": "Mini-Jacks", "jump-jacks": "Jump-Jacks", "split-jump-jacks": "Split-Jump-Jacks", "hand-jacks": "Hand-Jacks", "anchors": "Anchors", "running-men": "Running-Men", "polyrhythms": "Polyrhythms", "jump-streams": "Jump-Streams", 'hand-streams': 'Hand-Streams', 'bursts': 'Bursts', 'trills': 'Trills', 'jump-trills': 'Jump-Trills', 'split-jump-trills': 'Split-Jump-Trills', 'one-hand-trills': 'One-Hand-Trills', 'rolls': 'Rolls', 'split-rolls': 'Split-Rolls', 'jump-gluts': 'Jump-Gluts', 'flams': 'Flams', "mini jacks": "Mini-Jacks", "jump jacks": "Jump-Jacks", "split jump jacks": "Split-Jump-Jacks", "hand jacks": "Hand-Jacks", "poly rhythms": "Polyrhythms", "jump streams": "Jump-Streams", "hand streams": "Hand-Streams", "streams": "Streams", "jumptrills": "Jump-Trills", "jump trills": "Jump-Trills", "split jumptrills": "Split-Jump-Trills", "one hand trills": "One-Hand-Trills", "split rolls": "Split-Rolls", "jump gluts": "Jump-Gluts", "minijacks": "Mini-Jacks", "mini-jacks": "Mini-Jacks", "jumpjacks": "Jump-Jacks", "jump jacks": "Jump-Jacks", "split jumpjacks": "Split-Jump-Jacks", "handjacks": "Hand-Jacks", "chordjacks": "Hand-Jacks", "chord-jacks": "Hand-Jacks", "chord jacks": "Hand-Jacks","jacks": "Jacks", "jack": "Jacks", "runningmen": "Running-Men", "running men": "Running-Men", "grace": "Flams", "irregular": "Irregular", "jumpstreams": "Jump-Streams", "stream": "Streams", "jump-stream": "Jump-Streams", "hand-stream": "Hand-Streams", "jump-trill": "Jump-Trills", "split-jump-trill": "Split-Jump-Trills", "gallops": "Gallops", "triplets": "Triplets"}

labels_list = []

# Nths = ["64th", "48th", "32nd", "24th", "16th", "12th", "8th", "4th"]
# Na = ["64ths", "48ths", "32nds", "24ths", "16ths", "12ths", "8ths", "4ths"]

# Reverse the order of Nths and Na.
Nths = ["4th", "8th", "12th", "16th", "24th", "32nd", "48th", "64th"]
Na = ["4ths", "8ths", "12ths", "16ths", "24ths", "32nds", "48ths", "64ths"]

username = "Psychotik"
labels = """

Starchaser: 16th Jacks, 16th Mini-Jacks, 8th Jump-Streams | Certain
Boy & Bear: 16th Mini-Jacks, 16th Bursts, 8th Jump-Streams | Certain
The Great Pumpkin Tapes: 48th Bursts, 48th Rolls, Irregular Flams, 24th Gallops | Certain
Christmas Ain't The Same: Broken 16th Jump-Streams, 8th Anchors | Certain
Jingle Bells (Bass): 32nd Rolls, 8th Jump-Stream, 8th Jump-Jacks, 12th Mini-Jacks, 12th Gallops | Certain
Fake Santa: 12th Hand-Stream, 12th/24th Gallops, 12th Jump-Streams, 12th Jump-Trills, 12th/24th Stream, 12th Split-Rolls | Certain
Final Boss: 16th Jacks, 16th Jump-Jacks, 32nd Rolls, 16th Jump-Trills, 16th Jump-Gluts, 24th Mini-Trills | Certain
POP/STARS: Irregular Bursts, 8th Jump-Gluts, 8th Anchors, 32nd Rolls, 16th Jump-Jacks | Certain
Ricochet: 24th Gallops, 24th Jump-Streams, 48th Flams, 8th/12th Polyrhythms | Certain
Make Eggs, Eat Eggs: 24th Bursts, 64th Gallops, 32nd Flams, 16th Mini-Jacks | Certain
hARPIES15HP: 16th/32nd One-Hand-Trills, 16th Jump-Streams, 32nd Trills, 8th Jump-Jacks, Irregular Rolls, 16th Mini-Jacks | Certain
Silly Videogame Bleep Bloops: 32nd Rolls, 32nd Split-Rolls, 32nd Trills, 16th Mini-Jacks, 24th Gallops | Certain
Dracula Man X2 Alpha Turbo: 24th Stream, 16th Jump-Streams, 16th Mini-Jacks, 24th Trills, 24th Jump-Trill | Certain
SAIKOU: 32nd Bursts, 16th Jump-Streams, 16th Mini-Jacks, 12th/24th Gallops, 24th Stream | Certain
TURBO [Tokyo Machine] [Standard]: 16th Stream, 24th Bursts, 16th Trills | Certain
Oedo Hop: 24th Gallops, 24th Bursts, 12th Jacks | Certain
Hornet: 24th Streams, Irregular Bursts, 12th Jump-Gluts, 12th Jump-Jacks, 24th Anchors, 16th Jump-Streams | Certain
Twilight: 16th Stream, 8th Jump-Jacks, 16th Mini-Jack | Certain
Opia: Broken 16th Jump-Streams, 16th/24th Polyrhythms, 64th Flams | Certain
Brostep Strikes Back: 12th/16th Mini-Jacks, 16th Jump-Trills, 16th Streams | Certain
Blackmagik Blazing: 16th Split-Jump-Trills, 24th Bursts, 8th/16th Jump-Gluts, 32nd Hand-Streams, 8th/12th Chord-Jacks, 16th jump-Trills, 32nd/64th Rolls | Certain
Morning Run: 16th/32nd Stream, 64th/96th Flams, 16th Mini-Jacks | Certain
Lawn Wake III: Irregular Bursts, Broken 16th Jump-Stream, 16th Mini-Jacks, 16th Jump-Jacks, Irregular Rolls | Certain
Fett's Vette v2: Broken 16th Jump-Streams, 16th Mini-Jacks, Irregular Bursts | Certain
Right Now BLUE Ver.: 24th Gallops, 16th Mini-Jacks, Broken 16th Jump-Stream, 24th Bursts | Certain
Platforms & Pitfalls: 8th Jump-Streams, 16th Bursts | Certain
Smoked Turkey Rag: 16th Jump-Stream, 16th Mini-Jacks, 16th Jump-Trills | Certain
Audio Avenue: Broken 16th Jump-Stream, 16th Mini-Jacks, 16th Stream | Certain
One Look: Broken 16th Streams, Broken 8th Jump-Streams | Certain
Running in the 90's: Broken 8th/16th Jump-Streams, 16th Trills, 12th Gallops, 12th Mini-Jacks | Certain
Flight of the Bumble Bee [MonstDeath]: 16th Split-Jump-Trills, 16th Jump-Streams, 16th Anchors, 16th Jump-Trills | Certain
Kreutzer: 32nd Rolls, 24th Stream, 16th Jump-Stream, 16th Hand-Stream, 16th Mini-Jacks, 8th Jump-Gluts, 16th Anchors | Certain
hatsu miku time: 8th/16th Jump-Jacks, 8th/16th Jacks, 32nd Bursts, 16th Stream | Certain
Roundtable Rival: 24th Stream, 24th Bursts, Broken 16th Jump-Streams, 16th Mini-Jacks | Certain
life flashes before weeb eyes: Broken 16th Jump-Streams, 16th Split-Jump-Trills, 16th Mini-Jacks, Irregular Bursts, Irregular Rolls | Certain
Ordine: Irregular Trills, 24th/48th Bursts, 16th Mini-Jacks, 16th/24th Polyrhythms | Certain
Synth Synth Synth: 12th Jump-Streams, 12th Gallops, 12th One-Hand-Trills | Certain
Live at the Sandopolis: Irregular 24th Stream, 32nd Bursts, 16th Jump-Jacks, 16th Mini-Jacks, 16th/24th Polyrhythms | Certain
Dawgs In Da House: 24th Stream, 16th Jump-Stream, 16th One-Hand-Trill | Certain
JINGLE BELLS: 64th Gallops, 8th Jump-Gluts, 16th Bursts | Certain
Bad Apple!!: 24th Stream, 16th Jump-Stream, 12th Jump-Jacks, 24th/32nd Bursts | Certain
Blend W: 16th Jump-Streams, 24th/32nd Bursts, 16th Mini-Jacks | Certain
Crab Rave: Broken 16th Jump-Stream, 16th Trills | Certain
Kababies: Irregular Rolls, 24th/16th Jump-Streams, 32nd Bursts, 16th Mini-Jacks, 16th Jump-Trills | Certain
BUBBLES: 32nd/24th Bursts, 24th Stream, 16th Mini-Jacks, 16th Jump-Stream | Certain
PYROMANIA: 24th/32nd Bursts, 16th Jump-Streams, 16th Mini-Jacks, 8th Chord-Jacks, 64th Roll | Certain
A Tiny Spaceship's Final Mission: Broken 16th Jump-Streams, 24th Rolls, 24th Bursts | Certain
Last Summer: 16th Jump-Stream, 16th Stream, 32nd Bursts, 16th Mini-Jacks | Certain
UR+ MusicEater LV99: 16th/12th Jump-Jacks, 32nd/24th Bursts, 16th Jump-Streams, 16th Mini-Jacks, 48th Stream | Certain
CO5M1C R4ILR0AD: 8th/12th Polyrhythms, 24th/16th Jump-Stream, 32nd Rolls, 12th Jump-Gluts | Certain
Kadinchey: Broken 16th Jump-Stream, 16th Trill, 8th Anchors, 8th Jump-Gluts | Certain
Micro Media Broth: 16th/24th Polyrhythms, 16th Jump-Gluts, 32nd/24th Bursts, 16th Mini-Jacks, 16th Jump-Stream | Certain
Apocaliptix: 24th Streams, 16th Jump-Streams, 16th Jump-Trills, 24th Bursts | Certain
Mario Overworld (Super Mario Remix): 24th Gallops, 24th Bursts, 8th/12th Polyrhythms | Certain
ROCK IT: 64th Gallops, 32nd Bursts, Broken 16th Jump-Streams, 64th Flams | Certain
Invenzione No. 3N&3R: Sonatina for a Dying Lord: 24th Bursts, Broken 16th/12th Jump-Streams, 16th/24th Polyrhythms | Certain

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

    




