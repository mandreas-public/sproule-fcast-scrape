import requests
import datetime
import pandas as pd

# Get dates for file download 
now = datetime.date.today()

prev_year = now.year
prev_month = now.month - 1
month = now.month
year = now.year

if now.month == 1:
    prev_year = year - 1
    prev_month = 12

prev_year = '{:02d}'.format(prev_year)
prev_month = '{:02d}'.format(prev_month)
month = '{:02d}'.format(month)
year = '{:04d}'.format(year)

# Example URL: https://sproule.com/wp-content/uploads/2021/09/2021-08-Constant.xlsx

file_string = f'{prev_year}-{prev_month}-Constant'
url = f'https://sproule.com/wp-content/uploads/{year}/{month}/{file_string}.xlsx'

# Download File
xl_df = pd.read_excel(url, 
                    sheet_name='Constant Prices',
                    header=7,
                    index_col=1)

# Transform Excel sheet to dataframe
xl_df = xl_df.iloc[:14]
xl_df = xl_df.dropna(how='all').drop(xl_df.columns[0], axis=1)
xl_df = xl_df.reset_index().rename(columns={'index':'Month'})

# Save 
xl_df.to_csv(f'files/{file_string}.csv')

#with open(file_string, 'wb') as f:
#    f.write(r.content)