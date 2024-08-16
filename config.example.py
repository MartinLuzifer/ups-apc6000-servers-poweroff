log_file = "/root/ups.log"
ups_ip = ''

snmp_get_battery = f'snmpwalk -v 1 -c public {ups_ip} 1.3.6.1.4.1.318.1.1.1.11.1.1.0'
snmp_get_charge = f'snmpwalk -v 1 -c public {ups_ip} 1.3.6.1.4.1.318.1.1.1.2.2.1.0'
