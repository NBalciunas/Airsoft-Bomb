import RPi.GPIO as GPIO
import i2c_lcd
from time import sleep, perf_counter
import time
from random import choice

# RPi setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Button setup
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Blue / Planter
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Yellow / Defuser

# LCD setup
lcd = i2c_lcd.lcd()

# Keypad setup
length = 6
col = [19, 13, 6, 5]
row = [21, 20, 16, 26]

for j in range(4):
    GPIO.setup(col[j], GPIO.OUT)
    GPIO.output(col[j], 1)
for i in range(4):
    GPIO.setup(row[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Checks
code_check = True
timer_check = True
check_if_alive = True

# Customizable variables
amount_of_tries = 3
decoder_amount = 16


# Password checker // Password guesser
def check_keypad(length):

    global code_check
    global amount_of_tries

    col = [19, 13, 6, 5]
    row = [21, 20, 16, 26]

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    result = ""

    while code_check:
        for j in range(4):
            GPIO.output(col[j], 0)

            timer()
            if GPIO.input(27) == GPIO.HIGH:
                amount_of_tries = amount_of_tries + 1
                code_check = False
                break

            if not check_if_alive:
                code_check = False
                break

            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    time.sleep(0.02)
                    result = result + matrix[i][j]
                    lcd.lcd_display_string("         ", 2)
                    lcd.lcd_display_string(result, 2)
                    while GPIO.input(row[i]) == 0:
                        time.sleep(0.02)

            GPIO.output(col[j], 1)
            if len(result) >= length:
                print("Tried - " + result)
                return result


# Start sequence // Password maker
def starter():

    global password
    global time_for_defusing
    x = 0

    lcd.lcd_display_string("Starting...", 1)
    sleep(5)

    lcd.lcd_clear()
    lcd.lcd_display_string("Input a time", 1)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    passwordmaker = ""
    timemaker = ""

    while x != 1:
        while GPIO.input(17) == GPIO.HIGH:
            if len(timemaker) == 3:
                lcd.lcd_display_string(timemaker, 2)
                time_for_defusing = int(timemaker)
                print("Time - " + timemaker)
                x = 1
                break
            lcd.lcd_display_string(timemaker, 2)
            for j in range(4):
                GPIO.output(col[j], 0)

                for i in range(4):
                    if GPIO.input(row[i]) == 0:
                        time.sleep(0.02)
                        if matrix[i][j] == "0" or matrix[i][j] == "1" or matrix[i][j] == "2" or matrix[i][j] == "3" or matrix[i][j] == "4" or matrix[i][j] == "5" or matrix[i][j] == "6" or matrix[i][j] == "7" or matrix[i][j] == "8" or matrix[i][j] == "9":
                            timemaker = timemaker + matrix[i][j]
                            if timemaker == "000":
                                lcd.lcd_display_string(timemaker, 2)
                                sleep(0.4)
                                timemaker = ""
                                lcd.lcd_display_string("      ", 2)
                        while GPIO.input(row[i]) == 0:
                            time.sleep(0.02)
                GPIO.output(col[j], 1)
            if GPIO.input(17) == GPIO.LOW:
                timemaker = ""
                lcd.lcd_display_string("      ", 2)

    sleep(0.5)
    lcd.lcd_clear()
    lcd.lcd_display_string("Time set to :" + str(time_for_defusing), 1)
    sleep(2)
    lcd.lcd_clear()
    lcd.lcd_display_string("Input a password", 1)

    while x != 2:
        while GPIO.input(17) == GPIO.HIGH:
            if len(passwordmaker) == 6:
                lcd.lcd_display_string(passwordmaker, 2)
                password = passwordmaker
                print("Password - " + password)
                x = 2
                break
            lcd.lcd_display_string(passwordmaker, 2)
            for j in range(4):
                GPIO.output(col[j], 0)

                for i in range(4):
                    if GPIO.input(row[i]) == 0:
                        time.sleep(0.02)
                        passwordmaker = passwordmaker + matrix[i][j]
                        while GPIO.input(row[i]) == 0:
                            time.sleep(0.02)
                GPIO.output(col[j], 1)
            if GPIO.input(17) == GPIO.LOW:
                passwordmaker = ""
                lcd.lcd_display_string("      ", 2)

    sleep(0.5)
    lcd.lcd_clear()
    lcd.lcd_display_string("Initiating", 1)
    lcd.lcd_display_string("startup sequence", 2)
    sleep(2)
    lcd.lcd_clear()
    sleep(0.5)


# Timer
def timer():

    global check_if_alive

    if check_if_alive:
        time_now = perf_counter()
        timer_real = time_now - timer_start
        timer_rounded = round(timer_real)
        timer_on_screen = time_for_defusing - timer_rounded
        if timer_on_screen < 10:
            timer_on_screen = str(timer_on_screen) + " "
        lcd.lcd_display_string(str(timer_on_screen), 1)
        if timer_real > time_for_defusing:
            check_if_alive = False
            lcd.lcd_clear()
            lcd.lcd_display_string("Boom!", 1)


# Code way
def code():

    global check_if_alive
    global amount_of_tries
    y2 = 0

    # Password from keypad
    amount_of_tries_str = str(amount_of_tries)
    text = "(" + amount_of_tries_str + " / 3)"
    lcd.lcd_display_string(str(text), 2)
    result = check_keypad(length)
    amount_of_tries = amount_of_tries - 1

    # Password check
    if result == password:
        y2 = 1

    # Correct password
    if y2 == 1:
        check_if_alive = False
        lcd.lcd_clear()
        lcd.lcd_display_string("Deactivated", 1)

    # Incorrect password
    elif amount_of_tries == 0 & y2 == 0:
        check_if_alive = False
        lcd.lcd_clear()
        lcd.lcd_display_string("Boom!", 1)


# Decoder Way
def decoder():
    while GPIO.input(27) == GPIO.HIGH:

        global check_something_x
        global something_x
        global amount

        something = choice("0123456789ABCD*#")

        if check_something_x:
            something_x = ""
            amount = 0
            check_something_x = False

        something_x = something_x + something
        lcd.lcd_display_string(something_x, 2)

        col = [19, 13, 6, 5]
        row = [21, 20, 16, 26]

        matrix = [["1", "2", "3", "A"],
                  ["4", "5", "6", "B"],
                  ["7", "8", "9", "C"],
                  ["*", "0", "#", "D"]]

        while True:
            for j in range(4):
                GPIO.output(col[j], 0)
                timer()
                for i in range(4):
                    if GPIO.input(row[i]) == 0:
                        time.sleep(0.02)
                        if matrix[i][j] == something:
                            amount = amount + 1
                            return
                        while GPIO.input(row[i]) == 0:
                            time.sleep(0.02)
                GPIO.output(col[j], 1)


# Stuff
starter()
timer_start = perf_counter()

while True:

    if check_if_alive:
        if code_check:
            timer()
            code()
        if GPIO.input(27) == GPIO.HIGH:
            code_check = False
            lcd.lcd_clear()
            lcd.lcd_display_string("Decoder starting", 2)
            sleep(1)
            check_something_x = True
            decoder_check = False
            amount = 0
            lcd.lcd_display_string("                ", 2)
            while True:
                timer()
                decoder()
                if amount == decoder_amount:
                    decoder_check = True
                    break
                if not check_if_alive:
                    break
            if decoder_check:
                check_if_alive = False
                lcd.lcd_clear()
                lcd.lcd_display_string("Deactivated", 1)
                break
        if not check_if_alive:
            break

#  Closing procedures
print("Finished")
sleep(10)
lcd.lcd_display_string(":^)", 2)
