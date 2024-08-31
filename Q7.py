def pctclaculator(numerator: float, denominator: float)-> float:
    pct :float= (numerator / denominator) * 100
    return pct

numerator =  float(input(" Enter the value of numerator: "));

denominator = float(input(" Enter the value of denominator: "));



print("percentage: " ,pctclaculator(numerator,denominator), "%");