SumOfOdds = 0
for i in range(100):
    if i%2 == 1:
        print(i)
        SumOfOdds = SumOfOdds+i
    else:
        pass

print("Sum of all odds till 100 = ", SumOfOdds)