import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import random
import time

ua = UserAgent()

session = requests.Session()

headers = {
    "User-Agent": ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": random.choice(["en-US", "en-GB", "fr-FR", "de-DE", "es-ES"]),
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.propertyguru.com.sg/property-for-sale", 
}

content = []

for page in range(1, 51):  
    target_url = f'https://www.propertyguru.com.sg/property-for-sale?page={page}'

    response = session.get(target_url, headers=headers)
    print(f"Scraping Page {page} - Status:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h3', class_='listing-title')
        locations = soup.find_all('div', class_='listing-address')
        prices = soup.find_all('div', attrs={'da-id': 'lc-price'})
        bedrooms = soup.find_all('i', class_='pgicon pgicon-bedroom')
        bathrooms = soup.find_all('i', class_='pgicon pgicon-bathroom')
        square_feet = soup.find_all('ul', class_='listing-feature-group')
        psf = soup.find_all('ul', class_='listing-feature-group')
        types = soup.find_all('div', class_='listing-property-group')
        lease_hold = soup.find_all('div', class_='listing-property-group')
        agent_names = soup.find_all('a', class_='actionable-link agent-name')
        descriptions = soup.find_all('div', class_='info-description')
        target_divs = soup.find_all('div', class_='swiper-slide swiper-carousel-item')
        listed_dates = soup.find_all('ul', class_='listing-recency')

        for i in range(len(titles)):
            bedroom = bedrooms[i].find_parent().get_text(strip=True) if i < len(bedrooms) else None
            bathroom = bathrooms[i].find_parent().get_text(strip=True) if i < len(bathrooms) else None

            square = psf_value = None
            if i < len(square_feet):
                info_list = square_feet[i].find_all('li', attrs={'da-id': 'lc-gallery-info-group-item'})
                if len(info_list) >= 4:
                    square = info_list[2].get_text(strip=True)
                    psf_tag = info_list[3].find('span', class_='info-value')
                    psf_value = psf_tag.get_text(strip=True) if psf_tag else None

            lease = None
            if i < len(lease_hold):
                lease_tags = lease_hold[i].find_all('span', {'da-id': 'lc-info-badge'})
                if len(lease_tags) >= 3:
                    lease = lease_tags[2].get_text(strip=True)

            prop_type = None
            if i < len(types):
                type_tags = types[i].find_all('span', {'da-id': 'lc-info-badge'})
                if len(type_tags) >= 2:
                    prop_type = type_tags[1].get_text(strip=True)

            image_url = target_divs[i].find('img')['src'] if i < len(target_divs) and target_divs[i].find('img') else None

            property_data = {
                "title": titles[i].get_text(strip=True),
                "location": locations[i].get_text(strip=True) if i < len(locations) else None,
                "price": prices[i].get_text(strip=True) if i < len(prices) else None,
                "bedrooms": bedroom,
                "bathrooms": bathroom,
                "square_feet": square,
                "psf": psf_value,
                "type": prop_type,
                "lease_hold": lease,
                "agent_name": agent_names[i].get_text(strip=True) if i < len(agent_names) else None,
                "description": descriptions[i].get_text(strip=True) if i < len(descriptions) else None,
                "image": image_url,
                "listed_date": listed_dates[i].get_text(strip=True) if i < len(listed_dates) else None
            }

            content.append(property_data)

        time.sleep(random.uniform(2, 5))

    else:
        print(f"Request failed with status: {response.status_code}")

df = pd.DataFrame(content)
df.to_csv('C:\\Users\\HM Laptops\\Desktop\\Sample\\Property_scrap.csv', index=False)
print("✅ Data saved to CSV.")