import pandas as pd
from pandas import ExcelWriter
import xlsxwriter

def Sector_breakdown():
    sector_list = []
    company = pd.read_excel('/home/dudals3844/Financial_Engneering/data/kospi.xls', sheet_name='Sheet1', encoding = 'utf-8')
    for idx in company['업종'].unique():
        sector_list.append(idx)
    
    print(pd.DataFrame(sector_list))
    
    sector_list_dataframe = pd.DataFrame(sector_list)
    writer = pd.ExcelWriter('/home/dudals3844/Financial_Engneering/data/sector_breakdown.xlsx', engine = 'xlsxwriter')

    sector_list_dataframe.to_excel(writer, sheet_name='Sector')
    sector_list_dataframe.to_csv('/home/dudals3844/Financial_Engneering/data/sector_breakdown.csv', mode='w')
    writer.close()
    

Sector_breakdown()