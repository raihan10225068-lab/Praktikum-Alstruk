bilangan = int(input("Masukan sebuah bilangan: "))

if bilangan > 1:
    is_prima = True
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            is_prima = False
            break
    if is_prima:
        print("Output: bilangan prima")
    else:
        print("Output: bukan bilangan prima")
else: 
    print("Output: bukan bilangan prima")