import base64
import binascii
from tkinter.filedialog import askopenfilename
from tkinter import *

root = Tk()





print("Добро пожаловать в прогу версия 0.6. Роберт Ислямов"  )
print("Выбери файл, который нужно конвертировать")
file = askopenfilename()

print('{:*^60}'.format('Данные'))

with open(file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    encoded_string = str(encoded_string)
    encoded_string = encoded_string[1:]
    encoded_string = encoded_string[1:]
    encoded_string = encoded_string[:-1]


for i in range(len(encoded_string)):
    print(encoded_string[i], end='')
    i = i + 1
    if i % 60 == 0:
        print("")




print("")
print("")
print('{:*^60}'.format('Контрольная сумма'))


buf = open(file,'rb').read()
buf = (binascii.crc32(buf) & 0xFFFFFFFF)
print('{: ^60}'.format(buf))

print("")
print("")
root.destroy()
input('Нажми  ENTER чтобы выйти')









