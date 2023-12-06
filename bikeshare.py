import time
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago', 'new york city', 'washington']
    city = str(input("Enter city name:chicago, new york city, washington")).lower()
    while city not in cities:
        city = str(input('Please try again')).lower()
        if city in cities:
            print("Great!,{}".format(city))
            break
        else:
            print("Emo!,try again")

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    month = input('Enter the month:january, february, march, april, may, june or all ').lower()

    while month not in months:
        month = input('Please try again ').lower()
        if month in months:
            print("Good,{}".format(month))
            break
        else:
            print('Emo!, something went worng')

# create a change for git
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'sunday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    day = input('Enter the day:monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ').lower()

    while day not in days:
        day = input('Please try again ').lower()
        if day in days:
            print('well done , the day is {}'.format(day))
            break
        else:
            print('Emo, try again ')



    print('-'*40)
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
    # Reference from practice 3
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
    # Filter by month :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    # Filter by day:
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        print('The most common month:', df['month'].mode()[0])

    # display the most common day of week
    if day == 'all':
        print('The most common day of week:', df['day_of_week'].mode()[0])

    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour

    print('The most common hour of day:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most common start station:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('most common end station:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    Comb_Station = df.groupby(['Start Station', 'End Station'])['Trip Duration'].agg(
        'count').sort_values(ascending=False).head(1)

    print("most common trip from start to end: \n", Comb_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # display mean travel time
    print('Average travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of each user type : ",
          df['User Type'].value_counts())

    # Display counts of gender
    if city == 'new york city' or city == 'chicago':
        print("Counts of each gender ",
              df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
        print("Earliest birth year: ", df['Birth Year'].min())
        print("Most recent year: ", df['Birth Year'].max())
        print("Most common year: ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Show 5 rows of data and more
def show_raw_data(df):
        raw_data = input("Do you like to see raw data? please type (yes or no)? ").lower()
        start_loc = 0
        while (raw_data != "no"):
            print(df[start_loc:start_loc + 5])
            raw_data = input("5 more data? please type (yes or no)? ").lower()
            start_loc += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
