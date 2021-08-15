from nutritionix import Nutritionix

# add a call to Nutritionix to get info from API
nutritionix = Nutritionix()
print(nutritionix.send_query(age=26, weight=75))
