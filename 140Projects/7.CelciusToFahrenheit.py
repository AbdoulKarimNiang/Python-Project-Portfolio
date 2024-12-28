celcius = None
def get_celcius(celcius) -> float:
    while not isinstance(celcius, (int, float)):
        try:
            celcius: float = float(input(f"Please insert the °C to convert in °F: "))        
        except ValueError as v:
            print(v, "Please insert a valid int or float value")
    return celcius

celcius = get_celcius(celcius)

fahrenheit:float = celcius * 9 / 5 + 32
print(f"The equivalent of {celcius} °C are {fahrenheit} °F")