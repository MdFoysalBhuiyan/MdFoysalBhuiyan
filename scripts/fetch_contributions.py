import os
import json
import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_PROFILE_USER", "MdFoysalBhuiyan")

URL = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

contributions = []

# GitHub's contribution calendar uses elements with this class
days = soup.select(".ContributionCalendar-day")

print(f"Found {len(days)} contribution cells.")

for day in days:
    date = day.get("data-date")
    level = day.get("data-level")

    if date and level is not None:
        contributions.append({
            "date": date,
            "level": int(level)
        })

os.makedirs("data", exist_ok=True)

with open("data/contributions.json", "w", encoding="utf-8") as f:
    json.dump(contributions, f, indent=2)

print(f"Saved {len(contributions)} contribution days.")