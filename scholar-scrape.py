import requests
from bs4 import BeautifulSoup
import time
# from ratelimit import limits

FIFTEEN_MINUTES = 900
MANAGEMENT_SCIENCE = "management science"
ECONOMICS = "economics"

# authors_list = ["Chris Forman", "Aija Leiponen", "Matt Marx", "Deborah Streeter"]
# authors_list = ["Ron Adner", "Pino Audia", "Sydney Finkelstein", "Giovanni Gavetti", "Vijay Govindarajan", "Constance E Helfat", "Hart Posen", "Ella L.J. Bell Smith", "John M Doris", "Eric Abrahamson", "Modupe Akinola", "Daniel Ames", "Joel Brockner", "Meyer Feldberg", "Adam Galinsky", "Kathryn Harrigan", "E Tory Higgins", "Raymond Horton", "Paul Ingram", "Sheena Iyengar", "Bruce Kogut", "Stephan Meier", "Malia Mason", "Michael Morris", "Sushil Bikchandani", "M Keith Chen", "Magali Delmas", "Marvin Lieberman", "John W Mamer", "Mariko Sakakibara", "Olav Sorenson", "Wes Yin", "Pierre Azoulay", "Michael Cusumano", "Fiona E Murray", "Edward Roberts", "Scott Stern", "Eric Arthur von Hippel", "Ezra W Zuckerman Sivan", "Ramon Casadesus-Masanell", "Juan Alcacer", "Bharat N Anand", "Felix Oberholzer-Gee", "Michael E Porter", "Jan W Rivkin", "Rebecca M Henderson", "Raffaella Sadun", "Tarun Khanna", "Eric J Van den Steen", "Dennis A Yao", "David B Yoffie", "Cynthia A Montgomery"]
# authors_list = ["Ryan W Buell", "Amitabh Chandra", "Amy C Edmonson", "Frances X Frei", "Shane M Greenstein", "Gary P Pisano", "Janice H Hammond", "Ananth Raman", "Marco Iansiti", "Willy C Shih", "Karim R Lakhani", "Stefan H Thomke", "Michael W Toffel", "Feng Zhu", "Thomas R Eisenmann", "Teresa M Amabile", "Lynda M Applegate", "Josh Lerner", "Shai Benjamin Bernstein", "Lauren H Cohen", "Tom Nicholas", "Mihir A Desai", "Joseph B Fuller", "William A Sahlman", "Shikhar Ghosh", "Paul A Gompers", "Ranjay Gulati", "William R Kerr", "Mitchell B Weiss", "Ashish Arora", "Sharon Belenzon", "Aaron Chatterji", "Wesley Cohen", "David Besanko", "Sally Blount", "David Dranove", "Craig Garthwaite", "Thomas N Hubbard", "Benjamin F Jones", "Niko Matouschek", "Michael Mazzeo", "Therese J McGuire", "Luis Rayo", "Morton Shapiro", "Daniel Spulber", "Jeroen Swinkels", "Ernesto Dal Bo", "Frederico Finan", "Ann E Harrison", "Steven Tadelis", "Franceso Trebbi", "Pamela Hinds", "Itai Ashlagi", "Nicholas Bambos", "Jose Humberto Blanchet Mancilla", "Margaret Brandeau", "Thomas Byers", "Kathleen Eisenhardt", "Kay Giesecke", "Peter Glynn", "Ashish Goel", "Ramesh Johari", "Riitta Katila", "M Elisabeth Pate-Cornell", "Amin Saberi", "Robert Sutton", "James Sweeney", "Benjamin Van Roy", "John Weyant", "Yinyu Ye", "Allan Afuah", "Felipe Csaszar", "Michael Jensen", "Aneel Karnani", "Jordan Siegel", "Jim Walsh", "James Westphal", "Brian Wu"]
# authors_list = ["Pierre Azoulay", "Michael Cusumano", "Fiona E Murray", "Edward Roberts", "Scott Stern", "Eric Arthur von Hippel", "Ezra W Zuckerman Sivan", "Ramon Casadesus-Masanell", "Juan Alcacer", "Bharat N Anand", "Felix Oberholzer-Gee", "Michael E Porter", "Jan W Rivkin", "Rebecca M Henderson", "Raffaella Sadun", "Tarun Khanna", "Eric J Van den Steen", "Dennis A Yao", "David B Yoffie", "Cynthia A Montgomery", "Ryan W Buell", "Amitabh Chandra", "Amy C Edmonson", "Frances X Frei", "Shane M Greenstein", "Gary P Pisano", "Janice H Hammond", "Ananth Raman", "Marco Iansiti", "Willy C Shih", "Karim R Lakhani", "Stefan H Thomke", "Michael W Toffel", "Feng Zhu", "Thomas R Eisenmann", "Teresa M Amabile", "Lynda M Applegate", "Josh Lerner", "Shai Benjamin Bernstein", "Lauren H Cohen", "Tom Nicholas", "Mihir A Desai", "Joseph B Fuller", "William A Sahlman", "Shikhar Ghosh", "Paul A Gompers", "Ranjay Gulati", "William R Kerr", "Mitchell B Weiss", "Ashish Arora", "Sharon Belenzon", "Aaron Chatterji", "Wesley Cohen", "David Besanko", "Sally Blount", "David Dranove", "Craig Garthwaite", "Thomas N Hubbard", "Benjamin F Jones", "Niko Matouschek", "Michael Mazzeo", "Therese J McGuire", "Luis Rayo", "Morton Shapiro", "Daniel Spulber", "Jeroen Swinkels", "Ernesto Dal Bo", "Frederico Finan", "Ann E Harrison", "Steven Tadelis", "Franceso Trebbi", "Pamela Hinds", "Itai Ashlagi", "Nicholas Bambos", "Jose Humberto Blanchet Mancilla", "Margaret Brandeau", "Thomas Byers", "Kathleen Eisenhardt", "Kay Giesecke", "Peter Glynn", "Ashish Goel", "Ramesh Johari", "Riitta Katila", "M Elisabeth Pate-Cornell", "Amin Saberi", "Robert Sutton", "James Sweeney", "Benjamin Van Roy", "John Weyant", "Yinyu Ye", "Allan Afuah", "Felipe Csaszar", "Michael Jensen", "Aneel Karnani", "Jordan Siegel", "Jim Walsh", "James Westphal", "Brian Wu"]
# authors_list = ["James Westphal", "Brian Wu"]
# authors_list = ["Mihir A Desai", "Joseph B Fuller", "William A Sahlman", "Shikhar Ghosh", "Paul A Gompers", "Ranjay Gulati", "William R Kerr", "Mitchell B Weiss", "Ashish Arora", "Sharon Belenzon", "Aaron Chatterji", "Wesley Cohen", "David Besanko", "Sally Blount", "David Dranove", "Craig Garthwaite", "Thomas N Hubbard", "Benjamin F Jones", "Niko Matouschek", "Michael Mazzeo", "Therese J McGuire", "Luis Rayo", "Morton Shapiro", "Daniel Spulber", "Jeroen Swinkels", "Ernesto Dal Bo", "Frederico Finan", "Ann E Harrison", "Steven Tadelis", "Franceso Trebbi", "Pamela Hinds", "Itai Ashlagi", "Nicholas Bambos", "Jose Humberto Blanchet Mancilla", "Margaret Brandeau", "Thomas Byers", "Kathleen Eisenhardt", "Kay Giesecke", "Peter Glynn", "Ashish Goel", "Ramesh Johari", "Riitta Katila", "M Elisabeth Pate-Cornell", "Amin Saberi", "Robert Sutton", "James Sweeney", "Benjamin Van Roy", "John Weyant", "Yinyu Ye", "Allan Afuah", "Felipe Csaszar", "Michael Jensen", "Aneel Karnani", "Jordan Siegel", "Jim Walsh"]
# authors_list = ["Magali Delmas",  "Marvin Lieberman"]
authors_list = ["Juan Alcacer","Felix Oberholzer-Gee" ]
# MANAGEMENT SCIENCE
# print("MANAGEMENT SCIENCE!!!!!!!!\n")
# for author in authors_list:
#     print(author)

