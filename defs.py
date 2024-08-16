import subprocess
from datetime import datetime
from config import *


def ups_powered_type() -> str | None:

    result = subprocess.getoutput(snmp_get_battery)
    st = result[-65:-1]

    if st[1] == '0' and st[3] == '1':
        print('UPS Powered: line')
        return "line"
    elif st[1] == '1' and st[3] == '0':
        print('UPS Powered: battery')
        return "battery"
    else:
        return None


def ups_charge() -> int | None:
    try:
        result = subprocess.getoutput(snmp_get_charge)
        persent = int(result[-3:])
    except:
        return None
    else:
        print(f'Battery charge: {persent} %')
        return persent


def append_log(text: str):
    curr_time = datetime.now()
    with open(file=log_file, mode='a') as f:
        f.write(f"{curr_time} ==>> {text}")
