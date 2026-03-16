choice = input("Please enter 2, 3, 4, 5 or 6: ").strip()

if choice == "2":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    result = x ** 2 + y ** 4
    print("Result:", result)
elif choice == "3":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    result = x ** 3 + y ** 3 + z ** 8
    print("Result:", result)
elif choice == "4":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    k = float(input("Enter k: "))
    result = x ** 3 + y ** 2 + z ** 2 + k ** 9
    print("Result:", result)
elif choice == "5":
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the 2nd number: "))
    c = float(input("Enter the 3rd number: "))
    d = float(input("Enter the 4th number: "))
    result = a * b * c * d
    print("Result:", result)
elif choice == "6":
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the 2nd number: "))
    c = float(input("Enter the 3rd number: "))
    d = float(input("Enter the 4th number: "))
    result = max(a, b, c, d)
    print("Result:", result)
else:
    print("Invalid input. Please enter 2, 3, 4, 5 or 6.")
