import dateparser
from numpy import datetime64
import pandas as pd
from datetime import date

def df_interval(date_debut, date_fin):
    return pd.DataFrame(pd.Series(\
        pd.date_range(start=date_debut, end=date_fin), name='date'))

def action_gouv_calendar_builder(path_file):
    df_gouv = pd.read_csv(path_file, index_col=0, header=0)\
        .fillna(date.today()).astype(str).reset_index()
    # .strftime("%d/%m/%Y") for inputing to date_range 
    df_gouv['Date_debut'] = df_gouv['Date_debut']\
        .apply(lambda d: dateparser.parse(d).date().strftime("%d/%m/%Y"))
    df_gouv['Date_fin'] = df_gouv['Date_fin']\
        .apply(lambda d: dateparser.parse(d).date().strftime("%d/%m/%Y"))
    # now we want to flip the gouv action df in order to have 
    # date index and boolean values for actions in columns
    covid_calendar = df_interval('1/12/2019', date.today())
    for action_col in df_gouv.Action_gouv.unique():
        # for each government action, create a dataframe of one column containing 1
        # at each date (index) where the action applies
        df_action = pd.concat([df_interval(row[1]['Date_debut'], row[1]['Date_fin']) 
                    for row in df_gouv[df_gouv['Action_gouv']==action_col].iterrows()])
        df_action[action_col] = 1
        covid_calendar = covid_calendar.merge(df_action, how='left', on='date').fillna(0)
    return covid_calendar
    # now just join on epidemic stats for more complete data 
    
def epidemic_stats(url):
    df_epidemic_stats = pd.read_csv(url, header=0, sep=',')
    df_epidemic_stats = df_epidemic_stats[df_epidemic_stats['location']=='France']
    df_epidemic_stats = df_epidemic_stats[['date',  
    'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'icu_patients', 
    'positive_rate', 'people_fully_vaccinated', 'median_age']]
    df_epidemic_stats['date'] = df_epidemic_stats['date']\
        .apply(lambda d: dateparser.parse(d).date()).astype(datetime64)
    return df_epidemic_stats

if __name__ == "__main__":
    path = 'chronologie_covid/'
    file = 'covid_chronologie.csv'
    covid_calendar = action_gouv_calendar_builder(path + file)
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df_epidemic_stats = epidemic_stats(url)
    covid_calendar = covid_calendar.merge(df_epidemic_stats, how='left', on='date').fillna(0)
    covid_calendar.to_csv(path + 'calendrier.csv')