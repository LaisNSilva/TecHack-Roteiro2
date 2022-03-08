import sys
import socket
from socket import getservbyport

ipAddress = input("Digite o IP: ")
p = input("Digite a(s) porta(s) separando por com espacos. Caso queira ver todas aperte Enter: ")
ports = p.split()
if len(ports)==0:
	ports = list(range(1,65535))



for port in ports:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	port = int(port)
	try:
		if s.connect_ex((ipAddress, port)) == 0:
			if port in range(0, 1024):
				service = getservbyport(port, "tcp")
				print(f"Porta {port} Aberta  "+service)
			else:
				print(f"Porta {port} Aberta  ")
		s.close()

	except KeyboardInterrupt:
		print('Você pressionou <Ctrl>+<C>')
		sys.exit()

	except socket.gaierror:
		print('O hostname não pode ser resolvido')
		sys.exit()

	except socket.error:
		print('Não foi possível conectar no servidor')
		sys.exit()   