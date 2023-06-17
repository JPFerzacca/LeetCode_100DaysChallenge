def numberOfSteps(num):
    solution = ""
    counter = 0
    while num != 0:
        if(num % 2 == 1):
            num = num - 1
            counter += 1
            solution = solution + "Step "+ str(counter) + ") " + str((num + 1)) + " is odd; subtract 1 and obtain " + str(num) + ".\n"
        else:
            num = int(num/2)
            counter += 1
            solution = solution + "Step "+ str(counter) + ") " + str((num + 1)) + "is even; divide by 2 and obtain " + str(num) + ".\n"
    return solution

print(numberOfSteps(7))