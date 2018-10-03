import os
try:
    os.chdir('c:/users/dougl/desktop')
    file = open('teste.txt', 'x')
except Exception as e:
    os.chdir('c:/users/dougl/desktop')
    file = open('teste.txt', 'at')

file.write(
    '' + '\n')
file.close()
