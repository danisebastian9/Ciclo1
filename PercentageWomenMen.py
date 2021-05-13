quantW = int(input("Add the amount of Women Students "))
quantM = int(input("Add the amount of Men Students "))
totalStudents = quantM + quantW
percentW = quantW * 100 / totalStudents
percentM = quantM * 100 / totalStudents
print("The percentage of Women is ", percentW, '% and the Men percentage is ', percentM, "%")