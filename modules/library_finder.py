import pandas as pd
import re

def find_libraries(city):
    data = pd.read_csv("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/609034/Public_libraries_in_England_basic_dataset__as_on_1_July_2016_.csv",header=1,encoding='unicode_escape')
    mask = list(bool(re.search(city,record)) for record in data['Library service'].str.lower().str.strip())
    return data.loc[mask,['Library name','Postcode']]