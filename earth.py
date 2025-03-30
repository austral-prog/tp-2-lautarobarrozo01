def earth():
    x = "Bangladesh"
    y = "Barbados"
    chequeo1 = x.lower()<y.lower()
    chequeo2 = y.lower()<x.lower()
    print(f"The result of {x} comes first in the dictionary than {y} is {chequeo1}.")
    print(f"The result of {y} comes first in the dictionary than {x} is {chequeo2}.")
