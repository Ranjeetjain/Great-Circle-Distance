import math, random

DEGREES_IN_RADIAN = 57.2958
MEAN_EARTH_RADIUS_KM = 6371

# https://medium.com/@petehouston/calculate-distance-of-two-locations-on-earth-using-python-1501b1944d97
class GreatCircle(object):
    def __init__(self):

        self.latitude1_degrees = 0
        self.longitude1_degrees = 0
        self.latitude1_radians = 0
        self.longitude1_radians = 0

        self.latitude2_degrees = 0
        self.longitude2_degrees = 0
        self.latitude2_radians = 0
        self.longitude2_radians = 0

        self.central_angle_radians = 0
        self.distance_kilometres = 0
        self.error = None

    def calculate(self):
        """
        Validate the given latitude and logitude and calcute the distance.
        """

        self.__validate_degrees()

        if not self.error:
            self.__calculate_radians()
            self.__calculate_central_angle()
            self.__calculate_distance()
        else:
            return self.error

    def __validate_degrees(self):
        """
        Check latitudes and longitudes are within valid ranges.
        """

        if self.latitude1_degrees < -90.0 or self.latitude1_degrees > 90.0:
            self.error = "Invalid latitude1_degrees"
            return

        if self.longitude1_degrees < -180.0 or self.longitude1_degrees > 180.0:
            self.error = "Invalid longitude1_degrees"
            return

        if self.latitude2_degrees < -90.0 or self.latitude2_degrees > 90.0:
            self.error = "Invalid latitude2_degrees"
            return

        if self.longitude2_degrees < -180.0 or self.longitude2_degrees > 180.0:
            self.error = "Invalid longitude2_degrees"
            return

    def __calculate_radians(self):
        """
        Calculate radians from degrees by dividing by constant.
        """

        self.latitude1_radians = self.latitude1_degrees / DEGREES_IN_RADIAN
        self.longitude1_radians = self.longitude1_degrees / DEGREES_IN_RADIAN

        self.latitude2_radians = self.latitude2_degrees / DEGREES_IN_RADIAN
        self.longitude2_radians = self.longitude2_degrees / DEGREES_IN_RADIAN

    def __calculate_central_angle(self):
        if self.longitude1_radians > self.longitude2_radians:
            longitudes_abs_diff = self.longitude1_radians - self.longitude2_radians
        else:
            longitudes_abs_diff = self.longitude2_radians - self.longitude1_radians

        self.central_angle_radians = math.acos( math.sin(self.latitude1_radians)
                                         * math.sin(self.latitude2_radians)
                                         + math.cos(self.latitude1_radians)
                                         * math.cos(self.latitude2_radians)
                                         * math.cos(longitudes_abs_diff))

    def __calculate_distance(self):
        """
        Multiply central angle with earth's mean radius
        """
        self.distance_kilometres = round(MEAN_EARTH_RADIUS_KM * self.central_angle_radians, 3)
