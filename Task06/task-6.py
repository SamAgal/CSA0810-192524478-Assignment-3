"""Task 6: Nested Data: A Railway Timetable."""

if __name__ == "__main__":
    timetable = {
        "Chennai Express": {"Departure": "06:00", "Arrival": "12:30", "Stops": ["Tambaram", "Villupuram", "Trichy"]},
        "Pandian Express": {"Departure": "21:05", "Arrival": "05:00", "Stops": ["Tambaram", "Madurai"]}
    }
    
    print("Railway Timetable Database Loaded successfully.")
    for train, info in timetable.items():
        print(f"Train: {train} | Dep: {info['Departure']} | Stops: {len(info['Stops'])}")
