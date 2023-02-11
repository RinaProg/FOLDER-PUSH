import time 
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title ="It's Time to Drink Water ",
            message ="Water helps your body:Keep a normal temperature. Lubricate and cushion joints.Protect your spinal cord and other sensitive tissues. Get rid of wastes through urination, perspiration, and bowel movements.",
            app_icon ="D:\PYTHON_CODES\icon.ico" ,
            timeout = 10          
        )
        time.sleep(60*60)
