from bs4 import BeautifulSoup
from requests import get

def extract_text(element):
    return element.get_text().strip() if element else ''

# Get the username from user input
user = input("> Enter username: ")

# Send a GET request to the npmjs website to fetch the HTML content of the user's profile
url = f"https://www.npmjs.com/~{user}"
response = get(url)
html = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract the user's profile image URL
img_element = soup.select_one("div._73a8e6f0 a img")
img = "https://npmjs.com" + img_element.get("src") if img_element else "NA"

# Extract the username
username_element = soup.select_one("h2.b219ea1a")
username = extract_text(username_element) if username_element else "NA"

# Extract the name
name_element = soup.select_one("div._73a8e6f0 div.eaac77a6")
name = extract_text(name_element) if name_element else "NA"

# Extract social links
social_elements = soup.select("ul._07eda527 li._43cef18c a._00cd8e7e")
social = [e.get("href") for e in social_elements]

# Extract the total number of packages
total_packages_element = soup.select_one("div#tabpanel-packages h2.f3f8c3f4 span.c5c8a11c")
total_packages = extract_text(total_packages_element) if total_packages_element else "NA"

# Extract the titles, descriptions, and published information of the packages
package_elements = soup.select("div._0897331b ul._0897331b li._2309b204")
packages = []
for element in package_elements:
    title_element = element.select_one("h3.db7ee1ac")
    description_element = element.select_one("p._8fbbd57d")
    published_element = element.select_one("span._66c2abad")

    package = {
        'title': extract_text(title_element),
        'description': extract_text(description_element),
        'published': extract_text(published_element)
    }
    packages.append(package)

# Create a dictionary containing all the extracted data
data = {
    'image': img,
    'username': username,
    'name': name,
    'social': social,
    'total_packages': total_packages,
    'latest_packages': packages
}

# Print the data dictionary
print(data)
