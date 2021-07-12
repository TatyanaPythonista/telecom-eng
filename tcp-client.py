import socket
import logging

main_log = logging.getLogger('main')
main_log.setLevel(logging.DEBUG)
main_fh = logging.FileHandler("tracker.log", 'a', 'utf-8')
main_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
main_fh.setFormatter(main_formatter)
main_log.addHandler(main_fh)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('127.0.0.1', 8888))
        message = input('Введите данные: ')
        sock.send(bytes(message, encoding='utf-8'))
        main_log.info(f'Сообщение {message} отправлено.')
        data = sock.recv(1024)
        main_log.info(f'Сообщение {data.decode("utf-8")} получено.')
        print('Message: ', data.decode('utf-8'))
except ConnectionResetError:
    main_log.critical("Разорвано соединение с сервером")
    print("Разорвано соединение с сервером")

