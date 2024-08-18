#this is where all the code that needs to do processing at

import os
import speedtest

def get_temperature():
    return float(os.popen("vcgencmd measure_temp").readline().replace("temp=", "").replace("'C\n", ""))



def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    return download_speed, upload_speed