# Clear duplicates from Dropbox backup
import json
from icalendar import Calendar, Event

print('Enter the file (and path if needed) for your Nomie backup.')
try:
    fileName = input('> ')
except:
    print('Re-input. Program has fallen back to Python 2.x protocols')
    fileName = raw_input('> ')
file = open(fileName)
dataRaw = file.read()

data = json.loads(dataRaw)
# Event fields: title, startdate, enddate, description, geo
events = data['events']
calendarEvents = []
for i in events:
    print(i)
    toAdd = None # TODO: Built calendar event
    calendarEvents += [toAdd]

cal = Calendar()
for i in events:
    event = Event()
    event.add('summary', i['description'])
    event.add('dtstart', i['startdate'])
    event.add('dtend', i['enddate'])
    event.add('location', i['geo'])
    cal.add_component(event)

# Print ical contents
print(cal.to_ical())
