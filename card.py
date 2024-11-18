import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
csv_file = '/workspaces/-shiptivitas-3/card_changes.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['cardID'], df['card_changes'], color='blue')

# Formatting the chart
plt.title('Number of Status Changes by Card', fontsize=16)
plt.xlabel('Card ID', fontsize=14)
plt.ylabel('Number of Status Changes', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.tight_layout()

# Show the plot
plt.savefig("card_changes.png") 
