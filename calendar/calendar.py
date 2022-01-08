#!/usr/bin/python3

import random

"""
A bunch of constants up here. Feel free to change the names of the days or
months to match your worlds.
"""

SUNDAY = "Sunday"
MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
SATURDAY = "Saturday"
DAYS_OF_WEEK = [
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
]

DAYS_IN_MONTH = 30
MONTHS_IN_YEAR = 12

JANUARY = "January"
FEBRUARY = "February"
MARCH = "March"
APRIL = "April"
MAY = "May"
JUNE = "June"
JULY = "July"
AUGUST = "August"
SEPTEMBER = "September"
OCTOBER = "October"
NOVEMBER = "November"
DECEMBER = "December"

MONTHS_OF_YEAR = [
    JANUARY,
    FEBRUARY,
    MARCH,
    APRIL,
    MAY,
    JUNE,
    JULY,
    AUGUST,
    SEPTEMBER,
    OCTOBER,
    NOVEMBER,
    DECEMBER
]

SPRING = "Spring"
SUMMER = "Summer"
AUTUMN = "Autumn"
WINTER = "Winter"

SEASONS_IN_YEAR = [
    SPRING,
    SUMMER,
    AUTUMN,
    WINTER
]

MONTH_SEASON_MAP = {
    JANUARY: WINTER,
    FEBRUARY: WINTER,
    MARCH: SPRING,
    APRIL: SPRING,
    MAY: SPRING,
    JUNE: SUMMER,
    JULY: SUMMER,
    AUGUST: SUMMER,
    SEPTEMBER: AUTUMN,
    OCTOBER: AUTUMN,
    NOVEMBER: AUTUMN,
    DECEMBER: WINTER
}

# Fields in a day dictionary
FIELD_YEAR  = "Year"
FIELD_DAY = "Day"
FIELD_MONTH = "Month"
FIELD_MONTH_DAY = "Month Day"
FIELD_YEAR_DAY = "Year Day"
FIELD_TEMPERATURE = "Temperature"
FIELD_WEATHER = "Today's Weather"
FIELD_SEASON = "Season"
FIELD_NEWS = "News"
FIELD_HOLIDAY = "Holday"

# Some temperature constants
SEASON_TEMP_MIN = {
    SPRING: 0,
    SUMMER: 30,
    AUTUMN: -10,
    WINTER: -25
}
SEASON_TEMP_MAX = {
    SPRING: 75,
    SUMMER: 110,
    AUTUMN: 65,
    WINTER: 40
}


# Some weather constants
FREEZING_TEMPERATURE = 32

# Represents 1 in X chance for precipitation
SEASON_PRECIPITATION_DICE = {
    SPRING: 4,
    SUMMER: 8,
    AUTUMN: 12,
    WINTER: 20
}

# Change these for your world
HOLIDAYS = dict([
    (171, "Summer Solstice"),
    (262, "Equinox"),
    (340, "Day of darkness"),
    (351, "Winter Solstice"),
    (300, "Devils night"),
    (182, "Day of honor"),
    (1, "New Year day"),
    (360, "New Year eve"),
    (257, "Harvest day")
])

# one in an X chance for event to happen
EVENT_LIKELIHOOD = dict([
    ("Assassination", 100),
    ("Political Gaffe", 100),
    ("Major Crime", 100),
    ("Blood Moon", 100),
    ("Blue Moon", 100),
    ("Strange Meteor", 200),
    ("Deity visit", 200),
    ("Attacked Village", 100)
])

ERA = "Age of the Human"
START_YEAR = 325
START_DAY = 0 # Uses days in year, zero indexed
DAYS_TO_CALCULATE = 720


def get_temperature(day):
    season = day[FIELD_SEASON]
    temp_min = SEASON_TEMP_MIN[season]
    temp_max = SEASON_TEMP_MAX[season]
    # Roll two numbers to get bell curve
    temp_die = abs(int((temp_max - temp_min) / 2))
    temp_roll = random.randint(1, temp_die)
    temp_roll += random.randint(1, temp_die)

    return  temp_roll + temp_min

