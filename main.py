# Importing from packages
from vehicles import Vehicle, SchoolBus

def main():
    car = Vehicle("Toyota", "Corola")
    bus = SchoolBus("Bluebird", "Vision", 60)

    car.drive()
    car.stop()
    print(car.get_info())

    print()

    bus.drive()
    print(f"Bus capacity: {bus.get_capacity()}")

if __name__ == "__main__":
    main()