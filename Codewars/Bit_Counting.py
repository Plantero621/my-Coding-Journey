n = 123
def count_bits(n):
    n = bin(n)[2:]
    einer = 0
    for i in n:
         if i == "1":
            einer+=1
    return einer
print(count_bits(n))
