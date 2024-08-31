def bmicalculator(weight: int, height: float):
    bmi: float = weight/ height**2 
    return bmi;


weight =  float( input (" Enter the weight in kg: "));

height= float( input (" Enter the height in meter: "));


print(" BMI: " ,bmicalculator(weight, height));