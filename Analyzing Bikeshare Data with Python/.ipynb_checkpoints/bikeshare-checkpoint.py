import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
accepted_months = ['january','february','march','april','may','june']
accepted_days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter the city whose bikeshare data you would like to analyze: ')
        city = city.lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print("\nThat is not a valid city! \nSupported cities are: 'Chicago', 'New York City', and 'Washington'.")
    print('You selected {}!'.format(city.title()))

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease enter the month for which you would like to analyze data: ')
        month = month.lower()
        if (month == 'all') or (month in accepted_months):
            break
        else:
            print("\nThat is not a valid month! \nSupported options are: {}.".format(accepted_months))
    print("You selected {}!".format(month.title()))

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease enter the day of the week for which you would like to analyze data: ')
        day = day.lower()
        if (day == 'all') or (day in accepted_days):
            break
        else:
            print("\nThat is not a valid day! \nSupported options are: {}.".format(accepted_days))
    print("You selected {}!".format(day.title()))

    print('-'*40)
    print('Initiating analysis with selections as city: {}, month: {}, day: {}'.format(city.title(),month.title(),day.title()))

    # Return selected variables
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

    # Load correct .csv file depending on city selection
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to DateTime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday
    df['Start Hour'] = df['Start Time'].dt.hour

    # Filter by month selection
    if month != 'all':
        month = accepted_months.index(month) + 1
        df = df[df['Month'] == month]
    # Filter by day of week selection
    if day != 'all':
        day = accepted_days.index(day)
        df = df[df['Day of Week'] == day]

    # Return filtered DataFrame
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    x = df['Month'].mode()
    print('The most common month for rides in your selection is {}.'.format(accepted_months[x[0] - 1].title()))

    # Display the most common day of week
    y = df['Day of Week'].mode()
    print('The most common day of week for rides in your selection is {}.'.format(accepted_days[y[0]].title()))

    # Display the most common start hour
    z = df['Start Hour'].mode()
    print('The most common hour for rides in your selection is at {}:00.'.format(z[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    x = df['Start Station'].mode()
    print('The most commonly used start station is {}.'.format(x[0]))

    # Display most commonly used end station
    y = df['End Station'].mode()
    print('The most commonly used end station is {}.'.format(y[0]))

    # Display most frequent combination of start station and end station trip
    df['Journey'] = df['Start Station'].str.cat(df['End Station'], sep =', to ')
    z = df['Journey'].mode()
    print('The most popular journey is from {}.'.format(z[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    x = df['Trip Duration'].sum()
    print('The total trip duration for all rides is {} seconds.'.format(x))

    # Display mean travel time
    y = df['Trip Duration'].mean()
    print('The mean trip duration for all rides is {} seconds.'.format(y))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    x = df.groupby('User Type').count()
    print('Riders that are Customers: {} \nRiders that are Subscribers: {}'.format(x['Start Time']['Customer'],x['Start Time']['Subscriber']))

    if city == 'chicago' or city == 'new york city':
        # Display counts of gender
        y = df.groupby('Gender').count()
        print('\nRiders that are Female: {} \nRiders that are Male: {}'.format(y['Start Time']['Female'],y['Start Time']['Male']))

        # Display earliest, most recent, and most common year of birth
        z_mode = df['Birth Year'].mode()
        print('\nThe most common birth year is ',int(z_mode[0]))
        z_min = df['Birth Year'].min()
        print('The earliest is ',int(z_min))
        z_max = df['Birth Year'].max()
        print('The most recent is ',int(z_max))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
