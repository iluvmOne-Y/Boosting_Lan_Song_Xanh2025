import pandas as pd

# Load the CSV file
input_file = 'new_13_pas.csv'
output_file = 'NEW_13_extracted_credentials.txt'

# Read the CSV
df = pd.read_csv(input_file)

# Select Username and Password columns
# Fill missing passwords with an empty string so the script doesn't crash or print 'nan'
df['Password'] = df['Password'].fillna('')

# Open the output file and write lines
with open(output_file, 'w') as f:
    for index, row in df.iterrows():
        username = str(row['Username'])
        password = str(row['Password'])
        # Write formatted string: username space password
        f.write(f"{username} {password}\n")

print(f"Successfully extracted credentials to {output_file}")
