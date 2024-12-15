from datetime import datetime, timedelta

def is_advent(d: datetime):
    return d <= datetime(d.year, 12, 24) < d + timedelta(weeks=4)

current_date = datetime(2020, 4, 3) # starter med å legge inn de to første dagene manuelt
end_date = datetime(2024, 12, 12)
sunday_counter = 0
nums = [1, 1]
while current_date <= end_date:
    if current_date.weekday() == 6: # søndag
        sunday_counter += 1
    if (
        current_date.weekday() == 6 and (
            sunday_counter == 3
            or (current_date.month == 7) # juli
            or is_advent(current_date)
        )
    ):
        sunday_counter = 0
        nums.extend([0, 1])
        current_date += timedelta(days=1)
    else:
        nums.append(nums[-1] + nums[-2])
    current_date += timedelta(days=1)
print(sum(nums))