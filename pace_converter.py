import math

def mins_per_uno_mile_calculator(distance, time):
    mins_per_mile_decimal = time/(distance/1.609) # decimal time
    mins = math.floor(mins_per_mile_decimal) # mins
    decimal_secs = mins_per_mile_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)/100 # secs
    mins_per_mile = mins + secs
    mins_per_mile = mins_per_mile 
    mins_per_mile_float = "{:.2f}".format(mins_per_mile)
    mins_per_mile_float = str(mins_per_mile_float).replace(".",":")
    return mins_per_mile_float 

def mins_per_marathon_calculator(distance, time):

    mins_per_marathon_decimal = time/distance # decimal time
    mins_per_marathon = mins_per_marathon_decimal * 42.195

    hours = math.floor(mins_per_marathon / 60)
    mins_decimal = mins_per_marathon - (hours * 60) #math.floor(mins_per_marathon_decimal) # mins
    mins = math.floor(mins_decimal) # mins
    decimal_secs = mins_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)#/100 # secs
    mins_per_marathon = hours + mins + secs
    # print("hours", hours)
    # print("mins", mins)
    # print("secs", secs)
    # print("mins_marathon",mins_per_marathon)
    secs = int(secs)
    # mins_per_marathon_float = "{:.2f}".format(mins_per_marathon)
    # mins_per_marathon_float = str(mins_per_marathon_float).replace(".",":")

    #return mins_per_marathon_float 

    # if mins_per_marathon > 60:
    #     hours = math.floor(mins_per_marathon / 60)
    #     mins_n_secs = mins_per_marathon % 60
    #     secs_decimal, mins = math.modf(mins_n_secs)
    #     mins = int(mins)
    #     secs = secs_decimal * 60
    #     secs = int(secs)

    return hours, mins, secs

def mins_per_half_marathon_calculator(distance, time):
    mins_per_half_marathon_decimal = time/distance # decimal time
    mins_per_half_marathon = mins_per_half_marathon_decimal * 21.098

    hours = math.floor(mins_per_half_marathon / 60)
    mins_decimal = mins_per_half_marathon - (hours * 60) #math.floor(mins_per_marathon_decimal) # mins
    mins = math.floor(mins_decimal) # mins
    decimal_secs = mins_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)#/100 # secs
    mins_per_half_marathon = hours + mins + secs

    secs = int(secs)
    # mins_per_half_marathon_float = "{:.2f}".format(mins_per_half_marathon)
    # mins_per_half_marathon_float = str(mins_per_half_marathon_float).replace(".",":")

    #return mins_per_half_marathon_float 

    #mins_per_marathon_float = "{:.2f}".format(mins_per_marathon)
    #return mins_per_marathon_float 

    # if mins_per__half_marathon > 60:
    #     hours = math.floor(mins_per__half_marathon / 60)
    #     mins_n_secs = mins_per__half_marathon % 60
    #     secs_decimal, mins = math.modf(mins_n_secs)
    #     mins = int(mins)
    #     secs = secs_decimal * 60
    #     secs = round(secs)
        
    #     # print("hours",hours)
    #     # print("mins",mins)
    #     # print("secs",secs)

    return hours, mins, secs

def mins_per_10_km_calculator(distance, time):
    mins_per_km_decimal = time/distance # decimal time
    mins_per_10_km_decimal = mins_per_km_decimal * 10
    mins = math.floor(mins_per_10_km_decimal) # mins
    decimal_secs = mins_per_10_km_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)/100 # secs
    mins_per_10_km = mins + secs
    mins_per_10_km_float = "{:.2f}".format(mins_per_10_km)
    mins_per_10_km_float = str(mins_per_10_km_float).replace(".",":")
    return mins_per_10_km_float 

def mins_per_5_km_calculator(distance, time):
    mins_per_km_decimal = time/distance # decimal time
    mins_per_5_km_decimal = mins_per_km_decimal * 5
    mins = math.floor(mins_per_5_km_decimal) # mins
    decimal_secs = mins_per_5_km_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)/100 # secs
    mins_per_5_km = mins + secs
    mins_per_5_km_float = "{:.2f}".format(mins_per_5_km)
    mins_per_5_km_float = str(mins_per_5_km_float).replace(".",":")
    return mins_per_5_km_float 

def mins_per_uno_km_calculator(distance, time):
    mins_per_km_decimal = time/distance # decimal time
    mins = math.floor(mins_per_km_decimal) # mins
    decimal_secs = mins_per_km_decimal - mins # secs (decimal)
    secs = (decimal_secs * 60)/100 # secs
    mins_per_km = mins + secs
    mins_per_km_float = "{:.2f}".format(mins_per_km)
    mins_per_km_float = str(mins_per_km_float).replace(".",":")
    return mins_per_km_float

