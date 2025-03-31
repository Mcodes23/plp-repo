def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        print (price - discount_amount)
    else:
        print(price)

user_price = int(input("Enter price: "))
user_discount_percent = int(input("Enter discount percent: "))
calculate_discount(user_price, user_discount_percent)