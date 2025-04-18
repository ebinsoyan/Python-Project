import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample Uber trip data (simulating for 7 days)
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Simulated trip data
num_trips = np.random.randint(200, 600, size=7)               # Total trips per day
avg_duration = np.random.randint(10, 35, size=7)              # Average duration in minutes
avg_distance = np.random.uniform(3, 10, size=7).round(2)      # Average distance in km
num_cancellations = np.random.randint(10, 50, size=7)         # Canceled rides

# Create DataFrame
df = pd.DataFrame({
    'Day': days,
    'Trips': num_trips,
    'Avg_Duration(min)': avg_duration,
    'Avg_Distance(km)': avg_distance,
    'Cancellations': num_cancellations
})

print("Sample Uber Trip Data:\n")
print(df)

# 1. Line Plot - Trips per Day
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Trips'], marker='o', color='purple')
plt.title('Uber Trips per Day')
plt.xlabel('Day')
plt.ylabel('Number of Trips')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Plot - Average Trip Duration
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Avg_Duration(min)'], color='orange')
plt.title('Average Trip Duration per Day')
plt.xlabel('Day')
plt.ylabel('Duration (minutes)')
plt.tight_layout()
plt.show()

# 3. Bar Plot - Average Trip Distance
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Avg_Distance(km)'], color='steelblue')
plt.title('Average Trip Distance per Day')
plt.xlabel('Day')
plt.ylabel('Distance (km)')
plt.tight_layout()
plt.show()

# 4. Line Plot - Cancellations per Day
plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Cancellations'], marker='x', linestyle='--', color='red')
plt.title('Ride Cancellations per Day')
plt.xlabel('Day')
plt.ylabel('Cancellations')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Horizontal Bar Chart - Trip Share by Day
plt.figure(figsize=(10, 6))
plt.bar(df['Day'], df['Trips'], color='mediumseagreen')
plt.title('Trip Share by Day')
plt.xlabel('Number of Trips')
plt.ylabel('Day')
plt.tight_layout()
plt.show()
