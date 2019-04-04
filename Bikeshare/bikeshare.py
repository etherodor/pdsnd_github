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

    chosen_city = input('choose a city from either Chicago, New York or Washington: ').title()
    possible_cities = ['Chicago', 'New York', 'Washington']
    while chosen_city in possible_cities :
        break
    else: chosen_city = input('that was not a correct city. Which city do you want? ')

    print('you chose the city ', chosen_city)
        # TO DO: get user input for month (all, january, february, ... , june)
    possible_months = ['January', 'February', 'March', 'April', 'May', 'June']
    chosen_month = input('Now choose a month from January - June: ').title()
    while chosen_month in possible_months :
        break
    else: chosen_month = input('that was not a correct month. Which month do you want? ')
    print('you chose the month ', chosen_month)

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    possible_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    chosen_day = input('Now choose a day from Monday - Sunday: ').title()
    while chosen_day in possible_days :
        break
    else: chosen_day = input('that was not a correct day. Which day do you want? ')
    print('you chose the day ', chosen_day)

    print('-'*40)
    return chosen_city, chosen_month, chosen_day
    #testcomment
    #second test comment
    #third commit message

def load_data(chosen_city, chosen_month, chosen_day):
    """
        df - Pandas DataFrame containing city data filtered by month and day
    """
    chosen_city = chosen_city.lower()
    df = pd.read_csv(CITY_DATA[chosen_city])
    return df


def time_stats(df):
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

    tripduration = df['Trip Duration'].sum()
    print('the total trip duration is ', df['Trip Duration'].sum(), ' seconds.')

    # TO DO: display mean travel time
    #mean_triptime = df['Trip Duration'].mean()
    print('the mean trip duration is ', df['Trip Duration'].mean(), 'seconds')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #user_types = df['User Type'].value_counts() - deleted this for the last project
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    #gender = df['Gender'].value_counts() - deleted this for the last project
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth

    birthyear = df['Birth Year']
    # earliest
    ear_birthyear = int(min(birthyear))
    print('\nThe oldest person using our bikes is from the year ',ear_birthyear)
    # most recent
    mr_birthyear = int(max(birthyear))
    print('The youngest person using our bikes is from the year ', mr_birthyear)
    # most common
    mc_birthyear = int(df['Birth Year'].mode()[0])
    print('The most common birth year is ', mc_birthyear)

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
