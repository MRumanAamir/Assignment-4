def fahren_celcalculator(fahrenheit: int):
    celsius: int= (fahrenheit - 32) * 5//9;
    return celsius;


fahrenheit  = int(input("Enter the temperature in fahrenheit: "));


print("\nAfter conversion");
print("Celsius:",fahren_celcalculator(fahrenheit));



def cel_fahrencalculator(celsius: int):
    fahrenheit: int= (celsius * 9/5) + 32;
    return fahrenheit;


celsius = int(input("Enter the temperature in celsius: "));


print("\nAfter conversion");
print("Fahreenheit: ",cel_fahrencalculator(celsius));


