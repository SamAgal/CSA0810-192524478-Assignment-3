"""Task 4: Sets: Elective Registration Clash Detection."""

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

if __name__ == "__main__":
    # Using set operators
    clash = ai_elective & iot_elective
    exactly_one = ai_elective ^ iot_elective
    neither = all_students - (ai_elective | iot_elective)
    
    print("clash :", sorted(clash))
    print("exactly one:", sorted(exactly_one))
    print("neither :", sorted(neither))
