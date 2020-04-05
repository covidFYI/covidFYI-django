from datetime import datetime
from covidFYI.data.models import InfoType, Location, Entry
import csv

def run():

    # If data already populated
    if Entry.objects.all().count() > 0:
        return

    with open('covid_data.csv') as f:
        reader = csv.reader(f)
        l = tuple(reader)

        for s in l[1:]:
            st = s[0].replace('&', 'and').strip()
            
            loc , created = Location.objects.get_or_create(state=st, district=s[1].strip())
            i, created = InfoType.objects.get_or_create(name=s[2])

            e = Entry.objects.create(location=loc, infotype=i, name=s[3].strip(), dr_name=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9], source_link=s[10], source=s[11])
            e.save()
