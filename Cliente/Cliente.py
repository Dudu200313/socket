import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('localhost', 7777))
    print('Conectado!\n')

    namefile = input('Arquivo> ')

    client.send(namefile.encode())

    with open(namefile, 'wb') as file:
        while True:
            data = client.recv(1000000)
            if not data:
                break
            file.write(data)

    print(f'{namefile} recebido!\n')

except Exception as e:
    print(f"Erro durante a execução: {e}")

finally:
    client.close()