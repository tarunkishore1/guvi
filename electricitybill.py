print("Enter the units consumed")

units=int(input())

if (units<=100):

    cost=units*2

    print("Your Electricity Bill Amount is ")

    print(cost)

elif (units>100) and (units<=200):

    cost=units*4

    print("Your Electricity Bill Amount is ")

    print(cost)

elif (units>200) and (units<=300):

    cost=units*6
    
    print("Your Electricity Bill Amount is ")

    print(cost)

elif (units>300) and (units<=400):

    cost=units*8

    print("Your Electricity Bill Amount is ")

    print(cost)

elif (units>400) and (units<=500):

    cost=units*10
    
    print("Your Electricity Bill Amount is ")

    print(cost)

else:

    cost=units*15

    print("Your Electricity Bill Amount is ")

    print(cost)