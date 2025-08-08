# Exceptions Handling with try-exception block which is similar to try-catch block
denominator = int(input("Enter a denominator: "))
numerator = int(input("Enter a numerator: "))
try: 
    result = numerator///denominator
except Exception as e:
    print("Raised Error: ",e.upper())
else:
    print("Do not Enter Zero as a denominator!")

