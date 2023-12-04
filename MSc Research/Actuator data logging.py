import time
import csv

# Example code for data logging
data_log = []

# Simulate actuator movement
for i in range(10):
    # Measure voltage and current
    voltage = measure_voltage()
    current = measure_current()

    # Measure position (if applicable)
    position = measure_position()

    # Measure speed
    speed = calculate_speed()

    # Record data
    data_point = {
        "Time": time.time(),
        "Voltage": voltage,
        "Current": current,
        "Position": position,
        "Speed": speed
    }
    data_log.append(data_point)

    # Pause for a short duration
    time.sleep(1)

# Write data to CSV file
with open('actuator_data.csv', 'w', newline='') as csv_file:
    fieldnames = ["Time", "Voltage", "Current", "Position", "Speed"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_log)
