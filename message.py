import discord
from commands import *
from info import token as key
import logging

file_name = 'unauthorized_user.txt'


# Configure the logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs.log',  # Log file
    filemode='a'         # Append mode (use 'w' to overwrite)
)

logging.info('this is a test')


channel_id = int(key.get('channel_id', 0))  # Convert to integer, default to 0 if not found
user_id = int(key.get('user_id', 0))  # Convert to integer, default to 0 if not found

token = key['token']

temp_command = TempCommand()
break_command = BreakCommand()
yes_command = YesCommand()
help_command = HelpCommand()
internet_speed_command = InternetSpeedCommand()
hello_command = HelloCommand()


COMMAND_MAP = {
    '/temp': temp_command,
    '/break': break_command,
    '/yes': yes_command,
    '/help': help_command,
    '/internet speed': internet_speed_command,
    'hello': hello_command,
    
}
Clist = COMMAND_MAP

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = discord.Client(intents=intents)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')
    print("bot is ready")
    logging.info(f'Logged in as {bot.user.name}!')
    logging.info("bot is ready")
   

@bot.event
async def on_message(message):
    logging.debug(message)
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Check if the message is from the allowed channel
    if message.channel.id == channel_id:
        content = message.content.lower()    
        # Check if the content is a command in Clist
        if content in Clist:
            command = Clist[content]  # Get the command object
            await command.execute(message)  # Execute the command
            print(f"Executed command from {message.author}: {content}")
        else:
            response = "I didn't understand that command."
            await message.channel.send(response)
    
    
    if isinstance(message.channel, discord.DMChannel) and message.author.id == user_id:
        content = message.content.lower()    
        # Check if the content is a command in Clist
        if content in Clist:
            command = Clist[content]  # Get the command object
            await command.execute(message)  # Execute the command
            print(f"Executed command from {message.author}: {content}")
        else:
            response = "I didn't understand that command."
            await message.channel.send(response)
            
    elif isinstance(message.channel, discord.DMChannel):
        # Respond to other users with a generic message or ignore
        information = f"Received DM from an unauthorized user called {message.author} author id:{message.author.id} content: {message.content}"
        # logging
        logging.info(information)
        
        with open(file_name, 'a') as file:
            file.write(information + '\n')
        
        
        await message.channel.send('You are not authorized to use this bot.')


def run_bot():
    bot.run(token)

# Run the bot
run_bot()
