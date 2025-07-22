distance = int(input("Enter your distance "))
if(5 <= distance <= 50 ):
    print("10 THB")
elif(51 <= distance <= 100 ):
    print("15 THB")
elif(101 <= distance <= 300 ):
    print("25 THB")
elif(301 <= distance <= 500 ):
    print("35 THB")
elif(distance > 500 ):
    print("45 THB")    
else:
    print("0 THB")   