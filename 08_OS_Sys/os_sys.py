#!/usr/bin/env python3

import sys, os


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    w = sys.platform
    print(w)

    z = os.name
    print(z)
    print()


    y = os.getenv('PATH')  # imprime variaveis de ambiente
    print(y)
    print()

    i = os.getcwd()  # imprime diretorio local
    print(i)
    print()

    # imprime o PATH do arquivo e da instalacao do Python
    for p in sys.path: print(p)


if __name__=="__main__":main()
