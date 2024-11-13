SaldainiuKaina = 0.5
GumosKaina = 0.75
TraskuciuKaina = 1.00
GerimoKaina = 1.50

Pinigai=float(input('Kiek tu turi pinigų?'))
if Pinigai<0.50:
    print('Neužtenka lėšų')
elif Pinigai<0.75:
    print('Galite įsigyti saldainį (1)')
    Pasirinkimas=int(input('Pasirinkite prekę'))
    if Pasirinkimas == 1:
        Pinigai = Pinigai - SaldainiuKaina
        print("Ačiū, pasiimkite saldainį")
    elif Pasirinkimas == 2 or Pasirinkimas == 3 or Pasirinkimas == 4:
        print('Neužtenka pinigų')
    else:
        print('#ERROR')
elif Pinigai<1.00:
    print('Galite įsigyti saldainį(1) ir gumos(2)')
    Pasirinkimas=int(input('Pasirinkite prekę'))
    if Pasirinkimas == 1:
        Pinigai = Pinigai - SaldainiuKaina
        print("Ačiū, pasiimkite saldainį")
    elif Pasirinkimas == 2:
        Pinigai = Pinigai - GumosKaina
        print("Ačiū, pasiimkite gumą")
    elif Pasirinkimas == 3 or Pasirinkimas == 4:
        print('Neužtenka pinigų')
    else:
        print('#ERROR#')
elif Pinigai<1.5:
    print('Galite įsigyti saldainį(1), gumos(2) ir traškučių(3)')
    Pasirinkimas=int(input('Pasirinkite prekę'))
    if Pasirinkimas == 1:
        Pinigai = Pinigai - SaldainiuKaina
        print("Ačiū, pasiimkite saldainį")
    elif Pasirinkimas == 2:
        Pinigai = Pinigai - GumosKaina
        print("Ačiū, pasiimkite gumą")
    elif Pasirinkimas == 3:
        Pinigai = Pinigai - TraskuciuKaina
        print("Ačiū, pasiimkite traškučius")
    elif Pasirinkimas == 4:
        print('Neužtenka pinigų')
    else:
        print('#ERROR#')
elif Pinigai>1.5:
    print('Galite įsigyti saldainį(1), gumos(2), traškučių(3) ir gėrimą(4)')
    Pasirinkimas=int(input('Pasirinkite prekę'))
    if Pasirinkimas == 1:
        Pinigai = Pinigai - SaldainiuKaina
        print("Ačiū, pasiimkite saldainį")
    elif Pasirinkimas == 2:
        Pinigai = Pinigai - GumosKaina
        print("Ačiū, pasiimkite gumą")
    elif Pasirinkimas == 3:
        Pinigai = Pinigai - TraskuciuKaina
        print("Ačiū, pasiimkite traškučius")
    elif Pasirinkimas == 4:
        Pinigai = Pinigai - GerimoKaina
        print("Ačiū, pasiimkite gėrimą")
    else:
        print('#ERROR#')
        
print("Jusu likutis: ", Pinigai)