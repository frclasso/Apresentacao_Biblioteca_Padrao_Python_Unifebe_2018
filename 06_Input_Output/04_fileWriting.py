#!/usr/bin/env python3


myFile = open('scores.txt', 'w')

## Show attributes  and properties of that file
print('Name: ', myFile.name)
print('Mode: ', myFile.mode)

# Write a file
myFile.write("First Player: 100"
             "\nSecond Player: 200"
             "\nThird Player: 300"
             "\nFourth Player: 250"
             "\nFifth Player: 350")

myFile.close()


# exemplo2
# Abrindo o arquivo
# fo = open('arquivo.txt', 'w')
# fo.write("Python is a great language.\nYeah its great!")
#
# # Fechando
# fo.close()
