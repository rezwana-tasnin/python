import os

cart = []
quan = []

products = [ 
    "Alu (1kg)", #0
    "Onion (1kg)", #1
    "Chicken (1kg)" #2
]
prices = [
    30,
    100,
    300
]

def selectProduct(clear):
    if(clear):
        os.system('cls')
    print("\nProducts")
    print("=============================")
    for i in range(len(products)):
        print(f"{i+1}. {products[i]} - {prices[i]}")
    return int(input('# ')) - 1

def getWhatNext():
    os.system('cls')
    print('\nWhat do you want to do next?')
    print('=================================')
    print('1. Add more products')
    print('2. Checkout')
    return int(input('# '))

def getSpaceStr(n):
    str = ''
    for _ in range(n):
        str += ' '
    return str

def showCart():
    os.system('cls')
    print('\nCart')
    print('=================================')
    total = 0
    for i in range(len(cart)):
        total += prices[cart[i]] * quan[i]
        print(f"{i + 1}. {products[cart[i]].ljust(15 ,' ')} {str(prices[cart[i]]).ljust(5,' ')} {quan[i]}x = {prices[cart[i]] * quan[i]}")
    print('---------------------------------')
    print('Total'.ljust(27, ' ') + f' = {total}')

def checkout():
    showCart()

def addToCart(clear = False):
    pi = selectProduct(clear)
    ci = cart.index(pi) if pi in cart else -1
    if(ci == -1):
        cart.append(pi)
        quan.append(1)
    else:
        quan[ci] += 1
    next = getWhatNext()
    if(next == 1):
        addToCart(True)
    if(next == 2):
        checkout()

print('=================================')
print('===== Welcome to Our Shop =======')
print('=================================')

addToCart()
print('\n')
