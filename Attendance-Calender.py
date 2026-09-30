print("===== ATTENDANCE CALENDAR =====")
name=input("Add Student Name:")
month = input("Enter month name: ")
days = int(input("Enter number of days in the month: "))

attendance = []

for day in range(1, days + 1):
    status = input(f"Day {day} - Present (P) / Absent (A): ").upper()

    if status == "P":
        attendance.append("Present")
    else:
        attendance.append("Absent")

print("\n===== ATTENDANCE CALENDAR =====")
print("Month:", month)

for day in range(1, days + 1):
    print(f"Day {day}: {attendance[day - 1]}")

present = attendance.count("Present")
absent = attendance.count("Absent")

percentage = (present / days) * 100

print("\n===== ATTENDANCE REPORT =====")
print("name:",name)
print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(percentage, 2), "%")

if percentage >= 75:
    print("Status: Eligible")
else:
    print("Status: Short Attendance")