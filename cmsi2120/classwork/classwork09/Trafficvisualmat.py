import pandas as pd
import matplotlib.pyplot as plt

class TrafficNode:
    def __init__(self, date, time, location, vehicle_count, speed, travel_time):
        self.date = date
        self.time = time
        self.location = location
        self.vehicle_count = vehicle_count
        self.speed = speed
        self.travel_time = travel_time
        self.next = None

class TrafficLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, date, time, location, vehicle_count, speed, travel_time):
        new_node = TrafficNode(date, time, location, vehicle_count, speed, travel_time)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, date, time, location):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.date == date and current_node.time == time and current_node.location == location:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def search_node(self, date, time, location):
        current_node = self.head
        while current_node:
            if current_node.date == date and current_node.time == time and current_node.location == location:
                return current_node
            current_node = current_node.next
        return None

    def calculate_average_speed(self):
        total_speed = 0
        count = 0
        current_node = self.head
        while current_node:
            total_speed += current_node.speed
            count += 1
            current_node = current_node.next
        if count > 0:
            return total_speed / count
        else:
            return None

# Prompt the user to enter the CSV file name
filename = input("Enter the CSV file name: ")

# Read the CSV file and add nodes to the linked list
df = pd.read_csv(filename)
linked_list = TrafficLinkedList()
for index, row in df.iterrows():
    date = row['date']
    time = row['time']
    location = row['location']
    vehicle_count = int(row['vehicle_count'])
    speed = float(row['speed'])
    travel_time = float(row['travel_time'])
    linked_list.add_node(date, time, location, vehicle_count, speed, travel_time)

# Calculate the average speed and plot the data
average_speed = linked_list.calculate_average_speed()
if average_speed is not None:
    df['speed'].plot()
    plt.axhline(y=average_speed, color='r', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.title('Average Speed of Traffic')
    plt.show()
    print("The average speed is:", average_speed)
else:
    print("No data available.")