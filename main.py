import threading
import temp
import message


    # Run temperature monitoring in a separate thread
temp_thread = threading.Thread(target=temp.continuous_temperature_monitoring)
temp_thread.start()
#Run Discord bot
message.run_bot()
    