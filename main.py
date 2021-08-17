from nutritionix import Nutritionix
import datetime as dt
from google_sheets import GoogleSheets

# add a call to Nutritionix to get info from API
nutritionix = Nutritionix()
weight = float(input("Current Weight?\t"))
nutritionix.send_query(weight, age=26)
# save data
nutritionix_data = nutritionix.clean_data()
# print(nutritionix_data)

# capture date and time
curr_datetime = dt.datetime.now()
# current date (formatted)
curr_date = curr_datetime.strftime('%d/%m/%Y')
# current time (formatted)
curr_time = curr_datetime.strftime('%H:%M:%S')

entries = list()
for task in nutritionix_data:
    entry = list()
    entry.append(curr_date)
    entry.append(curr_time)
    entry.append(task["name"])
    entry.append(float(task["duration_min"]))
    entry.append(float(task["nf_calories"]))
    entry.append(weight)
    entries.append(entry)

# add a call to Google Sheets API to save the captured data
google = GoogleSheets()
google.get_current_rows()
if google.write_new_stats(entries=entries):
    print("New stats successfully added!")
else:
    print("Error! Something went wrong.")
