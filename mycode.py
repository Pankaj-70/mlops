import pandas as pd
import os

# Sample data
data = {
    'Name': ['Alice', 'John', 'Ben'],
    'Age': [10, 19, 16],
    'City': ['NYC', 'WDC', 'HLD']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create directory if it doesn't exist
dir_name = 'data'
os.makedirs(dir_name, exist_ok=True)

# Save DataFrame to CSV
file_path = os.path.join(dir_name, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
