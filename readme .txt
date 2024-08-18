you need the discord, gpiozero, and speedtest-cli to make this code function 

please update the info with your own token, server channal id and user id 

note: if you user wrong user id it it will log u as a unwanted user


. Using screen or tmux
These are terminal multiplexers that allow you to start a session and keep it running, even if you disconnect.

Install screen:
sudo apt-get install screen

Create a new screen session you can change the mybot to a name you like :
screen -S mybot


Run your script:
python3 /home/markpi/discord_bots/pi_bot/main.py

Detach from the screen session:
Press Ctrl + A followed by D.

To reattach later, use:
screen -r mybot