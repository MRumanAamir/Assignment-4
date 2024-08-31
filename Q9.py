def volumecalculator(pi: float, radius: float, height: float):
    volume: float= pi * radius**2 * height ;
    return volume;

pi =  float( input (" Enter the value of pi: "));

radius= float( input (" Enter the value of radius: "));

height= float(input ("Enter the value of height: "));



print(" volume of cylinder : " ,volumecalculator(pi, radius,height)); 