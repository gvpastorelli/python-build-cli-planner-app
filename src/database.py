import csv
from typing import Type
from src.deadlined_reminders import DeadlinedReminder

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):
    if not issubclass(ReminderClass, DeadlinedReminder):
        raise TypeError("Invalid Reminder Class")
    with open('reminders.csv', 'a+', newline='\n') as file:
        reminder = ReminderClass(text, date)
        writer = csv.writer(file)
        writer.writerow(reminder)
