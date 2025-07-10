# Lehigh-Event-Calendar
Forget fiddling with calendars. This app shows all upcoming Lehigh University events in one spot and lets you pick ones you're interested in to drop straight into your virtual calendar. This project started as a fun way to finally put the dusty old e-ink Kindle to use instead of squinting at oversized academic calendar printouts taped to the wall.

generate_calendar.py generates an HTML file of the event calendar.
As older Kindle e-reader devices have limited or no support for JavaScript, which is needed for refreshing and fetching event data. Thus, create a server side endpoint to return the updated data. You may set up a job on your computer or Raspberry Pi, or use hosting services like GitHub Pages.

App Breakdown
* Calendar Page
  - Toggle showing calendar events in month or week view.
  - Consist of events marked as "interested".
* Upcoming Events Page
  - Display list of upcoming events with name, origanization name, location, time, and description.
  - Events can be marked as "interested".
* More paes and functionalities to be determined...