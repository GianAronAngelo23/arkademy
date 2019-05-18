import string

letter = 'a'
myString = 'arkademy bootcamp'
myList = []

for i in myString:
    myList.append(i)

count = 0

for i in myList:
    if i == letter:
        count = count + 1
    else:
        continue

print ("Katanya adalah: " + myString, "jumlah huruf "+ letter, "adalah", count)