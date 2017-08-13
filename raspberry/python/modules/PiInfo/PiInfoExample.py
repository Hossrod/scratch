import time
import PiInfo

piInfo = PiInfo.PiInfo()
logFile = "PiInfo.csv"

with open(logFile, 'w') as file:
    file.write("ºC,ºF,Core (v),SDRAM Core (v),SDRAM IO (v),SDRAM PHY (v)\n")

while 1:
    print("CPU:                " + "{0:.1f}".format(piInfo.cpuTempC) + "ºC, " + "{0:.1f}".format(piInfo.cpuTempF) + "ºF")
    print("Core Voltage:       " + str(piInfo.coreVoltage))
    print("SDRAM Core Voltage: " + str(piInfo.sdramCoreVoltage))
    print("SDRAM IO Voltage:   " + str(piInfo.sdramIOVoltage))
    print("SDRAM PHY Voltage:  " + str(piInfo.sdramPHYVoltage) + "\n")
    with open(logFile, 'a') as file:
        file.write(str(piInfo.cpuTempC) + "," + str(piInfo.cpuTempF) + "," + str(piInfo.coreVoltage) + "," + str(piInfo.sdramCoreVoltage) + "," + str(piInfo.sdramIOVoltage) + "," + str(piInfo.sdramPHYVoltage) + "\n")
    time.sleep(5.0)