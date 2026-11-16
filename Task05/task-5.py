"""Task 5: List Comprehension: Cleaning Sensor Readings."""

if __name__ == "__main__":
    raw_readings = [25.0, -60.0, 55.0, 5.0, 3.5, 52.0, -10.0]
    
    # Valid range: -50 <= temp <= 50
    valid_celsius = [t for t in raw_readings if -50 <= t <= 50]
    valid_fahrenheit = [c * 9/5 + 32 for c in valid_celsius]
    
    # Alarm minutes: outside 2-8 C
    alarm_minutes = [i for i, t in enumerate(raw_readings) if -50 <= t <= 50 and not (2 <= t <= 8)]
    
    print("Valid Celsius:", valid_celsius)
    print("Valid Fahrenheit:", valid_fahrenheit)
    print("Alarm Minutes (indices):", alarm_minutes)
