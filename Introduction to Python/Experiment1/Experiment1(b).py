def XOR(a,b):
    if a != b:
        return 1
    else:
        return 0 

# Truth table for XOR
print("A\tB\tXOR")
print("0\t"+"0\t"+str(XOR(0,0)))
print("0\t"+"1\t"+str(XOR(0,1)))
print("1\t"+"0\t"+str(XOR(1,0)))
print("1\t"+"1\t"+str(XOR(1,1)))