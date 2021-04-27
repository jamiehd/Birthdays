import datetime

birthdayMonth = 4
birthdayDay = 30
name = 'Rebecca'

# Get today's date
todaysDate=datetime.date.today()
# Create date object for birthday
birthdayDate=datetime.date(todaysDate.year, birthdayMonth, birthdayDay)

# if today > birthday, set birthday to next year.
if todaysDate > birthdayDate :
    nextYear = t.year + 1
    birthdayDate=datetime.date(nextYear, birthdayMonth, birthdayDay)

# Compare today's date to birthday and return days until
delta = birthdayDate - todaysDate
difference = delta.days

# If delta < 33 days = output message to terminal
if delta.days < 33 :
    print(name + "'s birthday is in", difference, "days.")




