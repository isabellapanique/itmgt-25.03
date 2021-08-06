def get_product(code):
    return products.get(code)

def get_property(code,property):
    return products[code][property]

def main():
    order = ""
    order_dict = {}
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    
    while True:
        order = input("ORDER & QUANTITY \nExample: americano,2\n")
        
        if order != "/":
            product,quantity = order.split(",")
            order_dict[product] = get_product(product)
            
            if product == "americano":
                a += 1*int(quantity)
                order_dict[product]["quantity"] = a
            elif product == "brewedcoffee":
                b += 1*int(quantity)
                order_dict["brewedcoffee"]["quantity"] = b 
            elif product == "cappuccino":
                c += 1*int(quantity)
                order_dict["cappuccino"]["quantity"] = c
            elif product == "dalgona":
                d += 1*int(quantity)
                order_dict["dalgona"]["quantity"] = d
            elif product == "espresso":
                e += 1*int(quantity)
                order_dict["espresso"]["quantity"] = e
            elif product == "frappuccino":
                f += 1*int(quantity)
                order_dict["frappuccino"]["quantity"] = f
        
        else:
            break
    
    with open('receipt.txt', 'w') as f:
        f.write('''
        ==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')

        total = 0
        for i in dict(sorted(order_dict.items())):
            code = i
            name = order_dict[i]["name"]
            price = order_dict[i]["price"]
            quantity = order_dict[i]["quantity"]
            subtotal = int(price)*int(quantity)
            total += subtotal

            f.write(f'''
{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}''')
        
        f.write(f'''
Total:\t\t\t\t\t\t\t\t\t\t{total}
        ==
    ''')
        
main()