# parse time
# check app. confliction
# create class(appointmet) object
#           name, day, start and end time, _participants
# check if equivalent appointment_str

from datetime import time
import re

def parse_time(tm_str):
    # method for parsing times
    # using military time format

    if not isinstance(tm_str,str):
        raise TypeError("time must be str")

    time_format = r"\d\d:\d\d"

    if not re.match(time_format,tm_str):
        raise ValueError("time format must be hh:mm. Ex: 22:00 or 14:30")

    # split into two from ":"
    hour, minute = tm_str.split(":")
    #convert to integer
    hour = int(hour)
    minute = int(minute)

    #check if hour in correct range
    if hour > 23 or hour < 0 :
        raise ValueError("hour must be in the rage of 0 - 23")
    if minute % 30 != 0 :
        raise ValueError("minute must be 00 or 30")


    return time(hour,minute)


def conflicting_appt(apt1, apt2):
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


class appointment(object):

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
            self.day = day
            self.start = start
            self.end = end
            self.participants = participants

        def __eq__(self, other):

            other_detail = self.detail == other.detail
            other_day = self.day == other.days
            other_start = self.start == other.start
            other_end = self.end == other.end

            set_intrsctn = set(self.participants) & set(other.participants)
            set_union = set(self.participants) | set(other.participants)

            other_participants = len(union) == len(intersection)

            return other_detail and other_day and other_start and other_end and other_participants

        def __str__(self):
            # human readable form of the appointment
            appointment_str = "Appointment \"" + self.detail + "\" on "
            appointment_str += self.day[0].upper() + self.day[1:] + " from "
            appointment_str += str(self.start)[:-3] + " to " + str(self.end)[:-3]
            appointment_str += " with "

            if len(self.participants) > 2:
                appointment_str += "".join(
                    [str(i) + ", " for i in self.participants[:-1]])
                appointment_str += "and " + str(self.participants[-1])
            elif len(self.participants) == 2:
                appointment_str += str(self.participants[0]) + " and "
                appointment_str += str(self.participants[1])
            else:
                appointment_str += str(self.participants[0])

            return appointment_str

        def __repr__(self):
            return self.__str__()

def main():


    test1 = appointment("Meeting with Mike","Monday","10:00","10:30", [1, 2, 3, 4])

    test2 = appointment("Lunch w/ my boyz","Tuesday","12:00","13:00", [1, 5, 6])


    print test2.__repr__()

if __name__ == "__main__":
    main()
