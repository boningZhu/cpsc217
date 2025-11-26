# created by : Bonnie Zhu
# created on : 11/22

import requests
from bs4 import BeautifulSoup

# 1. Download the page
url = "https://ottersarecute.com/bluejays.html"
response = requests.get(url)
print("Status code:", response.status_code)

# 2. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. Find the batting stats table (same id as in slides)
stats_table = soup.find("table", id="players_standard_batting")

# 4. Loop through the rows and print the player names
for tr in stats_table.tbody.find_all("tr"):
    cells = tr.find_all("td")
    if not cells:
        break        # stop when we hit the “totals” or empty row
    name = cells[0].get_text(strip=True)
    print(name)
