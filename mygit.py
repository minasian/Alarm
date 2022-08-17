def check_input(alarm_time):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if alarm_time[0] and alarm_time[1] and alarm_time[3] and alarm_time[4] not in nums:
        print('Wrong format of digits')
    elif int(alarm_time[0:2]) > 23 or int(alarm_time[0:2]) < 0 \
        or int(alarm_time[3:5]) > 59 or int(alarm_time[3:5]) < 0:
        print("Wrong time format")
        exit()
    return alarm_time
    
alarm_time = check_input(input("Please input alarm time with the follow format 'hh:mm': "))

