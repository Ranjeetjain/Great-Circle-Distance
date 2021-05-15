from great_circle_distance import GreatCircle


user_lat = 14.565443
user_long = 121.027535
DISTANCE_RANGE = 10 # change value for long range

def main():
    """
    Compare the given lat long with the data available.
    """
    result = []

    gc = GreatCircle()
    gc.latitude1_degrees = user_lat
    gc.longitude1_degrees = user_long
    # list of zomato restaurants with lat and long details
    with open('zomato-min.csv') as f:
        lines = [line.split(',') for line in f]

        for restaurant in lines[1:]:
            gc.longitude2_degrees = float(restaurant[1])
            gc.latitude2_degrees = float(restaurant[2])
            gc.calculate()
            # if distance is less than or eq to given range
            if not gc.distance_kilometres == 0 and gc.distance_kilometres <= DISTANCE_RANGE:
                result.append([restaurant[0], gc.distance_kilometres])

    if not result:
        print("No Restaurants present within the range of " + str(DISTANCE_RANGE) + " KM")
        return

    # sorting the list
    sorted(result,key = lambda x:x[1])
    for res in result:
        print(res[0] + " is " + str(res[1]) + " KM far from your location")

if __name__ == "__main__":
    main()