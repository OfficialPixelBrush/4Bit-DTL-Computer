import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename()

program = []
        
with open(file, "rb") as f:
    while (byte := f.read(1)):
        # Do stuff with byte.
        integer = int.from_bytes(byte, "big")
        high, low = integer >> 4, integer & 0x0F
        #print(hex(high), "\t", hex(low))
        program.append(high)
        program.append(low)
#print(program)

for d in program:
    print(hex(d))