#     # Construct URL for each Google Scholar search
#     source = MANAGEMENT_SCIENCE
#     query = f"author:{author}+source:{source}"
#     url = f"https://scholar.google.com/scholar?q={query}"
#     headers = {'User-Agent': 'ScrapingBizSchoolSeniorManagementFaculty/3.0'}

#     # send GET request to retrieve html content
#     response = requests.get(url, headers)
#     time.sleep(FIFTEEN_MINUTES) # wait before making next requestß

#     if response.ok:
#         html_content = response.text

#         # parsing html result to extract meaningful info
#         soup = BeautifulSoup(html_content, "html.parser")

#         # extract all items from search results
#         result_items = soup.find_all("div", class_="gs_r")

#         for item in result_items:
#             title = item.find("h3", class_="gs_rt")
#             other_info = item.find("div", class_="gs_a")
#             other_info_text = other_info.text.strip() if other_info else ""
            
#             if source.lower() in other_info_text.lower():
#                 if title:
#                     print("Title:", title.text.strip())
                
#                 if other_info and source.lower() in other_info_text.lower():
#                     print("Authors and Publication Info:", other_info_text)

#                 print()
#     else:
#         print("Request was not successful.", response.status_code)

# ECONOMICS
print("\nECONOMICS!!!!!!!!\n")
for author in authors_list:
    print(author)

    # Construct URL for each Google Scholar search
    source = ECONOMICS
    query = f"author:{author}+source:{source}"
    url = f"https://scholar.google.com/scholar?q={query}"
    headers = {'User-Agent': 'ScrapingBizSchoolManagementFaculty/5.0 (+https://mackinstitute.wharton.upenn.edu)'}

    # send GET request to retrieve html content
    response = requests.get(url, headers)
    time.sleep(10) # wait before making next requestß

    if response.ok:
        html_content = response.text

        # parsing html result to extract meaningful info
        soup = BeautifulSoup(html_content, "html.parser")

        # extract all items from search results
        result_items = soup.find_all("div", class_="gs_r")
        print(result_items)

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
    else:
        print("Request was not successful.", response.status_code)