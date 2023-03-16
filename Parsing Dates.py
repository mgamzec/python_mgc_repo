# Provide the correct format for the date -08/17/1978
date_data_three = pd.to_datetime(date_data_three, format="%m/%d/%Y")
print(date_data_three)

# Provide the correct format for the date - 2016 March 01 01:56
date_data_four = pd.to_datetime(date_data_four, format="%Y %B %d %H:%M")
print(date_data_four)

""" 
Detailed from website:
https://strftime.org

"""

