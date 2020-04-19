from collections import defaultdict
from datetime import datetime
from covidFYI.data.models import InfoType, Location, Entry
import csv
import requests

def run():

    # If data already populated
    if Entry.objects.all().count() > 0:
        print("Database already populated; not adding initial data")
        return

    print("Database not populated; adding initial data...")
    
    with open('DATA_NEW_2.csv') as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("adding new data..")
        source_links = defaultdict(bool)

        for s in l[1:]:
            st = s[0].replace('&', 'and').strip()
            
            loc , created = Location.objects.get_or_create(state=st, district=s[1].strip())
            i, created = InfoType.objects.get_or_create(name=s[2])

            # Check if Entry has a valid source link
            if s[10] in source_links:
                source_link_valid = source_links[s[10]]
            else:
                source_link_valid = False
                try:
                    req = requests.get(s[10], verify=False, timeout=5)
                    if req.status_code == 200:
                        source_link_valid = True
                    else:
                        print(f"{s[10]} is not 200\n")
                except:
                    print(f"{s[10]} can't reach\n")
                    pass
            
                source_links[s[10]] = source_link_valid

            e = Entry.objects.create(location=loc, infotype=i, name=s[3].strip(), dr_name=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9], source_link=s[10], source_link_valid=source_link_valid, source=s[11])
            e.save()

        print("Done adding initial data!")
