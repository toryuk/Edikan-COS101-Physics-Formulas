# COS 101 ASSIGNMENT
# FIVE PHYSICS FORMULAS
# Name: EDIKAN UBONG UKPONG

print("===================================")
print("       PHYSICS FORMULA CALCULATOR")
print("===================================")

while True:
    print("\nSelect a formula to calculate:")
    print("1. Final Velocity (v = u + at)")
    print("2. Force (F = ma)")
    print("3. Weight (W = mg)")
    print("4. Power (P = W/t)")
    print("5. Kinetic Energy (KE = 1/2mv^2)")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        u = float(input("Enter initial velocity: "))
        a = float(input("Enter acceleration: "))
        t = float(input("Enter time: "))
        v = u + a * t
        print("Final Velocity =", v, "m/s")

    elif choice == "2":
        m = float(input("Enter mass: "))
        a = float(input("Enter acceleration: "))
        F = m * a
        print("Force =", F, "N")

    elif choice == "3":
        m = float(input("Enter mass: "))
        g = 9.8
        W = m * g
        print("Weight =", W, "N")

    elif choice == "4":
        work = float(input("Enter work done: "))
        t = float(input("Enter time: "))
        if t != 0:
            P = work / t
            print("Power =", P, "W")
        else:
            print("Time cannot be zero!")

    elif choice == "5":
        m = float(input("Enter mass: "))
        v = float(input("Enter velocity: "))
        KE = 0.5 * m * v ** 2
        print("Kinetic Energy =", KE, "J")

    elif choice == "0":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice. Please try again.")