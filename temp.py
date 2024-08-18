import os
import time

temperature_threshold = 90.0

def get_temperature():
    return float(os.popen("vcgencmd measure_temp").readline().replace("temp=", "").replace("'C\n", ""))

def continuous_temperature_monitoring():
    while True:
        temperature = get_temperature()
        print(f"Current temperature: {temperature}°C")

        if temperature > temperature_threshold:
            os.system("sudo shutdown now")
        
        time.sleep(10)


