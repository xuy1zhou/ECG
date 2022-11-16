# -*- coding: utf-8 -*-

import usbtmc
import time

scope = usbtmc.Instrument('USB0::0x1AB1::0x04CE::DS1ZA204920505::INSTR')
# scope.write(':WAVeform:SOUR CHAN1')

# scope.write(':RUN')

scope.write(':WAVeform:SOUR CHAN2')
scope.write(':WAVeform:SOUR CHAN2')
print(scope.ask(':WAVeform:FORMat?'))

# scope.write(':WAVeform:FORMat WORD')
# print(scope.ask(':WAVeform:FORMat?'))
# print(scope.ask(':WAVeform:DATA?'))
# time.sleep(5)
# print(scope.ask('*IDN?'))

