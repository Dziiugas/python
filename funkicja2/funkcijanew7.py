cars = ['opel', 'mercedes', 'subaru', 'volkswagen', 'suzuki','bmw']
print(sorted(cars))
print(sorted(cars, key = len))

def kiekPriebalsiu(sar):
    balses = ['a','e','i','y','u','o']
    kiek = 0
    for raide in sar:
        if raide.lower() not in balses:
            kiek += 1
        return kiek

print(sorted(cars, key = kiekPriebalsiu))