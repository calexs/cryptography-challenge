from socket import *
serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))

def decrypt(texto_cifrado,  key = 4):
        ''' (Caesar, str, int) -> str
 
        Retorna em texto plano o texto_cifrado decifrado
        com a cifra de Cesar, utilizando a chave key,
        cujo padrao e 3.
        '''
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        plain_text = ''
        texto_cifrado = texto_cifrado.upper()
        for ch in texto_cifrado:
            if ch in letters:
                idx = letters.find(ch) - key
                plain_text += letters[idx]
        return plain_text.lower()

print ("UDP server\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8
    text = decrypt(text)
    print ("Received from Client:", text)