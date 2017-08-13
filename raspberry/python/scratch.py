def printBars(number):
    print((number * '='))

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
for element in a:
    if element == max(a):
        printBars(element)
        print('We reached the largest')
    printBars(element)