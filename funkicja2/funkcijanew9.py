sar = [8,7,9,4,1,12,3,5,8,7]

rez = sorted(sar, key = lambda elem: (elem % 2, elem))
print (rez)

cars = ['opel', 'mercedes', 'subaru', 'volvo', 'suzuki','bmw']
print(sorted(cars))
print(sorted(cars, key = len))
print(sorted (cars, key = lambda car: (len(car),car)))
print(sorted (cars, key = lambda car: (car, len(car))))