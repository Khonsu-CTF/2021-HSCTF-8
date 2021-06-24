from pwn import *

def fibs(n):
    fibs = [4,5]
    s = [4]

    for i in range(2,n+2):
        fibs.append(fibs[i-1]+fibs[i-2])
        s.append(s[i-2]+fibs[i-1])

    return str(sum(s))[-10:]

conn = remote('extended-fibonacci-sequence-2.hsc.tf',1337)

conn.recvline()
generated = str(conn.recvline())
while ("generated" in generated):
    print(conn.recvline())
    nnn = int(conn.recvline()[:-1])
    conn.sendline(fibs(nnn))
    print(conn.recvline())
    generated = str(conn.recvline())
    print(generated)

print(conn.recvline())
print(conn.recvline())

conn.close()
