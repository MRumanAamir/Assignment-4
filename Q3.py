def areacalculator(pi:float, radius:float):
    area: float= pi * radius**2;
    return area;


pi =  float( input (" Enter the value of pi: "));

radius= float( input (" Enter the radius: "));



print(" Area of circle is: " ,areacalculator(pi, radius));