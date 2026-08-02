print("-"*50)
print("      MOVIE TICKET BOOKING SYSTEM")
print("-"*50)

movie = input("Enter Movie Name: ")
show = input("Enter Show Time: ")

adults = int(input("Enter Number of Adults: "))
children = int(input("Enter Number of Children: "))

adult_price = 200

total_viewers = adults + children
total_amount = adults * adult_price

print("-"*50)
print("          BOOKING SUMMARY")
print("-"*50)

print("Movie Name      :", movie)
print("Show Time       :", show)
print("Adults          :", adults)
print("Children        :", children)
print("Total Viewers   :", total_viewers)
print("Ticket Price    : ₹", adult_price, "(Adults Only)")
print("Children Ticket : FREE")
print("Total Amount    : ₹", total_amount)

print("-"*50)
print("     THANK YOU! ENJOY YOUR MOVIE")
print("-"*50)