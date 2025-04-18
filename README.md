# Propertyguru
This Python web scraper is designed to extract real estate listings from PropertyGuru Singapore across multiple pages. The scraper collects detailed information for each property, helping in real estate data analysis, price comparison, and property trend monitoring.

Extracted Data Fields:
Title – The headline of the property listing.

Location – The address or locality of the property.

Price – The listed price of the property.

Bedrooms – Number of bedrooms available in the property.

Bathrooms – Number of bathrooms available in the property.

Square Feet – The area of the property in square feet.

PSF (Price per Square Foot) – Price per square foot value.

Type – The type of property (e.g., Condo, HDB, Landed).

Lease Hold – Lease duration (e.g., Freehold, 99-Year Lease).

Agent Name – The name of the real estate agent managing the listing.

Description – A brief detail/overview about the property.

Image Link – The main image URL associated with the listing.

Listed Date – The date when the property was listed.

Features:
Automatically scrapes multiple pages.

Uses rotating User-Agents and realistic headers to bypass basic bot detection.

Includes random delays to mimic human browsing behavior.

Saves the data to a structured CSV file for further use in analysis or dashboards.
