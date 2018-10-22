#!/usr/bin/env python3

# Abrindo um aarquivo em branco
f = open('arquivo.txt', 'w')  # caso o arquivo nao exista será criado, 'w' = write, escrita
f.close() # fecha o arquivo




#
# def main():
#     f = open('lines.txt', 'r')
#     # print(f"Nome do arquivo: {f.name}")
#     # print(f"Modo que foi aberto: {f.mode}")
#     print()
#     for line in f:
#         print(line.rstrip())
#
#
# if __name__=="__main__":main()