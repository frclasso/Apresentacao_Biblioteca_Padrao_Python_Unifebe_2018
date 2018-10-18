#!/usr/bin/env python3


myFile = open('scores.txt', 'w')

## Show attributes  and properties of that file
print('Name: ', myFile.name)
print('Mode: ', myFile.mode)

# Write a file
myFile.write("First Player: 100"
             "\nSecond Player: 200"
             "\nThird Player: 300")

myFile.close()


# exemplo2
# Abrindo o arquivo
fo = open('foo.txt', 'w')
fo.write("Python is a great language.\nYeah its great!")

# Fechando
fo.close()
