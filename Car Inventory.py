class Car:    def __init__(self, make, model, color, year, mileage):        self.__make = make        self.__model = model        self.__color = color        self.__year = year        self.__mileage = mileage    def __str__(self):        return f"{self.__year} {self.__make} {self.__model} ({self.__color}) - {self.__mileage} miles"    def get_make(self):        return self.__make    def get_model(self):        return self.__model    def get_color(self):        return self.__color    def get_year(self):        return self.__year    def get_mileage(self):        return self.__mileageclass CarInventory:    def __init__(self):        self.__inventory = []    def add_car(self, car):        self.__inventory.append(car)        print(f"Added: {car}")    def remove_car(self, make, model, color, year):        for car in self.__inventory:            if car.get_make() == make and car.get_model() == model and car.get_color() == color and car.get_year() == year:                self.__inventory.remove(car)                print(f"Removed: {car}")                return        print("Car not found in inventory.")    def display_inventory(self):        if not self.__inventory:            print("Inventory is empty.")            return        print("Current Inventory:")        for car in self.__inventory:            print(car)def main():    inventory = CarInventory()    while True:        print("\nCar Inventory Management")        print("1. Add Car")        print("2. Remove Car")        print("3. Display Inventory")        print("4. Exit")        choice = input("Choose an option: ")        if choice == '1':            make = input("Enter make: ")            model = input("Enter model: ")            color = input("Enter color: ")            year = int(input("Enter year: "))            mileage = int(input("Enter mileage: "))            new_car = Car(make, model, color, year, mileage)            inventory.add_car(new_car)        elif choice == '2':            make = input("Enter make of the car to remove: ")            model = input("Enter model of the car to remove: ")            color = input("Enter color of the car to remove: ")            year = int(input("Enter year of the car to remove: "))            inventory.remove_car(make, model, color, year)        elif choice == '3':            inventory.display_inventory()        elif choice == '4':            print("Exiting program.")            break        else:            print("Invalid option. Please try again.")if __name__ == "__main__":    main()