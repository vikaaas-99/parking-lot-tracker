from colorama import Fore, Style


class ParkingLot:
    def __init__(self, spaces_per_level=20):
        self.levels = {"A": [False] * spaces_per_level, "B": [False] * spaces_per_level}
        self.vehicle_to_spot = {}

    def park_vehicle(self, vehicle_number):
        for level, spots in self.levels.items():
            if level == "A":
                for spot_num, occupied in enumerate(spots):
                    if not occupied:
                        self.levels[level][spot_num] = True
                        self.vehicle_to_spot[vehicle_number] = {"level": level, "spot": spot_num + 1}
                        return {"level": level, "spot": spot_num + 1}
            elif level == "B":
                for spot_num, occupied in enumerate(spots):
                    if not occupied:
                        self.levels[level][spot_num] = True
                        self.vehicle_to_spot[vehicle_number] = {"level": level, "spot": spot_num + 1}
                        return {"level": level, "spot": spot_num + 21}
        return "Parking is full"

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_to_spot:
            return self.vehicle_to_spot[vehicle_number]
        else:
            return "Vehicle not found in the parking lot"


def main():
    parking_lot = ParkingLot()

    while True:
        print("\nChoose an operation:")
        print("1. Park a new vehicle")
        print("2. Retrieve parking spot for a vehicle")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.park_vehicle(vehicle_number)
            if result == "Parking is full":
                print(Fore.RED + "Parking is full. Cannot park the vehicle.")
            else:
                print(Fore.GREEN + f"Parked at Level: {result['level']}, Spot: {result['spot']}")
            print(Style.RESET_ALL)

        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            spot_info = parking_lot.retrieve_parking_spot(vehicle_number)
            if type(spot_info) == str:
                print(Fore.RED + "Vehicle not found in the parking lot.")
            else:
                print(Fore.YELLOW + f"Level: {spot_info['level']}, Spot: {spot_info['spot']}")
            print(Style.RESET_ALL)

        elif choice == "3":
            print("Exiting the parking lot application.")
            break

        else:
            print("Invalid choice. Please choose a valid option (1/2/3).")

if __name__ == "__main__":
    main()
