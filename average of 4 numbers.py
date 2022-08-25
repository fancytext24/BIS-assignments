numbers=[]
for i in range(4):
    try:
        number=int(input("Enter a number: "))
        numbers.append(number)
    except ValueError: # When the user inputs non numeric values
        number=0
        print("Invalid input, Assuming value to be 0")

average  = sum(numbers)/4 
print(f"Your average is: {average}")
if average >= 50:
    print("Well done")
else:
    print("Better luck next time")