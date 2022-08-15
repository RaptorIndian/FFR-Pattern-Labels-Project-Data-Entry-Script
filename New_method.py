import numpy as np
import csv

PATH_TO_GOOGLE_FORM_OUTPUT = './Song_Label_Submission_Form.csv'
PREPROCESSED_OUTPUT_PATH = './PLP - PLP - S1.csv'

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