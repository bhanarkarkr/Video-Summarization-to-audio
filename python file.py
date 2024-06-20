import random
import pandas as pd

# Generate synthetic data for 1000 rows
data = {
    'Motor1_Speed': [random.randint(1000, 2000) for _ in range(1000)],  # Speed of motor 1 (PWM signal)
    'Motor2_Speed': [random.randint(1000, 2000) for _ in range(1000)],  # Speed of motor 2 (PWM signal)
    'Motor3_Speed': [random.randint(1000, 2000) for _ in range(1000)],  # Speed of motor 3 (PWM signal)
    'Motor4_Speed': [random.randint(1000, 2000) for _ in range(1000)],  # Speed of motor 4 (PWM signal)
    'Acceleration_X': [random.uniform(-10, 10) for _ in range(1000)],  # Acceleration along X-axis (m/s^2)
    'Acceleration_Y': [random.uniform(-10, 10) for _ in range(1000)],  # Acceleration along Y-axis (m/s^2)
    'Acceleration_Z': [random.uniform(-10, 10) for _ in range(1000)],  # Acceleration along Z-axis (m/s^2)
    'Gyroscope_X': [random.uniform(-200, 200) for _ in range(1000)],  # Angular velocity around X-axis (deg/s)
    'Gyroscope_Y': [random.uniform(-200, 200) for _ in range(1000)],  # Angular velocity around Y-axis (deg/s)
    'Gyroscope_Z': [random.uniform(-200, 200) for _ in range(1000)]   # Angular velocity around Z-axis (deg/s)
}

# Create DataFrame
df = pd.DataFrame(data)
csv_file_path = 'D:/drone_dataset.csv'

# Save DataFrame to CSV file
df.to_csv('csv_file_path', index=False)

print("Dataset saved successfully.")