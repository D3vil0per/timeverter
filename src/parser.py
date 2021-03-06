import argparse
from src.util import ParseDataArgs

def arg_parse():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-c", "--colored", action='store_true', help="let's give some random colored output")
    parser.add_argument("-d", "--data", help="insert params for GET or POST request", action=ParseDataArgs)
    parser.add_argument("-D", "--date", help="convert a date to epoch time format")
    parser.add_argument("-div", "--divide", type=int, help="divide the timestamp by the specified value (used for change the order of magnitude)")
    parser.add_argument("-e", "--encode", help="encode the input to a chain of the specified formats. It will be applied before the --algorithm option")
    parser.add_argument("-E", "--epoch", type=int, help="convert epoch time to date format")
    parser.add_argument("-f", "--float", type=float, help="deal timestamp as floating point number and specify the floating step value when range option is set")
    parser.add_argument("-fr", "--filterregex", help="filter the response for the submitted regex")
    parser.add_argument("-g", "--algorithm", help="specify the algorithm to be used for token computation (look for hashlib or OpenSSL algorithms)")
    parser.add_argument("-h", "--help", action='store_true', help="show this help message and exit")
    parser.add_argument('-H', '--header', action='append', help="specify the headers of the request")
    parser.add_argument("-mr", "--matchregex", help="match the response for the submitted regex")
    parser.add_argument("-mul", "--multiply", type=int, help="multiply the timestamp by the specified value (used for change the order of magnitude)")
    parser.add_argument("-n", "--now", action='store_true', help="show current local time as epoch and date format")
    parser.add_argument("-p", "--prefix", default="", help="specify a prefix string before the timestamp")
    parser.add_argument("-r", "--range", type=int, default=0, help="specify a +- offset value of the timestamp in seconds (or other magnitudes according -div and -mul options)")
    parser.add_argument("-s", "--suffix", default="", help="specify a suffix string after the timestamp")
    parser.add_argument("-u", "--url", help="specify the url")
    parser.add_argument("-U", "--utc", choices=["-12:00", "-11:00", "-10:00", "-9:30", "-9:00", "-8:00", "-7:00", "-6:00", "-5:00", "-4:00", "-3:30", "-3:00", "-2:00", "-1:00", "-0:00", "+0:00", "+1:00", "+2:00", "+3:00", "+3:30", "+4:00", "+4:30", "+5:00", "+5:30", "+5:45", "+6:00", "+6:30", "+7:00", "+8:00", "+8:45", "+9:00", "+9:30", "+10:00", "+10:30", "+11:00", "+12:00", "+12:45", "+13:00", "+14:00"], help="show current UTC+N time as epoch and date format")
    parser.add_argument("-v", "--verbose", action='store_true', help="show verbose output")
    parser.add_argument("-V", "--version", action='store_true', help="show version information")
    parser.add_argument("-X", "--request", choices=["GET", "POST"], help="specify request method to use")
    parser.add_argument("-z", "--compare", help="compare a value to the output tokens")

    args = parser.parse_args()
    return args
