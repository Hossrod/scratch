import time
import PiInfo

piInfo = PiInfo.PiInfo()
logFile = "PiInfo.csv"

# Create csv file (with header row) to log to
with open(logFile, 'w') as fi:
    fi.write("ºC,ºF,Core (v),SDRAM Core (v),SDRAM IO (v),SDRAM PHY (v)\n")

# Loop forever printing out PiInfo to console and CSV log file.
while 1:
    # Print info to console.
    print("CPU Temp ºC:        " + str(piInfo.cpuTempC))
    print("CPU Temp ºF:        " + str(piInfo.cpuTempF))
    print("Core Voltage:       " + str(piInfo.coreVoltage))
    print("SDRAM Core Voltage: " + str(piInfo.sdramCoreVoltage))
    print("SDRAM IO Voltage:   " + str(piInfo.sdramIOVoltage))
    print("SDRAM PHY Voltage:  " + str(piInfo.sdramPHYVoltage) + "\n")

    # Append new row of info to csv log file.
    with open(logFile, 'a') as fi:
        fi.write(str(piInfo.cpuTempC) + ","
        + str(piInfo.cpuTempF) + ","
        + str(piInfo.coreVoltage) + ","
        + str(piInfo.sdramCoreVoltage) + ","
        + str(piInfo.sdramIOVoltage) + ","
        + str(piInfo.sdramPHYVoltage) + "\n")

    # Sleep for specified time before getting new info to print/log.
    time.sleep(5.0)
