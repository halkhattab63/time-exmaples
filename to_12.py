# 12 قم بعمل مخطط تدفقي يأخذ الساعة الآن ويطبع كم ساعة بقي حتى الساعة 
#  (إذا كانت الساعة الان الثامنة فسيتم طباعة أربع ساعات).

import datetime
def timeTO12(): 
    timeNow = datetime.datetime.now().hour
    TO_12 = (12 - timeNow)%12
    print(f"time TO 12 is {TO_12}")


timeTO12()