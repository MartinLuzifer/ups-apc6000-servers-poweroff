# ups-apc6000-servers-poweroff

## How TO

1. Make dir and change current directory
   ``` bash
   mkdir -p ~/python/ups/
   cd ~/python/ups/
   ```
2. Clone repo:
   ``` bash
   git clone https://github.com/MartinLuzifer/ups-apc6000-servers-poweroff.git .
   ```
   > ***copy all include dot (.)***
3. Create configfile:
   ``` bash
   cp config.example.py config.py
   ```
4. Edit `config.py`: set ip address ups, set log-file
5. Install snmpwalk, if not install
   ``` bash
   sudo apt install -y snmp
   ```
6. Create task in `crontab -e`
   ```
   */1 * * * * /usr/bin/python3 /root/python/ups/main.py
   ```
