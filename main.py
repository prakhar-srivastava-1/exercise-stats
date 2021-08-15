from nutritionix import Nutritionix

# add a call to Nutritionix to get info from API
nutritionix = Nutritionix()
nutritionix.send_query(age=26, weight=75)
# save data
nutritionix_data = nutritionix.clean_data()
print(nutritionix_data)

# add a call to Google Sheets API to save the captured data