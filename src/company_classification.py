import pandas as pd

def company_classification():
    sector_breakdown = pd.read_excel('/home/dudals3844/Financial_Engneering/data/sector_breakdown.xlsx', sheet_name='Sector', encoding = 'utf-8')
    company = pd.read_excel('/home/dudals3844/Financial_Engneering/data/kospi.xls', sheet_name='Sheet1', encoding = 'utf-8')
    
    # print(sector_breakdown[0])
    for sector in sector_breakdown[0]:
        print(sector)

company_classification()