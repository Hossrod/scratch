"""
Module provides classes and methods for getting information about the running Raspberry Pi.

Notes:
  ~ vcgencmd info: http://elinux.org/RPI_vcgencmd_usage

"""

import subprocess

class PiInfo:

    def __vgcVolts(self, voltName):
        return float(subprocess
                     .check_output(['/opt/vc/bin/vcgencmd', 'measure_volts', voltName])
                     .decode('utf-8')
                     .replace("volt=", "")
                     .replace("V", ""))
    
    def __getTempC(self):
        return float(subprocess
                     .check_output(['/opt/vc/bin/vcgencmd', 'measure_temp'])
                     .decode('utf-8')
                     .replace("temp=", "")
                     .replace("'C", ""))
    
    def __getTempF(self):
        return self.__getTempC() * 9 / 5 + 32
    
    def __getCoreV(self):
        return self.__vgcVolts('core')
    
    def __getSdramCoreV(self):
        return self.__vgcVolts('sdram_c')
    
    def __getSdramIoV(self):
        return self.__vgcVolts('sdram_i')
    
    def __getSdramPhyV(self):
        return self.__vgcVolts('sdram_p')
    
    cpuTempC = property(__getTempC)
    cpuTempF = property(__getTempF)
    coreVoltage = property(__getCoreV)
    sdramCoreVoltage = property(__getSdramCoreV)
    sdramIOVoltage = property(__getSdramIoV)
    sdramPHYVoltage = property(__getSdramPhyV)
