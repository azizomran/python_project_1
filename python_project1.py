# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:30:57 2020

@author: Abdulziz Al Omran
"""
import pandas as pd
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_DATA = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS_DATA= ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursaday', 'friday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city data would you like to explore? chicago, new york or washington?\n")
    while city not in CITY_DATA:
        print('please review your input to match our used spelling, case sensitive.\n')
        city = input("Which city data would you like to explore? chicago, new york or washington?\n")
              
    # TO DO: get user input for month (all, january, february, ... , june)
    month= input('which month would you like ti review? january, february, march, april, may, june or simply all\n')
    while month not in MONTHS_DATA and month != 'all':
        print('please review your input to match our used spelling, case sensitive.\n')
        month= input('which month would you like ti review? january, february, march, april, may, june or simply all \n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week= input('please specify a day of week (all, monday, tuesday, ... sunday)?\n')
    while day_of_week not in DAYS_DATA and day_of_week != 'all': 
        print ('please review your input to match our used spelling, case sensitive.')
        day_of_week= input('please specify a day of week (all, monday, tuesday, ... sunday)?\n')
    
    print('-'*40)
    return city, month, day_of_week

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
   
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = MONTHS_DATA.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month ]
       
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = DAYS_DATA.index(day)
        df = df[df['day_of_week']==day] 
     
       
    return df
def time_stats(df):
    if 'Start Time' not in df.columns:
        print('sorry we dont have enough data to calculate time stats')
        return
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = df ['Start Time'].apply(pd.to_datetime)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month_int'] = df ['Start Time'].dt.month
    popular_month = df['month_int'].mode()
    print('busiest month: ' + MONTHS_DATA[popular_month[0]-1])
    # TO DO: display the most common day of week
    df['day_of_week']= df['Start Time'].dt.dayofweek
    popular_day = df['day_of_week'].mode()
    # TO DO: display the most common start hour
    print('most popular day is: '+ DAYS_DATA[popular_day[0]])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
# find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()
    print('Most Frequent Start Hour:', popular_hour[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    if 'Start Station' not in df.columns or 'End Station' not in df.columns:
        print('sorry we dont have enough data to calculate station stats')
        return
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode()[0]
    print ('the most common starting station is: ' + str(common_station))
    
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print ('the most common end station is: ' +str (common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combine Stations'] = df['Start Station'] + ' and ' + df['End Station']
    common_combo = df['Combine Stations'].mode()[0]
    print ('the most common trip is between: ' + str(common_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    if 'Trip Duration' not in df.columns:
        print('sorry we dont have enough data to calculate trip stats')
        return
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_dur = sum(df['Trip Duration'])
    print('total travel time in minutes is:  ' + str(trip_dur//60))
    # TO DO: display mean travel time
    average_trip_dur = df['Trip Duration'].mean()
    print('on average a trip took, in minutes: ' + str(average_trip_dur //60))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    if 'User Type' not in df.columns or 'Gender' not in df.columns or 'Birth Year' not in df.columns:
        print('sorry we dont have enough data to calculate user stats')
        return
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print (user_types)
    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()
    print(count_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earlies_year = min(df['Birth Year'])
    print(int(earlies_year))
    common_year = df['Birth Year'].mode()[0]
    print(int(common_year))
    max_year = max(df['Birth Year'])
    print(int(max_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    start_loc = 0
    view_data = input('would you like to view the data, yes/no?')
    while view_data == 'yes':
        print(df.iloc[int(start_loc):int(start_loc)+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: yes/no \n").lower()
        
        
(city, month, day_of_week) = get_filters()

df = load_data(city, month, day_of_week)
print (df)
time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats(df)
show_data(df)