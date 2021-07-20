
# You Have to DO All tasks on that given Dictionary of Complany List
companyList = [ 
    {
        "Company Name": "Roshan",
        "Company Motto": "Roshan began operations in 2003 in an environment where there was virtually no telecommunications infrastructure.",
        "City": "Kabul",
        "Country": "Afghanistan",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshan.af",
            "Website": "http://www.roshan.af/"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/RoshanConnects",
            "Twitter": "https://www.twitter.com/roshanconnects",
            "LinkedIn": "https://www.linkedin.com/company/roshan"
        }
    }, 
    {
        "Company Name": "Gjirafa",
        "Company Motto": "Gjirafa is a video content and e-commerce platform for the Balkans built on top of an Albanian language specialized search engine.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "37744991206",
            "Email": "info@gjirafa.com",
            "Website": "http://www.gjirafa.com/"
        },
        "Social Accounts": {
            "Facebook": "http://www.facebook.com/gjirafa",
            "Twitter": "https://twitter.com/gjirafashqip",
            "LinkedIn": "https://www.linkedin.com/company/gjirafa-inc-"
        }
    },
    {
        "Company Name": "Shqiperia Com",
        "Company Motto": "ShqiperiaCom primarily provides web developing services and consultancy in the region of Balkan.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "35542403910",
            "Email": "mandi@shqiperia.com",
            "Website": "http://www.shqiperiacom.info"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/shqiperiacom",
            "Twitter": "http://twitter.com/ShqiperiaCom",
            "LinkedIn": "https://www.linkedin.com/company/shqiperiacom"
        }
    }
]


def get_countries(companyList):                 #For Countries and count how many times that country is in this list
    Empty_dictionary = {}                         
    Empty_list =[]                                
    for i in companyList:
        Countries = i['Country']                  
        Empty_list.append(Countries)                 #Appending all Countries in to a empty list            
    
        X = Empty_list.count(Countries)            #Counts the countries         
        Empty_dictionary[Countries] = X           
    return Empty_dictionary


def get_companies_names(companyList):          # Getting Company Names from upper dictionary            
    Empty_List = []                                  
    for i in companyList:
        COMPANY_NAMES = i['Company Name']                    #Taking all company Names
        Empty_List.append(COMPANY_NAMES)                     #Appending it in Empty List      
    return Empty_List

