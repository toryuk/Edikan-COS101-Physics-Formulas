from struct import pack_into


def velocity():
    u=float(input("enter initial velocity:"))
    a=float(input("enter acceleration:"))
    t=float(input("enter time"))
    print("answer:",u+(a*t))

def force():
        m=float(input("enter mass"))
        a=float(input("enter acceleration"))
        print("answer",m*a)

def weight():
            m=float(input("enter mass"))
            g=9.8
            print("answer",m*g)

def power():
                w=float(input("enter work done"))
                t=float(input("enter time"))
                print("answer",w/t)

def kinetic_energy():
    m=float(input("enter mass"))
    v=float(input("enter velocity"))
    print("answer:",0.5*m*(v**2))

while True:
    print("\n===physics calculator===")
    print("1.velocity")
    print("2.force")
    print("3.weight")
    print("4.power")
    print("5.kinetic energy")

    choice=input("choose an operation")
    if choice=="1":
        velocity()
    elif choice=="2":
        force()
    elif choice=="3":
        weight()
    elif choice=="4":
        power()
    elif choice=="5":
        kinetic_energy()
    else:
        print("invalid choice!")
        repeat=input("do u want to continue?(yes/no):")
        if repeat.lower()=="no":
            print("calculator closed!")
            break








