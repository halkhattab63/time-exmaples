import datetime

# To find out the content inside the time function (dir)
# print(dir(datetime))
# print(dir(datetime.datetime))

print("*"*40)
print("*"*40)

# print the current Date and Time 
# print(datetime.datetime.now())

# print the current year
# print(datetime.datetime.now().year)

# print the current month
# print(datetime.datetime.now().month)

# print the current day
# print(datetime.datetime.now().day)


# print Start Date and end of Date 
# print(datetime.datetime.min)
# print(datetime.datetime.max)


# time #
# print the current time 
# print(datetime.datetime.now().time()) 

# print the current time Hour 
# print(datetime.datetime.now().time().hour) 

# print the current time minute 
# print(datetime.datetime.now().time().minute)

# print the current time second
# print(datetime.datetime.now().time().second)

# print Start Date and end of time
# print(datetime.time.min)
# print(datetime.time.max)


# print specific time 
# print(datetime.datetime(1878)) # this error should be year month day 
# print(datetime.datetime(1998,5,23))
# print(datetime.datetime(1872,1,20,14,50,30))

### Birthday applications ### 

# MyBirthday = datetime.datetime(2002, 3 , 21)
# today = datetime.datetime.now() 

# print(f"my birthday is :{MyBirthday}")
# print(f"date now is : {today}")

# print(f"I lived for {today - MyBirthday}  ")
# print(f"I lived for {(today - MyBirthday).days} days")

print("*"*40)



# ---------------------------
# Date and time => format date 
# ---------------------------
# pythons strftime directive 

# myBirthday = datetime.datetime(2001 ,3  , 21)

# print(myBirthday.strftime("%Y-%m-%d"))
# print(myBirthday.strftime("%A"))
# print(myBirthday.strftime("%B")) 
# print(myBirthday.strftime("%Y/%B/%d"))


# %a	لإظهار إسم اليوم بشكل مختصر، مثل: Mon


# %A	لإظهار إسم اليوم بشكل كامل، مثل: Monday


# %w	لإظهار رقم اليوم بالنسبة للأسبوع مع الإشارة إلى أن أول يوم في الأسبوع يُعتبر يوم الأحد ( Sunday ) و هو يساوي 0، و آخر يوم في الأسبوع هو يوم السبت ( Saturday ) و هو يساوي 6، مثل: 1


# %d	لإظهار رقم اليوم بالنسبة للشهر مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 01 و 31، مثل: 03


# %b	لإظهار إسم الشهر بشكل مختصر، مثل: Dec


# %B	لإظهار إسم الشهر كاملاَ، مثل: December


# %m	لإظهار رقم الشهر بالنسبة للسنة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 01 و 12، مثل: 12


# %y	لإظهار رقم السنة بشكل مختصر، أي لإظهار أول رقمين منها فقط، مثل: 18


# %Y	لإظهار رقم السنة، مثل: 2018


# %H	لإظهار رقم الساعة بنظام 24 ساعة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 23، مثل: 14


# %I	لإظهار رقم الساعة بنظام 12 ساعة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 11، مثل: 2


# %p	لإظهار الكلمة AM إذا كان الوقت قبل الساعة 12 نهاراً و لإظهار الكلمة PM إذا كان الوقت بعدها.


# %M	لإظهار رقم الدقيقة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 59، مثل: 24


# %S	لإظهار رقم الثانية مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 59، مثل: 09


# %f	لإظهار أجزاء الثانية بالمايكرو ثانية ( Microsecond )، أي لإظهار الثانية الواحدة كمليون جزء مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 000000 و 999999، مثل: 034208


# %j	لإظهار رقم اليوم بالنسبة للسنة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 001 و 366، مثل: 337


# %U
# لإظهار رقم الأسبوع بالنسبة للسنة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 53 و أول يوم في كل أسبوع هو يوم الأحد ( Sunday )، مثل: 48


# %W	لإظهار رقم الأسبوع بالنسبة للسنة مع الأخذ بالإعتبار أن هذا الرقم سيكون ضمن النطاق 00 و 53 و أول يوم في كل أسبوع هو يوم الإثنين ( Monday )، مثل: 49


# %c	لإظهار التاريخ و الوقت الحالي بشكل كامل، مثل: Mon Dec 3 18:52:05 2018


# %x	لإظهار التاريخ الحالي بشكل كامل، مثل: 12/03/18


# %X	لإظهار الوقت الحالي بشكل كامل، مثل: 18:52:05
