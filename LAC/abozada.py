import pandas as pd
import re

def clean_username(username):
    # Replace the first "-" with "."
    first_dash_index = username.find("-")
    if first_dash_index != -1:
        username = username[:first_dash_index] + "." + username[first_dash_index+1:]

    # Remove digits before "@"
    username = process_email(username)

    # Replace everything after "@" with "elitelac.com"
    username = username.split("@")[0] + "@elitelac.com"

    return username

# Function to remove digits before '@' in email
def process_email(email):
    return re.sub(r'\d+(?=@)', '', email)

# Read the CSV file
df = pd.read_csv("cleaned_file.csv")

# Apply the cleaning function to the "Username" column
df["Username"] = df["Username"].apply(clean_username)

# Save the modified DataFrame to a new CSV file
df.to_csv("cleaned_file.csv", index=False)