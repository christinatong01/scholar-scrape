import requests
from bs4 import BeautifulSoup
import time

MANAGEMENT_SCIENCE = "management science"
ECONOMICS = "economics"

# authors_list = ["Chris Forman", "Aija Leiponen", "Matt Marx", "Deborah Streeter"]
authors_list = ["Ron Adner", "Pino Audia", "Sydney Finkelstein", "Giovanni Gavetti", "Vijay Govindarajan", "Constance E Helfat", "Hart Posen", "Ella L.J. Bell Smith", "John M Doris", "Eric Abrahamson", "Modupe Akinola", "Daniel Ames", "Joel Brockner", "Meyer Feldberg", "Adam Galinsky", "Kathryn Harrigan", "E Tory Higgins", "Raymond Horton", "Paul Ingram", "Sheena Iyengar", "Bruce Kogut", "Stephan Meier", "Malia Mason", "Michael Morris", "Sushil Bikchandani", "M Keith Chen", "Magali Delmas", "Marvin Lieberman", "John W Mamer", "Mariko Sakakibara", "Olav Sorenson", "Wes Yin", "Pierre Azoulay", "Michael Cusumano", "Fiona E Murray", "Edward Roberts", "Scott Stern", "Eric Arthur von Hippel", "Ezra W Zuckerman Sivan", "Ramon Casadesus-Masanell", "Juan Alcacer", "Bharat N Anand", "Felix Oberholzer-Gee", "Michael E Porter", "Jan W Rivkin", "Rebecca M Henderson", "Raffaella Sadun", "Tarun Khanna", "Eric J Van den Steen", "Dennis A Yao", "David B Yoffie", "Cynthia A Montgomery"]

# MANAGEMENT SCIENCE
print("MANAGEMENT SCIENCE!!!!!!!!\n")
for author in authors_list:
    print(author)

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
            other_info_text = other_info.text.strip() if other_info else ""
            
            if source.lower() in other_info_text.lower():
                if title:
                    print("Title:", title.text.strip())
                
                if other_info and source.lower() in other_info_text.lower():
                    print("Authors and Publication Info:", other_info_text)

                print()
        time.sleep(5) # wait before making next requestß
    else:
        print("Request was not successful.", response.status_code)

# ECONOMICS
# print("\nECONOMICS!!!!!!!!\n")
# for author in authors_list:
#     print(author)

#     # Construct URL for each Google Scholar search
#     source = ECONOMICS
#     query = f"author:{author}+source:{source}"
#     url = f"https://scholar.google.com/scholar?q={query}"
#     headers = {'User-Agent': 'ScrapingBizSchoolManagementFaculty/1.0 (+https://mackinstitute.wharton.upenn.edu)'}

#     # send GET request to retrieve html content
#     response = requests.get(url, headers)

#     if response.ok:
#         html_content = response.text

#         # parsing html result to extract meaningful info
#         soup = BeautifulSoup(html_content, "html.parser")

#         # extract all items from search results
#         result_items = soup.find_all("div", class_="gs_r")

#         for item in result_items:
#             title = item.find("h3", class_="gs_rt")
#             other_info = item.find("div", class_="gs_a")
#             other_info_text = other_info.text.strip()
            
#             if source.lower() in other_info_text.lower():
#                 if title:
#                     print("Title:", title.text.strip())
                
#                 if other_info and source.lower() in other_info_text.lower():
#                     print("Authors and Publication Info:", other_info_text)

#                 print()
#         time.sleep(5) # wait before making next request
#     else:
#         print("Request was not successful.", response.status_code)