def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60.0
def main():
    time_str = input("What time is it? ").strip()
    hours = convert(time_str)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")
main()