
## simple ADC test contributed by:   ul-gh

import pyads1256
import sys
import time

ads = pyads1256.ADS1256()

idNumber = ads.ReadID()
print("\nADS1256 reported ID value: {}".format(idNumber))


print("\nPress CTRL-C to interrupt..")
while True:
    ads.SetInputMux(ads.MUX_AIN0, ads.MUX_AINCOM)
    time.sleep(0.2) #Multiple of line frequency period
    val = ads.ReadADC()
    sys.stdout.write("AIN_0 value: {:d}\n".format(val))
   
    ads.SetInputMux(ads.MUX_AIN1, ads.MUX_AINCOM)
    time.sleep(0.2)
    val = ads.ReadADC()
    sys.stdout.write("AIN_1 value: {:d}\r\033M".format(val))
    sys.stdout.flush()

