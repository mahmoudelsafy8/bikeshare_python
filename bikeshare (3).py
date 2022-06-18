import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    cities = ['chicago', 'new york', 'washington']
    while True:
        city = input('Please, choose the city you want to explore: chicago, new york, washington? \n:').lower()
        if city in cities:
            print('\n Working on it!.')
            break
        else:
             print('\nOops, you entered invalid input city!!.')                  

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("now please, choose which month {}, or 'all' to apply no month filter: \n:".format(months)).lower()
        if month in months:
            break
        else:
            print('\n Oops, you entered invalid input month!!.')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input("\n Now please, choose which day {}, or 'all' to apply no day filter: \n:".format(days)).lower()
        if day in days:
            break
        else:
            print('\nOops, you entered invalid input day!!')
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
    df = pd.read_csv(CITY_DATA[city])
    
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month                                  
    df['day_of_week'] = df['Start Time'].dt.day_name()
                                      
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']             
        month = months.index(month) + 1
        df = df[df['month'] == month]   
                                      
    if day != 'all':  
        df = df[df['day_of_week'] == day.title()]                              

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        most_common_month = df['month'].mode()[0]
        months = ['january', 'february' , 'march', 'april', 'may', 'june']     
        most_common_month = months[most_common_month -1]
        print('Most common month: {}'.format(most_common_month))
                                      
    # TO DO: display the most common day of week
    if day == 'all':
         most_common_day = df['day_of_week'].mode()[0]
         print('Most common day of week: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['Start Time'] = df['Start Time'].dt.hour
    most_common_start_hour = df['Start Time'].mode()[0]
    print('Most common start hour: {}'.format(most_common_start_hour))  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(most_used_start_station))
    


    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station" {}'.format(most_used_end_station))      


    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    print('Most frequent combination of Start & End station trip: {}'.format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(total_travel))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time: {}'.format(mean_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Counts of user types: {} \n'.format(count_user_types))


    # TO DO: Display counts of gender
    if "Gender" in df:
        gender_count = df['Gender'].value_counts()
        print('Counts of gender: {} \n'.format(gender_count))
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
       
        earliest = int(df['Birth Year'].min())
        print('Earliest user year: {}'.format(earliest))
      
        most_recent = int(df['Birth Year'].max())
        print('Most recent user year: {}'.format(most_recent))
       
        most_common = int(df['Birth Year'].mode()[0])
        print('Most common year: {}'.format(most_common))
    else:
        print('Sorry, There is no birth year for Washington city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """Displays 5 rows on bikeshare users and next 5 rows as the requested."""
    
    view_data = input('Would you like to view 5 rows of individual trip data? yes or no?\n').lower()
    start_loc = 0
    while True:
        if view_data == 'yes':
            print(df[start_loc:start_loc + 5])
            start_loc += 5
            view_display = input('Do you wish to continue?:')
            if view_display != 'yes':
                print('Thank you')
                break
                
    
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
