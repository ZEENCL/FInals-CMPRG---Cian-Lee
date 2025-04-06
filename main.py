# Importing from packages
from vehicles import Vehicle, SchoolBus

def main():
    car = Vehicle("Sedan", "Toyota", "Corola")
    bus = SchoolBus("Bus", "Bluebird", "Vision", 60)

    print(car.get_info())
    car.drive()
    car.stop()

    print()

    print(bus.get_info())
    bus.drive()
    print(f"Bus capacity: {bus.get_capacity()}")

    bus.stop()
    print(f"Bus capacity: {bus.get_capacity() - bus.get_capacity()}")

if __name__ == "__main__":
    main()