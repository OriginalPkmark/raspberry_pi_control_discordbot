A discord bot that controls a raspberry pi it uses discord, gpiozero, and speedtest-cli libraries also it has a constant temp monitor. 

more and better commands may come in the future sometime soon



GETTING STARTED:

*  make sure you have the three librares installed (note: in the read me txt there is a way to run it in the background)

*  update info with your own informations(token, channel id, username and user id)

*  run the main.py






Note you can also use docker to run it:

* make a directory that you want to run it at : /mnt/@example
* save the files in the directory
* create a Dockerfile. You can check the examplefile for how
* then build the bot with the command (note: you can rename to whatever you want; I just name it bot for now): docker build -t bot .
* then run it: docker run -d --name python-container bot
  
