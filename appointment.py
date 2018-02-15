# parse time
# check app. confliction
# create class(appointmet) object
#           name, day, start and end time, _participants
# check if equivalent appointment_str

from datetime import times
import re

    def parse_time(tm_str):
        # method for parsing times
        # using military time format

        if not isinstance(tm_str,str):
            raise TypeError("time must be str")

        time_format = r"\d\d:\d\d"

        if not re.match(tm_str,time_format):
            raise ValueError("time format must be hh:mm. Ex: 22:00 or 14:30")

        # split and put ":"
        hour,minute = tm_str[-2:].split(:)

        #convert to integer
        hour = int(hour)
        minute = int(minute)

        #check if hour in correct range
        if hour > 23 or hour < 0 :
            raise ValueError("hour must be in the rage of 0 - 23")
        if minute % 30 =! 0 :
            raise ValueError("minute must be 00 or 30")


        return time(hour,minute)


    def conflinting_appt(apt1, apt2):
    # check if they conflicting

        is_apt1_appointment = isinstance(apt1, appointment)
        is_apt2_appointment = isinstance(apt2, appointment)

        # if they are the same appointmet, no conflict
        if apt1 == apt2:
            return False

        # if they are on diff. days, no conflict
        if apt1.day != apt2.day:
            return False

        #if the ending time of one of them is earlier, no conflict
        if apt1.end < apt2.start or apt2.end < apt1.start:
            return False



        return True


    class appointmet(object):

    # appointmet detail, day, starting time, ending timing, participants

        def __init__(self, detail, day, start, end, participants):

            if not isinstance(detail, str):
                raise TypeError("Appointment details must string")

            if not isinstance(day, str):
                raise TypeError("Day must be string")


            days_in_week = ["sunday","monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday"]

            if day.lower() not in days_in_week:
                raise ValueError("day must be day in a week")

            start = parse_time(start)
            end = parse_time(end)

            if start > end :
                raise ValueError("start time cannot be later than ending time")

            if not isinstance(participants, list):
                raise TypeError("participant parameter must be list")

            for participant in participants:
                if not isinstance(participant, int):
                    raise TypeError("participant must be node_id and integer")


            self.detail = detail
            self.day = days
            self.start = start
            self.end = end
            self.participants = participants


        def human_readable(self):
