from sre_constants import SRE_INFO_PREFIX
import numpy as np
import csv
import pandas as pd

PATH_TO_GOOGLE_FORM_OUTPUT = r'C:\Users\Raptor\Downloads\Song Label Submission Form.csv'
PREPROCESSED_OUTPUT_PATH = './Temp.csv'
SPREADSHEET = r'C:\Users\Raptor\Downloads\PLP - PLP - S1.csv'

# Convert the spreadsheet to a pandas dataframe.
spreadsheet_df = pd.read_csv(SPREADSHEET)

with open(PATH_TO_GOOGLE_FORM_OUTPUT, newline='') as csvfile:
    with open(PREPROCESSED_OUTPUT_PATH, 'w') as finalfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvwriter = csv.writer(finalfile, delimiter=',')
        for i, row in enumerate(csvreader):
            if not i:
                index = {v : k for k, v in enumerate(row)}
                csvwriter.writerow([
                    'Song name',
                    'Patterns',
                    'Patterns.1',
                    'Patterns.2',
                    'Patterns.3',
                    'Patterns.4',
                    'Labeler',
                    'Accuracy'
                ])
            else:
                song_name = row[index['Song Name exactly as it is in FFR:']]

                # If the song name is in the spreadsheet already, then skip the iteration.
                if song_name in spreadsheet_df['Song name'].values:
                    continue

                labeler_name = row[index['Your FFR username:']]
                accuracy = row[index['Confidence in the accuracy of the patterns and difficulty listed above:']]
                content = [song_name]

                for pattern, quantization in np.array(row[3:-1]).reshape(-1, 2):
                    quantization = quantization.split(' ')[0]
                    processed_pattern = ' '.join([quantization, pattern])
                    content.append(processed_pattern)

                content.append(labeler_name)
                content.append(accuracy)
                csvwriter.writerow(content)
            

# Convert Temp.csv to a pandas dataframe.
temp_df = pd.read_csv(PREPROCESSED_OUTPUT_PATH)

# Return rows that have duplicate song names.
duplicate_rows = temp_df[temp_df['Song name'].duplicated()]

# Only keep the first row with a duplicate song name.
temp_df = temp_df[~temp_df['Song name'].duplicated()]

# Append the temp dataframe to the end of the spreadsheet dataframe.
spreadsheet_df = spreadsheet_df.append(temp_df)

# Replace the spreadsheet with the new dataframe.
spreadsheet_df.to_csv(SPREADSHEET, index=False)

# Print the user names who contributed to the spreadsheet and the number of songs they labeled.
print(spreadsheet_df['Labeler'].value_counts())