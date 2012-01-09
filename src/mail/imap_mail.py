import imaplib

from settings import HOST, PORT, USER, PASS


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
