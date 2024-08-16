#!/usr/bin/python3
from defs import *

powered_type = ups_powered_type()
battery_charge = ups_charge()

if (powered_type is not None) and (battery_charge is not None):
    match powered_type:

        case "line":
            if battery_charge >= 75:
                append_log(f"Battery charge: {battery_charge}% ; Powered type: {powered_type} \n")
            if battery_charge < 70:
                append_log(f"Battery charge: {battery_charge}% ; Powered type: {powered_type} (charged) \n")

        case "battery":
            if battery_charge >= 75:
                append_log(f'UPS APC 6000 Battery charge: {battery_charge}%, Powered type: {powered_type} \n')
            if battery_charge < 75:
                append_log(f'Battery charge: {battery_charge}% ; Powered type: {powered_type} \n shutdown system \n')
                subprocess.getoutput("poweroff")


