from gpiozero import CPUTemperature
from maintext import *
import subprocess

class Command:
    def execute(self, message):
        pass

class TempCommand(Command):
    async def execute(self, message):
        current_temperature = get_temperature()
        response = f"Current temperature: {current_temperature}°C ❄️🤔"
        await message.channel.send(response)

class BreakCommand(Command):
    async def execute(self, message):
        response = "Are you sure? Type '/yes' to confirm. ⚠️"
        await message.channel.send(response)

class YesCommand(Command):
    async def execute(self, message):
        try:
            subprocess.run(["sudo", "shutdown", "now"], check=True)
            response = "Shutting down the Raspberry Pi. Goodbye! 👋🚀"
        except subprocess.CalledProcessError as e:
            response = f"Failed to shut down the Raspberry Pi. Error: {e} ❌"
        except Exception as e:
            response = f"An unexpected error occurred: {e} ❌"
        await message.channel.send(response)


class HelpCommand(Command):
    async def execute(self, message):
        response = "List of commands: /temp, /break, /internet speed"
        await message.channel.send(response)  # This line may cause an error, see note below

class InternetSpeedCommand(Command):
    async def execute(self, message):
        download_speed, upload_speed = check_internet_speed()
        if download_speed > 50 and upload_speed > 10:
            response = f"Great speeds! Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps 🚀"
        elif download_speed > 20 and upload_speed > 5:
            response = f"Decent speeds! Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps 🌐"
        else:
            response = "Consider checking your internet connection. ❓"
        await message.channel.send(response)  # This line may cause an error, see note below

class HelloCommand(Command):
    async def execute(self, message):
        response = "Hello👋👋! What can I help you with?There is a list of commands: /temp, /break, /internet speed 🤔🤔"
        await message.channel.send(response)  # This line may cause an error, see note below