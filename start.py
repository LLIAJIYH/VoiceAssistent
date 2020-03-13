import tests
import time
import datetime


now = datetime.datetime.now()

if now.hour >= 6 and now.hour < 12:
    tests.say("Доброе утро, Байрам!")
elif now.hour >= 12 and now.hour < 18:
    tests.say("Добрый день, Байрам!")
elif now.hour >= 18 and now.hour < 23:
    tests.say("Добрый вечер, Байрам!")
else:
    tests.say("Доброй ночи, Байрам!")

tests.start()