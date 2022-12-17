# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
import this
import time
import math
import datetime
import sys
import greet


def wait(seconds):
    print(time.asctime())
    time.sleep(seconds)
    print(time.asctime())
    return


def my_sin(value):
    sin = math.sin(value)
    return sin


def iso_now():
    now = datetime.datetime.now()  # Get the time and date of this exact moment
    # Transform into ISO 8601 format with a T between date and time(ending with full minutes)
    result = now.isoformat("T", "minutes")
    return result


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    result = greet.supergreeting(name)
    return result