def get_weather(day):
    season = day[FIELD_SEASON]
    temp = day[FIELD_TEMPERATURE]
    precipitation_die = SEASON_PRECIPITATION_DICE[season]
    precipitation_roll = random.randint(1, precipitation_die)
    precipitation = precipitation_roll == 1
    overcast = precipitation_roll < precipitation_die/4
    freezing = temp <= FREEZING_TEMPERATURE
    if precipitation:
        if freezing:
            return "snowy"
        else:
            return "rainy"
    else:
        if overcast:
            return "overcast"
        else:
            return "sunny"


def get_day_of_week(day_in_year):
    day_number = day_in_year %  len(DAYS_OF_WEEK)
    return DAYS_OF_WEEK[day_number]

def get_month_in_year(day_in_year):
    month_number = int(day_in_year / DAYS_IN_MONTH)
    return MONTHS_OF_YEAR[month_number]

def get_day_of_month(day_in_year):
    return 1 + day_in_year % DAYS_IN_MONTH
    
def get_season(day_in_year):
    month = get_month_in_year(day_in_year)
    return MONTH_SEASON_MAP[month]

def get_holiday(day_in_year):
    if day_in_year not in HOLIDAYS:
        return None
    return HOLIDAYS[day_in_year]

def get_news():
    events = []
    for event in EVENT_LIKELIHOOD:
        event_die = EVENT_LIKELIHOOD[event]
        event_roll = random.randint(1, event_die)
        if event_roll == 1:
            events.append(event)
    return events

def get_year(days_passed):
    return int(START_YEAR + days_passed / (MONTHS_IN_YEAR * DAYS_IN_MONTH))

def generate_day(day_in_year, days_passed):
    day = {
        FIELD_YEAR: get_year(days_passed),
        FIELD_DAY: get_day_of_week(day_in_year),
        FIELD_MONTH: get_month_in_year(day_in_year),
        FIELD_MONTH_DAY: get_day_of_month(day_in_year),
        FIELD_YEAR_DAY: day_in_year,
        FIELD_SEASON: get_season(day_in_year),
        FIELD_HOLIDAY: get_holiday(day_in_year),
        FIELD_NEWS: get_news()
    }
    day[FIELD_TEMPERATURE] = get_temperature(day)
    day[FIELD_WEATHER] = get_weather(day)
    return day

def increment_year_day(total_days):
    total_days += 1
    year_days = MONTHS_IN_YEAR * DAYS_IN_MONTH
    if total_days < year_days:
        return total_days
    return 1

def generate_calendar(total_days):
    days = []
    day = START_DAY
    for i in range(total_days):
        day = increment_year_day(day)
        days.append(generate_day(day, i))
    return days

def display_day(day):
    display = "\n###########################################\n"
    display += "#  {}: {}, {} {}({})\n".format(
        day[FIELD_YEAR_DAY],
        day[FIELD_DAY],
        day[FIELD_MONTH],
        day[FIELD_MONTH_DAY],
        day[FIELD_SEASON])
    display += "#  Year {}, {}\n".format(day[FIELD_YEAR], ERA)
    display += "#  Weather: {} degrees, {}\n".format(
        day[FIELD_TEMPERATURE],
        day[FIELD_WEATHER])
    if day[FIELD_HOLIDAY] is not None:
        display += "#  Holday: {}\n".format(day[FIELD_HOLIDAY])
    if len(day[FIELD_NEWS]) > 0:
        display += "#  News: {}\n".format(", ".join(day[FIELD_NEWS]))
    return display

def display_calendar(days):
    with open("calendar.txt", 'w') as file:
        for day in days:
            file.write(display_day(day))        

def main():
    calendar = generate_calendar(DAYS_TO_CALCULATE)
    display_calendar(calendar)

main()