#!/usr/bin/python3
from defs import *
from config import charge_limit

powered_type = ups_powered_type()
battery_charge = ups_charge()

if (powered_type is not None) and (battery_charge is not None):

    match powered_type:

        case "line":
            if battery_charge <= 100:
                append_log(f"Powered type: {powered_type} ; Battery charge: {battery_charge}% ; (Full) \n")
            if battery_charge > 100:
                append_log(f"Powered type: {powered_type} ; Battery charge: {battery_charge}% ; (Charged) \n")

        case "battery":
            if battery_charge >= charge_limit:
                append_log(f'Powered type: {powered_type} ; Battery charge: {battery_charge}%  \n')
            if battery_charge < charge_limit:
                append_log(f'Battery charge: {battery_charge}% ; Powered type: {powered_type} \n Shutdown system!!! \n')
                output = subprocess.getoutput("poweroff")  # POWEROFF
                append_log(output)
