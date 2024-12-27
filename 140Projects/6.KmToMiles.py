from typing import Final

CONVERSION_RATE: Final[float] = 0.621371

try:
    km: float = float(input(f"Please insert the Km to convert in Miles: "))
    miles = round(km * CONVERSION_RATE, 2)
    print(f"{km} are equivalent to {miles} miles")
except ValueError as v:
    print(v, "Please insert a valid number")
