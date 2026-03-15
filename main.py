count = input("Please enter 2 or 3: ").strip()

if count == "2":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    result = x ** 2 + y ** 4
    print("Result:", result)
elif count == "3":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    result = x ** 3 + y ** 3 + z ** 8
    print("Result:", result)
else:
    print("Invalid input. Please enter 2 or 3.")
