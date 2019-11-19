#!/usr/bin/env python
# coding: utf-8

# In[80]:


#!/usr/bin/env python

'''

__author__ = "Bijan Vafaei"
__copyright__ = "Copyright 2019"
__credits__ = 
__license__ = 
__version__ = "1.0.2"
__maintainer__ = 
__email__ = "bvafaei@epsteinglobal.com"
__status__ = "Prototype"

'''

# Importing required libraries

import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from scipy import stats
from Json_read import JsonObj


class Song_Analytics_Data_Challenge:

    def __init__(self):
        obj = JsonObj()
        self.file_name = obj.get_config_obj('file_name')
        self.data_store_location = obj.get_config_obj('data_store_location')

# General Functions        
    def read_data(self):
        df = pd.DataFrame(data = pd.read_csv(self.data_store_location+self.file_name,header='infer', encoding='utf-8' , na_values= '-'))
        return df
    
    
    def unique_value(self, df, arg):
        return df[arg].unique()

    
    def filter_col(self, df, cols):
        return df.filter( items= cols)

    
    def filter_value(self, df,**kwargs):
        if kwargs is not None:
            filtered_df = df
            for key, value in kwargs.items():
                filtered_df = filtered_df[filtered_df[key] == value]
        return filtered_df


    def agg(self, df, groupby_cols, count_cols, **kwargs):
        if ('method' in kwargs) & (kwargs['method'] == 'sum'):
                df_agg = df.groupby(groupby_cols)[count_cols].agg(pd.Series.sum).reset_index()
        else:
            df_agg = df.groupby(groupby_cols)[count_cols].agg(pd.Series.count).reset_index()
        return df_agg

    
#Question-Specific Functions q1 to q8, and q8_plot
    def q1(self, df, *args):
        arg_num =     [len(self.unique_value(df, arg).tolist()) for arg in args ] 
        return arg_num


    def q2(self, df):
        max_score = df['score'].max()
        chart_max_score = self.filter_value(df, score = max_score)
        return self.filter_col(chart_max_score, ['song','month', 'artist', 'score'])


    def q3(self, df, **kwargs): 
        fav_song = self.filter_value(df, **kwargs ).reset_index()
        months_on_chart_US = len(fav_song['month'].tolist())
        best_position_US = fav_song['us'].min()
        best_month_US = fav_song.iloc[fav_song['us'].idxmin()]['month']
        return months_on_chart_US, best_position_US , best_month_US


    def q4(self, df):
        agg_df_artist = self.agg(df, 'artist', 'month' , method = 'count')
        artist_most_time_on_chart = agg_df_artist['artist'].iloc[agg_df_artist['month'].idxmax()]
        most_time_on_chart = agg_df_artist['month'].iloc[agg_df_artist['month'].idxmax()]
        return artist_most_time_on_chart , most_time_on_chart

    
    def q5(self, df, **kwargs):
        return self.filter_value(df, **kwargs)['month'].count()


    def q6(self, df, **kwargs):
        df_target_artist = self.filter_value(df, artist = kwargs['artist'])
        agg_df = self.agg(df_target_artist, 'song' , kwargs['country'] , method = 'count')
        song_list = agg_df[agg_df[kwargs['country']] == kwargs['countryhit']]
        return  song_list 


    def q7(self, df, artist_name):
        agg_df_artist_month = self.agg(self.filter_value(df, artist = artist_name),'month','song' , method = 'count')
        max_num_songs = agg_df_artist_month['song'].max()
        artist_best_month = self.filter_value(agg_df_artist_month, song = max_num_songs)['month'].tolist()
        artist_metrics = self.filter_col(self.filter_value(df , month = artist_best_month[0], artist = artist_name), ['month' , 'artist' , 
        'song' ,'us']).reset_index(drop=True).sort_values('us')
        return artist_metrics


    def q8(self, df, start_date, end_date):
        df_filtered = self.filter_col(df, ['month', 'song', 'artist'])
        df_filtered['month'] = pd.to_datetime(df_filtered['month'], format = '%b %Y')
        mask = (df_filtered['month'] >= start_date) & (df_filtered['month'] <= end_date)
        df_yr = df_filtered[ mask ]
        df_yr_agg = df_yr.groupby(['artist']).agg('nunique').sort_values('song', ascending = False)\
        ['song'].to_frame().reset_index().head(10)
        return df_yr_agg


    def q8_plot(self, df, graph_title, *args):
        sns.set(style="whitegrid")
        f, ax = plt.subplots(figsize=(20, 15))
        sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
        ax = sns.barplot(x = args[0] , y = args[1] , data = df , label = "Number of Songs", palette="Blues_r", color="b" , saturation=0.8)
        ax.set_title(graph_title)
        ax.set(xlabel='Name of Artist', ylabel='No. of Unique Songs')
        ax.legend(ncol=2, loc="upper right", frameon=True)
        sns.despine(left=True, bottom=True)
        return plt.show()
