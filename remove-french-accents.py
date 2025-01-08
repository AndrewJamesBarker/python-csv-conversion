import os
from unidecode import unidecode

source_dir = '/Users/andrewbarker/tba-d10-v2-files/pdf'
# remove accentsa from file names
for entry in os.listdir(source_dir):
    full_path = os.path.join(source_dir, entry)
    if os.path.isfile(full_path):
        os.rename(os.path.join(source_dir, entry), os.path.join(source_dir, entry.replace('é', 'e')))
        print(entry)

# Input text data (replace this with your actual data)
