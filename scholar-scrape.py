import requests
from bs4 import BeautifulSoup
import time

MANAGEMENT_SCIENCE = "management science"
ECONOMICS = "economics"

authors_list = ["Chris Forman", "Aija Leiponen", "Matt Marx", "Deborah Streeter"]

# MANAGEMENT SCIENCE
print("MANAGEMENT SCIENCE!!!!!!!!\n")
for author in authors_list:
    # Construct URL for each Google Scholar search
    source = MANAGEMENT_SCIENCE
    query = f"author:{author}+source:{source}"
    url = f"https://scholar.google.com/scholar?q={query}"
    headers = {'User-Agent': 'ScrapingBizSchoolManagementFaculty/1.0 (+https://mackinstitute.wharton.upenn.edu)'}

    # send GET request to retrieve html content
    response = requests.get(url, headers)

    if response.ok:
        html_content = response.text

        # parsing html result to extract meaningful info
        soup = BeautifulSoup(html_content, "html.parser")

        # extract all items from search results
        result_items = soup.find_all("div", class_="gs_r")

        for item in result_items:
            title = item.find("h3", class_="gs_rt")
            other_info = item.find("div", class_="gs_a")
            other_info_text = other_info.text.strip()
            
            if source.lower() in other_info_text.lower():
                if title:
                    print("Title:", title.text.strip())
                
                if other_info and source.lower() in other_info_text.lower():
                    print("Authors and Publication Info:", other_info_text)

                print()
    else:
        print("Request was not successful.", response.status_code)

    time.sleep(5) # wait before making next request

# ECONOMICS
print("\nECONOMICS!!!!!!!!\n")
for author in authors_list:
    # Construct URL for each Google Scholar search
    source = ECONOMICS
    query = f"author:{author}+source:{source}"
    url = f"https://scholar.google.com/scholar?q={query}"
    headers = {'User-Agent': 'ScrapingBizSchoolManagementFaculty/1.0 (+https://mackinstitute.wharton.upenn.edu)'}

    # send GET request to retrieve html content
    response = requests.get(url, headers)

    if response.ok:
        html_content = response.text

        # parsing html result to extract meaningful info
        soup = BeautifulSoup(html_content, "html.parser")

        # extract all items from search results
        result_items = soup.find_all("div", class_="gs_r")

        for item in result_items:
            title = item.find("h3", class_="gs_rt")
            other_info = item.find("div", class_="gs_a")
            other_info_text = other_info.text.strip()
            
            if source.lower() in other_info_text.lower():
                if title:
                    print("Title:", title.text.strip())
                
                if other_info and source.lower() in other_info_text.lower():
                    print("Authors and Publication Info:", other_info_text)

                print()
    else:
        print("Request was not successful.", response.status_code)

    time.sleep(5) # wait before making next request