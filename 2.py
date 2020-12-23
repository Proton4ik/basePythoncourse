seconds_per_hour = 3600
seconds_per_minute = 60
user_seconds = int(input("Введите количество секунд в виде целого числа: "))
hours = user_seconds // seconds_per_hour
remaining_seconds = user_seconds - (hours * seconds_per_hour)
minutes = remaining_seconds // seconds_per_minute
seconds = remaining_seconds - (minutes * seconds_per_minute)
print ("Время: {} ч {} минут {} секунд." .format(hours, minutes, seconds))
print ("Конец программы.")



