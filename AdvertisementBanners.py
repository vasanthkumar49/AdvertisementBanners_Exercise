# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:00:55 2021
@author : Vasanthakumar Chidanandagari

"""


# Importing required modules
import pandas as pd
import numpy as np
import json


def advertisement_banners():
    # 1. Reading events stored in JSON files - clicks.json input file
    clicks_df= pd.read_json('<path>clicks.json')
    clicks_df.info()
    
    filtered_clicks_df=clicks_df.replace(r'', np.NaN)
    filtered_clicks_df=filtered_clicks_df.dropna()
    filtered_clicks_df.isnull().sum()
    
    # 1. Reading events stored in JSON files - impressions.json input file
    impressions_df = pd.read_json('<path>impressions.json')
    impressions_df=impressions_df.rename(columns={"id":"impression_id"})
    impressions_df.info()
    
    impressions_df=impressions_df.replace(r'', np.NaN)
    filtered_impressions_df=impressions_df.dropna()
    
    # 2. Calculating metrics for some dimensions
    final_df=pd.merge(filtered_impressions_df,filtered_clicks_df, on="impression_id",how="left")
    
    count_df = pd.pivot_table(final_df, index=['app_id','country_code'], aggfunc=lambda revenue: len(revenue.dropna())).rename(columns={'revenue': 'clicks','impression_id': 'impressions'},inplace=False)
    count_df=count_df.drop('advertiser_id',axis=1)
    revenue_df = final_df.groupby(['app_id','country_code'])['revenue'].sum().reset_index()
    
    metrics_df = pd.merge(count_df, revenue_df,  how='left', left_on=['app_id','country_code'], right_on = ['app_id','country_code'])
    # Writing the output to a JSON file using the given format
    metrics_df.to_json('<path>metrics.json',orient='records')
        
    # Making a recommendation for the top 5 advertiser_ids to display for each app and countrycombination.
    top5_advertiser_df = final_df.groupby(['app_id','country_code','advertiser_id'])['revenue'].sum().reset_index()
    top5_advertiser_df = top5_advertiser_df.sort_values(['app_id','revenue'],ascending=False).groupby(['app_id','country_code']).head(5)
    top5_advertiser_df = top5_advertiser_df.drop('revenue',axis=1)
    
    top5_advertiser_df2=top5_advertiser_df.pivot(index=['app_id','country_code'],columns='advertiser_id', values='advertiser_id').add_prefix('advertiser_id_').reset_index()
    top5_advertiser_df2['recommended_advertiser_ids'] =  top5_advertiser_df2.iloc[:,2:].agg(lambda x : x.dropna().tolist(),axis=1)
    top5_advertiser_df2=top5_advertiser_df2.iloc[:,[0,1,-1]]
    
    # Writing the output to a JSON file using the given format
    top5_advertiser_df2.to_json('<path>top5_advertiser.json',orient='records')
        

if __name__ == '__main__':
    # Calling main method 
    advertisement_banners()