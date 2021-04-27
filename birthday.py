import datetime

birthdayMonth = 4
birthdayDay = 30
name = 'Rebecca'

# Get today's date
t=datetime.date.today()
# Create date object for birthday
bd=datetime.date(t.year, birthdayMonth, birthdayDay)

# if today > birthday compare again with year + 1
if t > bd :
    # print('Birthday is before today')
    nextYear = t.year + 1
    bd=datetime.date(nextYear, birthdayMonth, birthdayDay)
    # print('Birthday changed to ' , bd)

# Compare today's date to birthday and return days until
delta = bd - t
difference = delta.days.__str__()

# If delta < 33 days = output message to terminal
if delta.days < 33 :
    print(name + "'s birthday is in "+difference+" days.")




