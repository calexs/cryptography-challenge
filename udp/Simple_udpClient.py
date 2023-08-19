from socket import *
serverName = "172.20.10.2" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6

def encrypt(self, texto_plano, key = 4):
        ''' (Caesar, str, int) -> str
 
        Retorna o texto_plano cifrado com a cifra
        de Cesar, utlizando a chave key,
        cujo padrao e 3.
        '''
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        cipher_text = ''
        texto_plano = texto_plano.upper()
        for ch in texto_plano:
            if ch in letters:
                idx = letters.find(ch) + key
                if idx >= 26:
                    idx -= 26
                cipher_text += letters[idx]
        return cipher_text

print("UDP Client\n")
while 1:
    message = input("Input message: ")
    if message == "exit":
            break
    message = encrypt(message)
    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
clientSocket.close()