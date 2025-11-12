import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import sqlite3

# Generate raw data with NumPy
num_events = 200
num_cars = 100

# car_id: Repeat 1-100 twice (each car has 2 events)
car_ids = np.repeat(np.arange(1, num_cars + 1), 2)

# event_id: Squential 1 to 200
event_ids = np.arange(1, num_events + 1)

# speed mph: Random floats between 40 and 70
speed_mph = np.random.uniform(40, 70, num_events)

# distance_miles: Random floats between 0.5 and 3
distance_miles = np.random.uniform(0.5, 3, num_events)

# Structure as DataFrame with Pandas
fleet_data = pd.DataFrame({
    'car_id': car_ids,
    'event_ids': event_ids,
    'speed_mph': speed_mph,
    'distance_miles': distance_miles
})

# Group by car_id
grouped = fleet_data.groupby('car_id')

# Compute aggregate metrics
summary = grouped.agg({
    'distance_miles': 'sum',  # Total distance per car
    'speed_mph': 'mean',  # Average speed per car
    'event_ids': 'count'  # Number of events per car
}).round(2)  # Round for readability

# Rename columns for clarity
summary.columns = ['total_distance', 'avg_speed', 'num_events']

# Add performance flag
summary['performance_flag'] = summary['avg_speed'].apply(
    lambda x: 'High' if x > 60 else 'Standard'
    )

# -------------------------------
# 3. Load Into SQLite Database
# -------------------------------
conn = sqlite3.connect('fleet.db')

# Write tables
fleet_data.to_sql('events_raw', conn, if_exists='replace', index=False)
summary.to_sql('car_metrics', conn, if_exists='replace', index=True)

# -------------------------------
# 4. SQL Queries
# -------------------------------
query_top_distance = """
SELECT car_id, total_distance
FROM car_metrics
ORDER BY total_distance DESC
LIMIT 1;
"""

query_top_speed = """
SELECT car_id, avg_speed
FROM car_metrics
ORDER BY avg_speed DESC
LIMIT 1;
"""

query_high_perf = """
SELECT COUNT(*)
FROM car_metrics
WHERE performance_flag = 'High';
"""

top_distance = pd.read_sql(query_top_distance, conn)
top_speed = pd.read_sql(query_top_speed, conn)
high_perf_count = pd.read_sql(query_high_perf, conn)

# -------------------------------
# 5. Print Insights
# -------------------------------
print("\n===== ETL Summary Insights =====")
print(f"Car with the highest total distance:\n{top_distance}\n")
print(f"Car with the highest average speed:\n{top_speed}\n")
print(f"Number of high-performance cars: {high_perf_count.iloc[0, 0]}\n")

# -------------------------------
# 6. Visualization
# -------------------------------
summary['total_distance'].plot(kind='bar', figsize=(12, 6))
mp.title("Total Distance Per Car")
mp.xlabel("Car ID")
mp.ylabel("Miles Driven")
mp.tight_layout()
mp.show()

