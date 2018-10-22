#!/usr/bin/env python3

"""Copiando o conteudo de um arquivo de texto e salvando em outro"""

def main():
    infile = open('loren_Ipsum.txt', 'rt')
    outfile = open('copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\done.')


if __name__=="__main__":main()