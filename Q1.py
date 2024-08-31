def calculateAge(currentYear:int, birthYear:int):
    age : int = currentYear - birthYear;
    return age;



currentYear =  int(input(" Enter the current year: "));
birthYear = int(input(" Enter your birth year: "));



print("Your age is" ,calculateAge(currentYear, birthYear));

