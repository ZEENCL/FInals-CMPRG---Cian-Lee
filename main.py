# Importing from packages
from vehicles import Vehicle, SchoolBus
from employees import Employee
from schools import SchoolOne, SchoolTwo
from vectors import Vector
from library import Book, Author

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
        {"name": "Ed", "grades": [49, 54, 63], "gpa": 1.00},
        {"name": "Edd", "grades": [52, 69, 64], "gpa": 1.25},
        {"name": "Eddy", "grades": [32, 76, 58], "gpa": 1.00}
    ]

    students_two = [
        {"name": "Dee Dee", "grades": [75, 83, 79], "gpa": 2.75},
        {"name": "Marky", "grades": [85, 87, 81], "gpa": 3.00},
        {"name": "Joey", "grades": [96, 61, 84], "gpa": 2.75}
    ]

    school1 = SchoolOne(students_one)
    school1.get_grades()

    print()

    school2 = SchoolTwo(students_two)
    school2.get_grades()

    # --- Vectors Adding (Dunder Method) ---
    print("\n---\n")

    vector1 = Vector(1, 2)
    vector2 = Vector(3, 4)

    result = vector1 + vector2

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print()
    print("Result of addition:", result)

    # --- Book & Author (Composition) ---
    print("\n---\n")

    author = Author(f"Sev Torreon", "Filipino", "Loves Cian Lee very much.")
    book = Book("I Like Cian Lee", "Romance Comedy", author)

    print(book.get_info())

    # --- End ---

    print("\n---")

if __name__ == "__main__":
    main()