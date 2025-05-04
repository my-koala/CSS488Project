import pandas as pd
import json

# Load the JSON file
with open('reddit_jokes.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter rows with score >= 10
filtered_df = df[df['score'] >= 100]

# Save to a new JSON file
filtered_df.to_json('filtered_output.json', orient='records', indent=4)

print(len(data))
print(len(filtered_df))