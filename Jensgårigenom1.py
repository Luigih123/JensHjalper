meter = int(input('släpp bollen från: '))

centimeter = 100 * meter
studs = 0

while centimeter > 1:
    print(centimeter * meter)
    centimeter = centimeter * 0.7
    print(centimeter)
    studs += 1
    print(meter)

print(f'studs: {studs}')