def mins_per_400m_calculator(distance, time):
    mins_per_km_decimal = time/distance # decimal time
    mins_per_400m = mins_per_km_decimal * .4
    secs = math.floor(mins_per_400m) # secs
    decimal_secs = mins_per_400m - secs # millisecs (decimal)
    milsecs = (decimal_secs * 60)/100 # secs
    mins_per_400m = secs + milsecs
    mins_per_400m_float = "{:.2f}".format(mins_per_400m)
    mins_per_400m_float = str(mins_per_400m_float).replace(".",":")
    return mins_per_400m_float

def mins_per_100m_calculator(distance, time):
    mins_per_km_decimal = time/distance # decimal time
    mins_per_200m = mins_per_km_decimal * .1
    secs = math.floor(mins_per_200m) # secs
    decimal_secs = mins_per_200m - secs # millisecs (decimal)
    milsecs = (decimal_secs * 60)/100 # secs
    mins_per_200m = secs + milsecs
    mins_per_200m_float = "{:.2f}".format(mins_per_200m)
    mins_per_200m_float = str(mins_per_200m_float).replace(".",":")
    return mins_per_200m_float

def kmph_calculator(distance, time):
    time_hour = time / 60
    speed = distance/time_hour
    speed_float = "{:.2f}".format(speed)
    return speed_float

def mph_calculator(distance, time):
    time_hour = time / 60
    distance_mile = distance / 1.609
    speed = distance_mile/time_hour
    speed_float = "{:.2f}".format(speed)
    return speed_float


if __name__ == '__main__':
    print('Enter distance (km):')
    distance = input()
    distance = float(distance)
    # print('Enter Time (min):')
    #time = int(input())#.split(":"))

    print('Enter Time Taken (min sec):')
    min, *sec = input().split()
    sec = next(iter(sec), 0) # default value if sec not defined
    # print("min: ",min)
    # print("sec: ",sec)
    min = int(min)
    sec = int(sec)
    if sec > 60:
        print("Enter secs less than 60:")
        min, sec = input().split()
    min = int(min)
    sec = int(sec)/60
    time = min + (sec) 
    print('')
    #print(time)

    ''' 
    # For Python 3.10 or newer
    print("Please Choose Function:")
    print("1. All Data")
    print("2. Average Running Speed")

    data = int(input("Option:"))

    match data:

        case 1:'''

    kmph_calculator(distance, time)
    print("Speed: ", kmph_calculator(distance,time), ' km/h')

    mph_calculator(distance, time)
    print("Speed: ", mph_calculator(distance,time), ' mph')

    mins_per_100m_calculator(distance, time)
    print('100m: ', mins_per_100m_calculator(distance,time), ' secs')

    mins_per_400m_calculator(distance, time)
    print('400m: ', mins_per_400m_calculator(distance,time), ' secs')

    mins_per_uno_km_calculator(distance, time)
    print('1km: ', mins_per_uno_km_calculator(distance,time), ' mins')

    mins_per_5_km_calculator(distance, time)
    print('5km: ', mins_per_5_km_calculator(distance,time), ' mins')

    mins_per_10_km_calculator(distance, time)
    print('10km: ', mins_per_10_km_calculator(distance,time), ' mins')
    
    mins_per_half_marathon_calculator(distance, time)
    #print('Half Marathon: ', mins_per_half_marathon_calculator(distance,time), 'hrs:min:secs')
    print('Half Marathon: {}:{}:{}, hrs:min:secs'.format(mins_per_half_marathon_calculator(distance,time)[0], mins_per_half_marathon_calculator(distance,time)[1], mins_per_half_marathon_calculator(distance,time)[2]))
    #print('Half marathon: ', mins_per_half_marathon_calculator(distance,time)[0], ' hours',mins_per_half_marathon_calculator(distance,time)[1],' mins',mins_per_half_marathon_calculator(distance,time)[2],' seconds')

    mins_per_marathon_calculator(distance, time)
    #print('Marathon: ', mins_per_marathon_calculator(distance,time), 'hrs:min:secs')
    print('Marathon: ', str(mins_per_marathon_calculator(distance,time)[0]) + ':'+ str(mins_per_marathon_calculator(distance,time)[1]) + ':' + str(mins_per_marathon_calculator(distance,time)[2]), 'hrs:min:secs')

    mins_per_uno_mile_calculator(distance, time)
    print('1 Mile: ', mins_per_uno_mile_calculator(distance,time), ' mins')

    #input("what else?") # so can read the time 

