import socket
import os

def send_file(file_path, connection):
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            connection.sendall(data)
            data = file.read(1024)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 7777))
    server.listen(1)

    connection, address = server.accept()

    namefile = connection.recv(1024).decode()
    print(f"Recebendo arquivo: {namefile}")

    # Obtendo o caminho absoluto do arquivo
    file_path = os.path.abspath(namefile)

    # Verificando se o arquivo existe
    if os.path.exists(file_path):
        send_file(file_path, connection)
        print('Arquivo enviado!')
    else:
        print(f"Arquivo não encontrado: {file_path}")

    connection.close()
    server.close()

if __name__ == "__main__":
    main()

