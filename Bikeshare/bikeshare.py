import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

def get_filters():

    #choose the filters:
    chosen_city = input('choose a city from either Chicago, New York City or Washington: ').title()
    possible_cities = ['Chicago', 'New York City', 'Washington']
    while chosen_city in possible_cities :
        break
    else: chosen_city = input('that was not a correct city. Which city do you want? ')

    print('you chose the city ', chosen_city)
        # TO DO: get user input for month (all, january, february, ... , june)

    chosen_month = ''
    filter_month = input('do you want to filter by month? yes / no ').lower()
    while filter_month != 'no':
        if filter_month == 'yes':
            possible_months = ['January', 'February', 'March', 'April', 'May', 'June']
            chosen_month = input('Now choose a month from January - June: ').title()
            while chosen_month not in possible_months:
                chosen_month = input('that was not a correct month. Which month do you want (January - June)? ').title()
            break
        if filter_month == 'no':
            break
        else: filter_month = input('I did not understand. Yes or no?').lower()
    if filter_month == 'no':
        print('no month-filter applied')
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    chosen_day = ''
    day_filter = input('do you want to filter by day? yes / no ').lower()
    while day_filter != 'no':
        if day_filter == 'yes':
            possible_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            chosen_day = input('Now choose a day from Monday - Sunday: ').title()
            while chosen_day not in possible_days:
                chosen_day = input('That was no correct day. Please choose a day: ').title()
            break
        if day_filter == 'no':
            break
        else: day_filter = input('I did not understand. Yes or no?').lower()
    if day_filter == 'no':
            print('no day-filter applied')

    print('-'*40)

    return chosen_city, chosen_month, chosen_day

def load_data(chosen_city, chosen_month, chosen_day):

    """
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #open the correct city table
    df = pd.read_csv(CITY_DATA[chosen_city.lower()])
    #now filter for the month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month #is a number from 1-6
    df['day_of_week'] = df['Start Time'].dt.weekday_name # is the name of the week (e.g. Sunday)

    month_dict = {
    'January' : 1,
    'February' : 2,
    'March' : 3,
    'April' : 4,
    'May' : 5,
    'June': 6,
    }

    if chosen_month != '':
        is_month = df['month']== month_dict[chosen_month]
        df = df[is_month]

    #now filter for the day
    if chosen_day != '':
        is_day = df['day_of_week']== chosen_day
        df = df[is_day]

    return df

def time_stats(df):
    show_data = 'not yet'
    while show_data != 'yes':
        show_data = input('Do you want to see the first 5 lines of the data as an example? yes / no ')
        if show_data == 'yes':
            print(df.head())
            break
        if show_data == 'no':
            break
        else:
            show_data = input('what now? ')

    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month
    #num_month = df['month']

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #num_day = df['day_of_week']

    df['hour'] = df['Start Time'].dt.hour
    popular_month = df['month'].mode()[0]

    # convert the Start Time column to datetime
        # df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns

    #num_month = df['month']
    #num_day = df['day_of_week']

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('most popular month is: ',popular_month)
    print('most popular day is: ',popular_day)
    print('most popular hour is: ',popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station']
    popular_startstation = df['Start Station'].value_counts().idxmax()

    # TO DO: display most commonly used end station
    end_station = df['End Station']
    popular_endstation = df['End Station'].value_counts().idxmax()

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = start_station + ' ' + end_station
    #old one: popular_combination = df['combination_stations'].value_counts().idxmax()
    popular_combination = combination_stations.value_counts().idxmax()

    print('the most popular start station is: ', popular_startstation)
    print('the most popular end station is: ', popular_endstation)
    print('the most popular station combination is: ', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    end_time = time.time()
    # TO DO: display total travel time
    #triptime = df['Duration']
    print('*' * 40)

    trip_hour = int(df['Trip Duration'].sum()/3600)
    trip_minutes = round(((df['Trip Duration'].sum() - (trip_hour * 3600)) / 60),2)

    print('The total trip durations are {} hours, and {} minutes'.format(trip_hour, trip_minutes))

    # TO DO: display mean travel time
    mean_triptime = int(df['Trip Duration'].mean()/60)
    print('The mean trip duration is ', mean_triptime, 'minutes')

    std_triptime = int(np.std(df['Trip Duration'])/60)
    print('The std of the trip duration is ', std_triptime, ' minutes')

    max_triptime = round(df['Trip Duration'].max() / 60,2)
    print('The longest trip was ', max_triptime, ' minutes')

    min_triptime = round(df['Trip Duration'].min() / 60,2)
    print('The shortest trip was ', min_triptime, ' minutes')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('\nThere is no gender data in this table')

    # TO DO: Display earliest, most recent, and most common year of birth

    # earliest
    if 'Birth Year' in df:

        df['Birth Year'] = df['Birth Year'].fillna((df['Birth Year'].mean()))

        ear_birthyear = min(df['Birth Year'])
        print('\nThe oldest person using our bikes is from the year ',int(ear_birthyear))
        # most recent
        mr_birthyear = max(df['Birth Year'])
        print('The youngest person using our bikes is from the year ', int(mr_birthyear))
        # most common
        mc_birthyear = df['Birth Year'].mode()[0]
        print('The most common birth year is ', int(mc_birthyear))

    else:
        print('\nThere is no birth year data in this table')


    print("\nThis took %s seconds." % (time.time() - start_time))
#run all the defined functions down here
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
