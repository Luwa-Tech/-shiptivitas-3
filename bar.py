import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
csv_file = 'C:\\Users\\Luwa\Documents\\task3\\daily_active_users.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Separate the data into "Before" and "After" periods
before_data = df[df['period'] == 'Before']
after_data = df[df['period'] == 'After']

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(before_data['date'], before_data['daily_active_users'], label='Before 2018-06-02', color='blue')
plt.plot(after_data['date'], after_data['daily_active_users'], label='After 2018-06-02', color='green')

# Formatting the chart
plt.title('Daily Active Users Before and After 2018-06-02', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Daily Active Users', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()
