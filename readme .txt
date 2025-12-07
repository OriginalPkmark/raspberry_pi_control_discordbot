Note: the commands and other stuff important stuff are in the ``` ``` for easier copy and paste




---

### 1️⃣ Create a PATH where the bot files are going to be eg: /home/nvme/python_apps/my_app

then run these commands
```
sudo chmod -R 777 /home/nvme/python_apps
cd /home/nvme/python_apps/my_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

This way, your program has its own libraries.

---

### 2️⃣ Create a systemd service file

Make a service file, e.g.

```
sudo nano /etc/systemd/system/discord_bot.service
```

update with ur own info then Put this inside:

```
[Unit]
Description=Discord Bot
After=network.target

[Service]
Type=simple
User=
WorkingDirectory=/home/python_apps/discord_bot
ExecStart=/home/python_apps/discord_bot/my_env/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target




```

---

### 3️⃣ Enable and start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable discord_bot.service
sudo systemctl start discord_bot.service
```

---

### 4️⃣ View logs

Systemd has logging built-in.  To see logs:

```
journalctl -u discord_bot.service -f
```

---

this will:

* Run your program at boot.
* Use your virtual environment (so required libraries are available).
* Auto-restart if it crashes.
* Keep logs in systemd.

---

