# -*- coding: utf-8 -*-
""" This code was written by Brendan Lee through to 08/08/2020, using knowledge obtained while studying Udacity Programming for Data Science
nanodegree. In completing the code, I have referenced a number of websites to support coding build. This includes Stack Overflow, GeeksforGeeks
and the Python package library. Much of this was to discover new methods/libraries or understand how to use the arguments within a particular
method or function.

A few more amends were made to support GitHub learning on 18/09/20"""

import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    city = input("Please enter the name of the city you'd like to analyse (chicago, new york city, washington): \n").lower()
    while city not in cities :
        print("{} is an invalid entry. Please enter one of 'chicago', 'new york city' or 'washington'.".format(city))
        city = input("Please enter the name of the city you'd like to analyse (chicago, new york city, washington): \n").lower()
    print("You are analysing {} for this request.".format(city).title())

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    month = input("Please enter the month you'd like to analyse (all, january, february, march, april, may, june): \n").lower()
    while month not in months :
        print("{} is an invalid entry, please try again.".format(month))
        month = input("Please enter the month you'd like to analyse (all, january, february, march, april, may, june): \n").lower()
    print("You have selected {} for analysis timeframe.".format(month).title())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Please enter the day you'd like to filter by (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): \n").lower()
    while day not in days :
        print("{} is an invalid entry, please try again.".format(day))
        day = input("Please enter the day you'd like to filter by (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): \n").lower()
    print("You have selected {} for days of week filter.".format(day).title())

    print('-'*40)
    print("Your analysis will be based upon " + city.title() + " with month filter set to " + month.title() + " and day filter set to " + day.title() +".")
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() #Changed to dt.weekday_name() in main submission to avoid error


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # Check output and export to csv only when validating answers
    #df.to_csv("first_output.csv")
    #print(df.head(5))
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    #cities = ['chicago','new york city','washington']
    #months = [january','february','march','april','may','june']
    #days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common rental month is: " + calendar.month_name[df['month'].mode()[0]])

    # TO DO: display the most common day of week
    print("The most common rental day of week is: " + str(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    # Need to create variable to summarise data to hourly level
    df['hour_start'] = df['Start Time'].dt.hour
    print("The most common rental start hour is: " + str(df['hour_start'].mode()[0]) + ":00 - " + str(df['hour_start'].mode()[0]) + ":59")

    # Check output and export to Excel to validate answers
    #df.to_excel("second_output.xls")
    #print(df.head(5))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: " + str(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: " + str(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station tripf
    # Need to create variable showing start and end journeys
    df['Start_End_Station'] = df['Start Station'] + " to " + df['End Station']
    print("The most common combination of stations is: " + str(df['Start_End_Station'].mode()[0]))

    # Check output and export to Excel to validate answers
    #df.to_excel("third_output.xls")
    #print(df.head(5))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time during the period selected is approx.: {} hours and {} minutes.".format(str(df['Trip Duration'].sum()//3600),str(int((df['Trip Duration'].sum()%3600)/60))))

    # TO DO: display mean travel time
    print("The mean travel time during the period selected is: {} minutes".format(str(int(df['Trip Duration'].mean()//60))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The user types in this selection are shown below:\n")
    print(df['User Type'].value_counts(dropna=False))


    #Check whether column names exist for user stats, and run stats if so, warning message if not.
    if 'Gender' in df:
    # TO DO: Display counts of gender
        print("\nThe Genders in this selection are shown below:\n")
        print(df['Gender'].value_counts(dropna=False))
    else:
        print("No Gender variable in dataset. Stats cannot be returned.")

    #Check whether column names exist for user stats, and run stats if so, warning message if not.
    if 'Birth Year' in df:
    # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earliest Year of Birth in this selection is: " + str(int(df['Birth Year'].min())))
        print("The latest Year of Birth in this selection is: " + str(int(df['Birth Year'].max())))
        print("The most common Year of Birth in this selection is: " + str(int(df['Birth Year'].mode()[0])))
    else:
        print("No Birth Year variable in dataset. Stats cannot be returned.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def first_five(df):
    #Add code to give user option of viewing first 5 lines of output. If not, leave function
        sample_answer = ['yes','no']
        sample = input("\nWould you like to see a sample of the first five rows of your data? Enter yes or no.\n").lower()
        while sample not in sample_answer :
            print("{} is an invalid entry, please try again.".format(sample))
            sample = input("\nWould you like to see a sample of the first five rows of your data? Enter yes or no.\n").lower()
        if sample == 'yes' :
            print(df.head(5))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        first_five(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
