# Importing from packages
from vehicles import Vehicle, SchoolBus
from employees import Employee
from schools.school_one import SchoolOne
from schools.school_two import SchoolTwo

def main():
    # --- Vehicles (Inheritance & Polymorphism) ---
    car = Vehicle("Sedan", "Toyota", "Corola")
    bus = SchoolBus("Bus", "Bluebird", "Vision", 60)

    print(car.get_info())
    print()
    car.drive()
    car.stop()

    print()

    print(bus.get_info())
    print()
    bus.drive()
    print(f"Bus capacity: {bus.get_capacity()}")
    bus.stop()
    print(f"Bus capacity: {bus.get_capacity() - bus.get_capacity()}")

    # --- Employees (Class Method) ---
    print("\n---\n")

    employee1 = Employee("Spongebob", 38)
    employee2 = Employee.from_string("Squidward-55")

    print(employee1)
    print(employee2)

    # --- Schools & Students' GPA ---
    print("\n---\n")

    students_one = [
        {"name": "Ed", "grades": [49, 54, 63], "gpa": 1},
        {"name": "Edd", "grades": [52, 69, 64], "gpa": 1.25},
        {"name": "Eddy", "grades": [32, 76, 58], "gpa": 1}
    ]

    students_two = [
        {"name": "Ed", "grades": [49, 54, 63], "gpa": 1},
        {"name": "Edd", "grades": [52, 69, 64], "gpa": 1.25},
        {"name": "Eddy", "grades": [32, 76, 58], "gpa": 1}
    ]

    school1 = SchoolOne(students_one)
    school1.get_grades()

    

if __name__ == "__main__":
    main()