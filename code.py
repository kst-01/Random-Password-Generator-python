import random
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
o=int(input("Enter length of random pass - "))
s=random.randint(0,25)
t=random.randint(0,25)
u=random.randint(0,9)
s2=random.randint(0,25)
t2=random.randint(0,25)
u2=random.randint(0,9)
s3=random.randint(0,25)
t3=random.randint(0,25)
u3=random.randint(0,9)
t4=random.randint(0,25)
p=(a[s]+b[t]+c[u]+a[s2]+b[t2]+c[u2]+a[s3]+b[t3]+c[u3]+a[t4])
print(p[:o])
