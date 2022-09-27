import time
import pandas as pd
import numpy as np
import IPython
from operator import itemgetter

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months=['january','february','march','april','may','june','all']

cities=['chicago','new york city','washington','all']

day_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months=['january','february','march','april','may','june','all']

cities=['chicago','new york city','washington','all']

day_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    msg='Hello! Let\'s explore some US bikeshare data'
    print('-'*len(msg)+'\n'+msg+'\n'+'-'*len(msg))
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            print('\nAvailable cities are: {}'.format(cities))
            city=input('Enter City:').lower()
            print('Value entered: {}'.format(city))
            if city in ['q']:
                city=None
                print('q entered, Exiting!!!!')
                break    
            elif city not in cities :
                print('Invalid entry !!!! try again')
                continue
            else:
                print('Input recorded')
        except Exception as e:
            print('{}'.format(e))
       
    # get user input for month (all, january, february, ... , june)
        try:
            print('\nMonths are: {}'.format(months))
            month=str(input('Enter month:')).lower()
            print('Value entered: {}'.format(month))

            if month in ['q']:
                month=None
                print('q entered, Exiting!!!!')
                break
            elif month not in months:
                print('Invalid entry!!!! try again')
                continue
            else:
                print('Input recorded')
        except Exception as e:
            print('{}'.format(e))

    # get user input for day of week (all, monday, tuesday, ... sunday)
        try:
            print('\nDay of the weeks are: {}'.format(day_of_week))
            day=str(input('Enter day of the week: ')).lower()
            print('Value entered: {}'.format(day))

            if day in ['q']:
                day = None
                print('q entered, Exiting!!!!')
                break
            elif day not in day_of_week:
                print('Invalid entry!!!! try again')
                continue
            else:
                print('Input recorded')
                break
        except Exception as e:
            print('{}'.format(e))
    
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

    if city=='all':
        db=pd.concat([pd.read_csv(CITY_DATA['chicago']),pd.read_csv(CITY_DATA['new york city'])],ignore_index=True)
        df=pd.concat([db,pd.read_csv(CITY_DATA['washington'])],axis=0,ignore_index=True)
    else :
        df=pd.read_csv(CITY_DATA[city])
        
    df.fillna(0)
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month_name()
    df['day of week']=df['Start Time'].dt.day_name()
    df['hour of day']=df['Start Time'].dt.hour
    df.insert(6,'Start-End',df['Start Station']+' '+ df['End Station'])
    
    if month !='all':
        df=df[df['month']==month.title()]
    
    if day !='all':
        df=df[df['day of week']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    countm={}
    for x in df['month']:
        countm[x]=countm.get(x,0)+1 
    maxm=max(countm)
    print('\nThe most common month is {}'.format(maxm))
               
    # display the most common day of week
    countdw={}
    
    for x in df['day of week']:
        countdw[x]=countdw.get(x,0)+1 
    maxdw=max(countdw)
    print('\nThe most common day of the week is {}'.format(maxdw))
               
    # display the most common start hour
    countsh={}
    for x in df['hour of day']:
        countsh[x]=countsh.get(x,0)+1 
    maxsh=max(countsh)
    print('\nThe most common start hour is {}'.format(maxsh))
               
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    countss={}
    for x in df['Start Station']:
        countss[x]=countss.get(x,0)+1
    print('\nThe most commonly used start station is {}'.format(max(countss)))

    # display most commonly used end station
    countes={}
    for x in df['End Station']:
        countes[x]=countes.get(x,0)+1
    print('\nThe most commonly used end station is {}'.format(max(countes)))

    # display most frequent combination of start station and end station trip
    countss_es={}
    for x in df['Start-End']:
        countss_es[x]=countss_es.get(x,0)+1
    print('\nThe most frequent combination of Start station and end station trip is {}'.format(max(countss_es)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nThe total travel time is {} mins'.format(sum(df['Trip Duration']/60)))

    # display mean travel time
    print('\nThe mean travel time is {} mins'.format(np.mean(df['Trip Duration']/60)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    countut={}
    for x in df['User Type']:
        countut[x]=countut.get(x,0)+1
    print('\nThe counts of user types is {}'.format(countut))

    # Display counts of gender
    countg={}
    for x in df['Gender']:
        countg[x]=countg.get(x,0)+1
    print('\nThe counts of gender is {}'.format(countg))

    # Display earliest, most recent, and most common year of birth
    print('\nThe earliest year of birth is {}'.format(int(min([x for x in df['Birth Year'] if x>0]))))
    print('\nThe the most recent year of birth is {}'.format(int(max([x for x in df['Birth Year'] if x>0]))))
    print('\nThe most common year of birth is {}'.format(int(df['Birth Year'].value_counts().index.tolist()[0])))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day=get_filters()
        df=load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        response=(str(input('\nDo you want to repeat? Yes or No: ')).lower())
        if response == 'no':
            print('\n'+'-'*7 + 'Exiting' + '-'*7+"\n Thank you for using Albert's application" )
            break
            
if __name__=='__main__':
    main()