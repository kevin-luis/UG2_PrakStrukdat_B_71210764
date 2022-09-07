import time


def deret_iteratif(n):
    awal = [1,2,3,4,5]
    for i in range(1,n-4):
        jumlah = awal[2] + awal[2+i]
        awal.append(jumlah)
    return awal

def deret_rekursif(n):
    if n < 6 :
        return n
    else :
        return deret_rekursif(n-2) + deret_rekursif(n//2)

print(deret_iteratif(100))

start = time.time()
print(deret_rekursif(4))
end = time.time()
print(end - start)