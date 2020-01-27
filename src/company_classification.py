import pandas as pd
from pandas import ExcelWriter
import xlsxwriter

def company_classification():
    sector_breakdown = pd.read_excel('/home/dudals3844/Financial_Engneering/data/sector_breakdown.xlsx', sheet_name='Sector', encoding = 'utf-8')
    companys = pd.read_excel('/home/dudals3844/Financial_Engneering/data/kospi.xls', sheet_name='Sheet1', encoding = 'utf-8')
    
    for sector in sector_breakdown[0]:
        sector_company_list = []
        for idx in range(0, len(companys)):
            if(sector == companys['업종'][idx]):
                sector_company_list.append(companys['기업명'][idx])
                
        
        sector_company_list_df = pd.DataFrame(sector_company_list)
        file_name = '/home/dudals3844/Financial_Engneering/data/sector/'+sector+'.xlsx'
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        sector_company_list_df.to_excel(writer, sheet_name='company_list')
        writer.close()

company_classification()