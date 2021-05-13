# This exercise request a specific amount of units to order for a clothes shop and the total price is calculated. 

quantity123 = int(input("Add the amount of Men pants to order "))
total123 = quantity123 * 45000

quantity345 = int(input("Add the amount of Short sleeve Shirt to order "))
total345 = quantity345 * 35000

quantity456 = int(input("Add the amount of Polo Shirt to order "))
total456 = quantity456 * 27000

quantity567 = int(input("Add the amount of Round neck T-shirt to order "))
total567 = quantity567 * 12000

quantity678 = int(input("Add the amount of Anckle Socks pair to order "))
total678 = quantity678 * 3000

totalOrder = total123 + total345 + total456 + total567 + total678

print("The purchase total is $", totalOrder, "COP")