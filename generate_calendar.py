import requests

# API endpoint from Lehigh University's LINC platform
eventEndsAfterDate = "2025-08-01T00%3A31%3A10-04%3A00" # Start date for the query: first day of August for Fall 2025 semester
                                                       # In the string format of "%Y-%m-%dT%H%%3A%M%%3A%S-04%%3A00"
url = f"https://lehigh.campuslabs.com/engage/api/discovery/event/search?orderByField=endsOn&orderByDirection=ascending&status=Approved&query=&take=1000&endsAfter={eventEndsAfterDate}"

# Fetch the data
response = requests.get(url)
data = response.json()

# Get and print event info
for event in data.get("value", []):
    name = event.get("name")
    organizationName = event.get("organizationName")
    location = event.get("location")
    starts_on = event.get("startsOn")
    ends_on = event.get("endsOn")
    description = event.get("description")

    print(name)
    print(f"Organization: {organizationName}")
    print(f"Location: {location}")
    print(f"Starts: {starts_on}")
    print(f"Ends: {ends_on}")
    print(f"Description: {description}")
    print()