'''
Pseudocode:

Given X dollars, first attempt to find lowest modulus for each cookie.
If 0, you are done.
Otherwise, find how many of each cookie you can buy and record change.
Minimize amount of change left after each possible other cookie purchase via int. div.
Output what cookie and amount of change

'''

# cookie.py

#Sugar - 2.65
#Choc - 3.20
#Snicker - 3.45
#Smore - 3.70

inputMoney = float(input("How much money do you have? "))

# sugarPrice = float(input("Sugar cookie price: "))
# chocPrice = float(input("Chocolate cookie price: "))
# snickerPrice = float(input("Snickerdoodle cookie price: "))
# smorePrice = float(input("S'more cookie price: "))

# Order is: sugar, choc, snicker, smore
cookieStr = ["Sugar", "Chocolate", "Snickerdoodle", "S'more"]
cookieArr = [2.65,3.20,3.45,3.70]
orderArr = [0,0,0,0]

remainder = [9999,9999,9999,9999]
numCookie = 0
# Check for perfect cookie order
for i in range(0,4):
    if (inputMoney % cookieArr[i] == 0):
        print("\nOnly buy " + cookieStr[i] + " cookies")
        exit()
    numCookie = inputMoney // cookieArr[i]
    if (numCookie != 0):
        remainder[i] = round(inputMoney % cookieArr[i],2)
        orderArr[i] = numCookie
    else:
        break

minIndex = remainder.index(min(remainder))

print("\nBuy " + str(int(orderArr[minIndex])) + " " + cookieStr[minIndex] + " cookies")
print("$" + str(remainder[minIndex]) + " remaining\n")

