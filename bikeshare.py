import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_stats_processing_time(start_time):
    """
    Calculates time in seconds and prints it
    """
    print("\nThis took %s seconds." % (time.time() - start_time))

def get_city():
    """
        Asks user to specify a city to analyze data for and returns the city

        Returns:
        (str) city - name of the city to analyze 
    """
    # TO DO: get city specified by the user, either (chicago, new york, washington).
    cities = ['chicago', 'new york', 'washington']
    city = ''
    while city not in cities:        
        city = input('Which city amongst the 3 would you like to explore data for?\n').lower() 
        if city in cities:
            break
        else:
            print('Sorry, you have entered a wrong city name. Please insert either chicago, new york or washington\n')
    return city
    
    
def get_month():
    """
    Asks user to specify a month to analyze data for and return the month

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    # TO DO: get month specified by the user (all, january, february, ... , june)
    months = ['january','februay','march', 'april', 'may', 'june', 'all']
    month = ''
    while month not in months: 
        month = input("Please enter a month to fliter data with or 'all' to apply no month filter. Data is only available for the first 6 months.\n").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please try again.")
    return month

           
def get_day():
    """
    Asks user to specify a day to analyze data for and returns the day

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get day specified by the  user (all, monday, tuesday, ... sunday)
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in weekdays:
        day = input("Please enter a day you would like to filter data on or 'all' to apply no day filter \n").lower()
        if day in weekdays:
            break
        else:
            print("Sorry, Invalid input. Please try again\n")
    return day


def get_filters():
    """
    Gets city, month and day specified by the user.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('There are 3 United States cities we can explore data for, namely: chicago, new york and washington\n')
  
    #get city input from get_city()
    city = get_city()

    #get month input from get_month()
    month = get_month()

    #get day input from get_day()
    day = get_day()

    print('-'*40)
    return city, month, day

def get_file_name(city):
    """
        load data file into data frame and print the file name data is being accessed from based on city filter
        Returns:
            data_frame - Pandas DataFrame containing city data filtered by month and day
        Exceptions:
            FileNotFoundError - returned when program is trying to read a file and it does not exist
            print message for the user about the file not found      
    """
    try:
        file_name = CITY_DATA[city]
        # load data file into a dataframe
        data_frame = pd.read_csv(file_name)
        print('Accessing data from {}:'.format(file_name))
        return data_frame
    #throw exception if file is not found
    except FileNotFoundError: 
        print('File can not be found')
    #throw exception for any general error related to the file
    except:
        print('An error occured. Please check stacktrace')


def show_data(city, month, day):
    """
    Shows data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = get_file_name(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()
    # TO DO: display the popular month
    popular_month = df['month'].mode()[0]
    print('The most popular month is {}'.format(popular_month))

    # TO DO: display the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular travel day is {}'.format(popular_day))

    # TO DO: display the most popular start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular travel hour is {}'.format(popular_hour))

    get_stats_processing_time(start_time)
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {} \n'.format(popular_start_station))

    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is {} \n'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station']+" "+df['End Station']
    popular_stations_combination =  df['Station Combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is {} \n'.format(popular_stations_combination))

    get_stats_processing_time(start_time)
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} \n'.format(total_travel_time))

    # TO DO: display average travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('The average travel time is: {} \n'.format(average_trip_duration))

    get_stats_processing_time(start_time)
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Display counts of user types:\n {}'.format(user_types),'\n')

    # Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('Display counts of gender:\n {}'.format(gender_types),'\n')
    else:
        print('There is no gender data available for Washington')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        coommon_birth_year = df['Birth Year'].mode()[0]

        print('The earliest birth year is: {}\n'.format(earliest_birth_year))
        print('The most recent birth year is: {}\n'.format(recent_birth_year))
        print('The most common birth year: {}\n'.format(coommon_birth_year))
    else:
        print('There is no year of birth data available for Washington')


    get_stats_processing_time(start_time)
    print('-'*40)
    
def get_raw_data(df):
    """
    Asks the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', 
    and continue these prompts and displays until the user says 'no'
    
    """
    raw_data_input = input('Would you like to see 5 lines of raw data? Please insert either yes or no.\n')
    no_of_lines = 5
        
    while raw_data_input.lower() == 'yes':
        print(df.head(no_of_lines))
        no_of_lines += 5
        raw_data_input = input('Would you like to see 5 lines of raw data? Pleaser insert either yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = show_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
