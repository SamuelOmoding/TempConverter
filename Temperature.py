def temperature_converter():
    print("\nTemperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter your choice (1-6): ")
    
    if not choice.isdigit(): 
        print("Invalid choice. Please enter a number between 1 and 6.")
        return
    choice = int(choice)
    if choice < 1 or choice > 6:
        print("Invalid choice. Please enter a number between 1 and 6.")
        return
    
    temp_input = input("Enter the temperature: ")
    
    if not temp_input.replace(',', ' ').isdigit():
        print("Invalid temperature. Please enter a valid number.")
        return
    
    temp = float(temp_input)
    choice = int(choice)
    
    if choice == 1:
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp:.2f}°C.")
    elif choice == 2:
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp:.2f}°F.")
    elif choice == 3:
        converted_temp = temp + 273.15
        print(f"{temp}°C is equal to {converted_temp:.2f}°K.")
    elif choice == 4:
        converted_temp = temp - 273.15
        print(f"{temp}°K is equal to {converted_temp:.2f}°C.")
    elif choice == 5:
        celsius = (temp - 32) *5/9
        converted_temp = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is equal to {converted_temp:.2f}°K.")
    elif choice == 6:
        celsius = temp - 273.15
        converted_temp = (celsius * 9/5) + 32
        print(f"{temp}°K is equal to {converted_temp:.2f}°F.")
        
# Run the converter
temperature_converter()        