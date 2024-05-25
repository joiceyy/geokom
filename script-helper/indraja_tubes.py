import pandas as pd
import glob
import os

# Specify the directory containing the Excel files
directory = '2018\METEOROLOGI'

# Use glob to find all Excel files in the directory
excel_files = glob.glob(os.path.join(directory, '*.xlsx'))

# Initialize a list to hold dataframes
dataframes = []

# Loop through the Excel files and read them into dataframes
annual_sum = 0.0
cnt_data = 0
new_data_list = []
month_data = []
rr_data = []
for file in excel_files:
    print(file)
    raw_data = pd.read_excel(file)
    df = raw_data.duplicated()
    df = raw_data.drop(raw_data.columns[2], axis=1)
    # Regex pattern for 'DD-MM-YYYY'
    pattern = r'\d{2}-\d{2}-\d{4}'

    # Filter rows where 'date' column matches the pattern
    filtered_df = df[df.iloc[:, 0].str.contains(pattern, regex=True, na=False)]
    filtered_df = filtered_df[(filtered_df.iloc[:, 1] != 8888) & (filtered_df.iloc[:, 1] != 9999)]

    column_name_0 = filtered_df.columns[0]
    column_name_1 = filtered_df.columns[1]

    monthly_sum = filtered_df.iloc[:, 1].sum()
    if monthly_sum != 0.0:
        cnt_data = cnt_data + 1
        annual_sum = annual_sum + monthly_sum


    new_row = {
      column_name_0: 'Total RR',
      column_name_1: monthly_sum
    }

    new_data = {
        'Bulan': file,
        'RR': monthly_sum
    }

    month_data.append(file)
    rr_data.append(monthly_sum)

    new_row_df = pd.DataFrame([new_row])
    raw_data = pd.concat([raw_data, new_row_df], ignore_index=True)
    raw_data.to_excel(file, index=False, engine='openpyxl')

month_data.append("")
month_data.append("Total")
rr_data.append("")
rr_data.append(annual_sum)
new_data = {
    'Bulan': month_data,
    'RR': rr_data
}

print(annual_sum)
new_df_data = pd.DataFrame(new_data)
new_df_data.to_excel(directory + '/data_tahun.xlsx', index=False, engine='openpyxl')