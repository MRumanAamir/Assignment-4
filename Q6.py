def secondcalculator(seconds: int):
    min = seconds // 60;
    sec = seconds % 60;
    min_sec = f" {min} min {sec} sec ";
    return min_sec

seconds = int(input("Enter the number of seconds: "));



print(secondcalculator(seconds));