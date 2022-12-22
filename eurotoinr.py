store = [("Jackets", 78.00),
         ("Hats", 15.00),
         ("Scarfs", 40.00),
         ("Shoes", 60.00)]

into_rupees = lambda data: (data[0], data[1]*88.06)

store_rupees = list(map(into_rupees, store))

for i in store_rupees:
    print(i)
