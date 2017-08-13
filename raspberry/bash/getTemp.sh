#!/bin/bash
# Display the ARM CPU and GPU  temperature of Raspberry Pi 2/3 
# -------------------------------------------------------

cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp | sed -e "s/^temp=//")"
echo "CPU => $((cpu/1000))'C"