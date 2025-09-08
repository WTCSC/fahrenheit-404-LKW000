print("Weclome to Temperature Converter!")
print("What would you like to convert?")
print("A. Convert Celsius to Fahrenheit")
print("B. Convert Fahrenheit to Celsius")
choice = input("Enter your choice, 1 or 2: ")


if choice =='1':
    Celsius = float(input("enter temperature in celsius: "))
    fahrenheit = (Celsius * 1.8) + 32
    print(f"{Celsius}°C is equal to {fahrenheit}°F")


elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (fahrenheit- 32) * 0.5555
    print(f"{fahrenheit}°F is equal to {Celsius}°C")
else:
    print("Invalid choice. Please run the program again and enter 1 or 2. :(")
    print("Thank you for using the temperaturew converter.")   