from apscheduler.schedulers.background import BackgroundScheduler
from covidFYI.data.models import Location, InfoType, Entry
import requests
import csv
import os

CSV_URL = 'https://docs.google.com/spreadsheets/d/1G4ar-G5EJR7_SAF7CsSvYev6-pGgK-OzgOk3X2St99w/export?format=csv'
CSV_NAME = 'new_csv.csv'

def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=download_csv, trigger="interval", seconds=10)
    scheduler.start()
    print("Scheduler started!")

def test_job():

    print("I'm a test job!")
    print(os.listdir())

def download_csv():

    req = requests.get(CSV_URL)

    if req.status_code != 200:
        print("Download error!")

    with open(CSV_NAME, 'wb') as f:
        for chunk in req:
            f.write(chunk)

    print("Downloaded most recent Google Sheet!")

    with open(CSV_NAME, 'r') as f:
        reader = csv.reader(f)
        l = tuple(reader)

        print("Checking for new entries in Google Sheet..")

        if len(l) - 1 == Entry.objects.all().count():
            print("No new entries to add to Database")
            return

        for s in l[::-1][:-1]:
            st = s[0].replace('&', 'and').strip()
            
            loc , created = Location.objects.get_or_create(state=st, district=s[1].strip())
            i, created = InfoType.objects.get_or_create(name=s[2])

            e, created = Entry.objects.get_or_create(location=loc, infotype=i, name=s[3].strip(), dr_name=s[4], email_id_1=s[5], email_id_2=s[6], phone_1=s[7], phone_2=s[8], extension=s[9], source_link=s[10], source=s[11])

            if created is True:
                print(f"Entry {e} saved!")
            else:
                print(f"Entry {e} onwards are all updated! Cheers!")
                return
