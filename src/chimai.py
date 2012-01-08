import imaplib

HOST = 'localhost'
PORT = imaplib.IMAP4_PORT
USER = 'mailuser'
PASS = '123'


def main():
    M = imaplib.IMAP4(host=HOST, port=PORT)
    M.login(USER, PASS)
    M.select()
    typ, data = M.search(None, 'ALL')
    print(typ, data)
    for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        print(typ, data)
        print('Message %s\n%s\n' % (num, data[0][1]))

    M.close()
    M.logout()


if __name__ == '__main__':
    main()
