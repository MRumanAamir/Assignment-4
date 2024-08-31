def areacalculator(lenght:int, widht:int):
    area: int= lenght * widht;
    return area;

    
lenght =  int( input (" Enter the lenght: "));

widht= int( input (" Enter the width: "));


print(" Area of rectangle is: " ,areacalculator(lenght, widht));