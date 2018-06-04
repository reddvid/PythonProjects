# This is a simple app to compute ETA of my Vape's charging time
print("############################################################")
print("This is a sample app to compute ETA of battery charging time")
print("############################################################")
time = 0
timemin = 0000
timemax = 2359
hrsmax = 23
minmax = 59

while True:
    try:
        time = int(input("Enter charge start time in 24-hour format (HHMM): "))
        tostring = str(time)
        if time > timemin and time < timemax and len(tostring) == 4 and int(tostring[2:]) <= minmax:
            break
    except ValueError:
        print("Sorry, I didn't understand that.")
        # better try again... Return to the start of the loop
        continue
    else:
        print("Sorry, that's beyond normal Earth time.")
        # better try again... Return to the start of the loop
        continue

print("Start time " + tostring[:2] + ":" + tostring[2:])

# Add 3 hours and 12 minutes
hrs = int(tostring[:2], 10) + 3  # get the first 2 digits
mins = int(tostring[2:], 10) + 12  # get last two digits

if mins > 60:
    hrs = hrs + 1
    mins = mins - 60
    
if hrs > 24:
    hrs = hrs - 24

print("Estimated time to full-charge 2x3200mAh batteries using 2A charger: " +
      str(hrs) + ":" + str(mins))
