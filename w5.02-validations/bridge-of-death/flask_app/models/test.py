from datetime import datetime

today = "03-20-2024"
today_date_object = datetime.strptime(today, "%m-%d-%Y")
print(type(today_date_object))
