from datetime import datetime

# Weather data for New York City from 1st August 2023 to 10th July 2024

weather_data = [
    {'date': '2023-08-01', 'max_temp': 29, 'min_temp': 21, 'humidity': 65},
    {'date': '2023-08-02', 'max_temp': 30, 'min_temp': 22, 'humidity': 70},
    {'date': '2023-08-03', 'max_temp': 31, 'min_temp': 23, 'humidity': 68},
    {'date': '2023-08-04', 'max_temp': 28, 'min_temp': 20, 'humidity': 75},
    {'date': '2023-08-05', 'max_temp': 27, 'min_temp': 19, 'humidity': 80},
    {'date': '2023-08-06', 'max_temp': 32, 'min_temp': 24, 'humidity': 72},
    {'date': '2023-08-07', 'max_temp': 33, 'min_temp': 25, 'humidity': 78},
    {'date': '2023-08-08', 'max_temp': 34, 'min_temp': 26, 'humidity': 60},
    {'date': '2023-08-09', 'max_temp': 29, 'min_temp': 22, 'humidity': 65},
    {'date': '2023-08-10', 'max_temp': 30, 'min_temp': 21, 'humidity': 66},
]

def find_highest_lowest_temperatures(data):
    """Find the highest and lowest temperatures recorded during the period."""
    highest_temp = max(data, key=lambda x: x['max_temp'])
    lowest_temp = min(data, key=lambda x: x['min_temp'])
    return highest_temp, lowest_temp

def count_days_above_30(data):
    """Determine the number of days with temperatures above 30°C."""
    return sum(1 for day in data if day['max_temp'] > 30)

def compute_average_humidity(data):
    """Compute the average humidity over the specified period."""
    total_humidity = sum(day['humidity'] for day in data)
    return total_humidity / len(data)

# Example usage
if __name__ == "__main__":
    # Finding highest and lowest temperatures
    highest, lowest = find_highest_lowest_temperatures(weather_data)
    print(f"Highest temperature recorded: {highest['max_temp']}°C on {highest['date']}")
    print(f"Lowest temperature recorded: {lowest['min_temp']}°C on {lowest['date']}")

    # Counting days with temperatures above 30°C
    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of days with temperatures above 30°C: {days_above_30}")

    # Computing average humidity
    average_humidity = compute_average_humidity(weather_data)
    print(f"Average humidity over the period: {average_humidity:.2f}%")
