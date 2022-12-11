# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2

leek_string = 'Leek is ' + str(leek_price) + ' euro per kilo.'
print(leek_string)

leek_order = 'leek 4'
leek_order_number = int(leek_order[5:])

sum_total = leek_order_number * leek_price

print(sum_total)

broccoli_price = 2.34
broccoli_order = 1.6

broccoli_total = round(broccoli_price * broccoli_order, 2)

print(str(broccoli_order) + 'kg broccoli costs ' + str(broccoli_total) + 'e')