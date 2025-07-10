import requests
from html import escape

# API endpoint from Lehigh University's LINC platform
eventEndsAfterDate = "2025-08-01T00%3A31%3A10-04%3A00" # Start date for the query: first day of August for Fall 2025 semester
                                                       # String format: "%Y-%m-%dT%H%%3A%M%%3A%S-04%%3A00"
url = f"https://lehigh.campuslabs.com/engage/api/discovery/event/search?orderByField=endsOn&orderByDirection=ascending&status=Approved&query=&take=1000&endsAfter={eventEndsAfterDate}"

# Fetch the data
response = requests.get(url)
data = response.json()

# Build HTML
html = """
<html>
    <head>
        <meta charset="UTF-8">
        <title>Lehigh Events</title>
        <style>
        </style>
    </head>
    <body>
        <h1>Fall 2025 Events</h1>
"""

# Get event info and add to HTML
for event in data.get("value", []):
    name = escape(event.get("name", ""))
    organizationName = escape(event.get("organizationName", ""))
    location = escape(event.get("location", ""))
    starts_on = escape(event.get("startsOn", ""))
    ends_on = escape(event.get("endsOn", ""))
    description = event.get("description", "")

    html += f"""
    <h2>{name}</h2>
    <p>Organization: {organizationName}</p>
    <p>Location: {location}</p>
    <p>Start: {starts_on}</p>
    <p>End: {ends_on}</p>
    <p>Description: {description}</p>
    """

html += "</body></html>"

# Save generated HTML to a file under the html directory
with open("html/event_calendar.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML file generated!!")