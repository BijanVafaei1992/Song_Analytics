#!/usr/bin/env python
# coding: utf-8


from Song_Analytics import Song_Analytics_Data_Challenge



class Model_run:

    def __init__(self):
        self.Tc=Song_Analytics_Data_Challenge()
        
    def Run_Model(self):

        print("###LOADING DATAFRAME###")
        
        chart = self.Tc.read_data()
        
        print("###DATAFRAME LOADED###")
        
        
        print("###ANSWERING TO THE QUESTIONS###")

        ans1 = self.Tc.q1(chart , 'artist', 'song')
        print'###ANSWER 1:'  
        print ans1
        
        
        ans2 = self.Tc.q2(chart)
        print'###ANSWER 2:'
        print ans2
        
        
        ans3 = self.Tc.q3(chart , song = 'Safe And Sound', artist = 'Capital Cities')
        print'###ANSWER 3:'
        print ans3
        
        
        ans4 = self.Tc.q4(chart)
        print'###ANSWER 4:' 
        print ans4
        
        
        hit = '1'
        ans5 = self.Tc.q5(chart, artist = 'Drake', ca = hit)
        print'###ANSWER 5:'
        print ans5 
        
        
        ans6 = self.Tc.q6(chart, artist = 'Lady GaGa', au = '-')
        print'###ANSWER 6:'  
        print ans6
              
        
        artist_name = 'Ariana Grande'
        ans7 = self.Tc.q7(chart, artist_name)
        print'###ANSWER 7:'
        print ans7
        
        
        start_date = 'Jan 2013'
        end_date   = 'Dec 2017'
        chart_yr_agg = self.Tc.q8(chart, start_date, end_date)
        print'###ANSWER 8:'
        print chart_yr_agg
        
        
        graph_title = "Top Ten Artists with the Most Number of Unique Songs on Charts ({date})".format(date = str(start_date)  + ' to ' + 
                                                                                                       str(end_date)) 
        ans8_plot = self.Tc.q8_plot(chart_yr_agg, graph_title, 'artist', 'song')
        print'###PLOT'
        print ans8_plot
        
        
        
        print("###DONE###")


if __name__=="__main__":
    a=Model_run()
    a.Run_Model()


