# ups-apc6000-servers-poweroff

## How TO

1. Git clone
2. `cp config.example.py config.py`
3. Edit `config.py`
4. `crontab -e`
5. `*/1 * * * * /usr/bin/python3 /root/python/ups/main.py`
