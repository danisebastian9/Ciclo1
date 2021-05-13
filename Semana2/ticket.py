# This exercise calculates the total of a ticket price based on the amount of km and the price per km.

kmAmount = int(input("Add the amount of KM for your desired bus route "))
kmPrice = 1050
ticketPrice = kmAmount * kmPrice
print('The ticket price is $', ticketPrice, ' for your bus route.' )