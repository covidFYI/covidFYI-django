from datetime import datetime
# import pandas as pd
from covidFYI.data.models import InfoType, Location, Entry
import csv

def run():

    with open('covid_data.csv') as f:
        reader = csv.reader(f)
        l = tuple(reader)
        # u = UserModel.query.first()
        for s in l[1:]:
            st = s[0].replace('&', 'and').strip()
            loc , created = Location.objects.get_or_create(state=st, district=s[1].strip())
            i, created = InfoType.objects.get_or_create(name=s[2])

            e = Entry.objects.create(location=loc, infotype=i, name=s[3].strip(), dr_name=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9], source_link=s[10], source=s[11])
            e.save()

    #         st = s[0].replace('&', 'and')
    #         loc = LocationModel.query.filter(LocationModel.state==st , LocationModel.district==s[1]).first()
    #         i = InfoTypeModel.query.filter(InfoTypeModel.name==s[2]).first()
            
    #         e = EntryModel(location_id=loc.id, user_id=u.id, infotype_id=i.id, name=s[3], dr_name=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9],source_link=s[10],source=s[11])
    #         e.save() 
    #         print(f'{e} saved')
       
    # entries = EntryModel.query.count()
    # print(f'\n{entries}')
    