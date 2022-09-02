#This app checks to see if you heart rate is too low or too high

heart_rate = 120

too_low = 60
too_high = 100

if heart_rate < too_low:
    print('Your heart rate is too low!')

elif heart_rate > too_high:
    print('Your heart rate is too high!')

else:
    print('Your heart rate is fine!')


