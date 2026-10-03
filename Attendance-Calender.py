print("===== ATTENDANCE MANAGEMENT SYSTEM =====")

name = input("Enter Student Name: ")
month = input("Enter Month: ")
days = int(input("Enter Number of Days: "))

attendance = []

for day in range(1, days + 1):

    while True:
        status = input(
            f"Day {day} - Present (P) / Absent (A) / Late (L): "
        ).upper()

        if status == "P":
            attendance.append("Present")
            break

        elif status == "A":
            attendance.append("Absent")
            break

        elif status == "L":
            attendance.append("Late")
            break

        else:
            print("Invalid input! Enter P, A or L.")

present = attendance.count("Present")
absent = attendance.count("Absent")
late = attendance.count("Late")

effective_present = present + (late * 0.5)
percentage = (effective_present / days) * 10

print("\n===== ATTENDANCE CALENDAR =====")
print("Student:", name)
print("Month:", month)

for day in range(1, days + 1):
    print(f"Day {day}: {attendance[day - 1]}")

print("\n===== ATTENDANCE REPORT =====")
print("Student:", name)
print("Present:", present)
print("Absent:", absent)
print("Late:", late)
print("Attendance:", round(percentage, 2), "%")

if percentage >= 75:
    print("Status: Eligible")
else:
    print("Status: Short Attendance")

print("\nThank you for using Attendance Management System!")