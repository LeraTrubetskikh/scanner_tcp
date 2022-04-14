import argparse
import socket
import sys


class Scanner:
    def __init__(self, ip):
        self.ip = ip

    def check_tcp(self, port):
        s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_tcp.settimeout(0.01)
        try:
            s_tcp.connect((self.ip, port))
            print(self.ip + ': ' + str(port) + ' is open')
        except:
            pass
        finally:
            s_tcp.close()


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('ip', nargs='?')
    p.add_argument('-s', '--start', default='0')
    p.add_argument('-e', '--end', default='65535')
    return p


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    scanner = Scanner(namespace.ip)

    for i in range(int(namespace.start), int(namespace.end)):
        scanner.check_tcp(i)
