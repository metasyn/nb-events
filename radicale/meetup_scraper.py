import re
import os
from datetime import datetime
import logging
from typing import Dict
from hashlib import md5

import requests

def setup_logging():
  logging.basicConfig(filename="logfile.txt")
  stderrLogger=logging.StreamHandler()
  stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
  logging.getLogger().addHandler(stderrLogger)
  return logging.getLogger(__name__)

logger = setup_logging()


def split_ics(content: str) -> Dict[str, str]:
    ''' Splits a VCALENDAR list of events into individual events. ''' 
    # Get rid of carriage bullshit
    content = content.replace("\r", "\n")
    content = content.replace("\n\n", "\n")

    # Extract header
    header_regex = re.compile(r"(?:BEGIN:VCALENDAR\s).+?(?:END:VTIMEZONE\s)", flags=re.S)
    header = re.findall(header_regex, content)[0]

    # Footer is required for each individual event
    footer = 'END:VCALENDAR'

    # Extract UID
    uid_regex = re.compile(r"UID:(.*)")
    uids = re.findall(uid_regex, content)

    # Convert UIDS to md5 just in case they have weird characters
    uids = [md5(uid.encode('utf-8')).hexdigest() for uid in uids]

    # Extract events
    events_regex = re.compile(r"(?:BEGIN:VEVENT\s).+?(?:END:VEVENT\s)", flags=re.S)
    events = re.findall(events_regex, content)

    result = {}
    for i, event in enumerate(events):
        result[uids[i]] = header + event + footer


    assert len(uids) == len(events), "each event should have a uid"

    return result


class Scraper:
    ''' A scraper class for getting ics events out of the meetup ical link.

    The scraper class will take a meetup url to a single ical event, then it
    will break up that content into a number of smaller ics events that can be
    then inserted into the correct folder structure that radicale uses.
    '''
    def __init__(self, meetup_ical_url: str, radicale_dir: str):
        '''The init here just stores a few variables for re-use:

          - meetup_ical_url (str): the url that points to the aggregated ics event file
          - radicale_dir (str): the path to the radicale storage location
        '''
        self.meetup_ical_url = meetup_ical_url
        self.radicale_dir = radicale_dir

    def download_calendar(self) -> str:
        '''Download calendar will download a calendar file from meetup.com'''

        response = requests.get(self.meetup_ical_url, allow_redirects=True)
        if response.status_code != requests.codes.ok:
            logger.error(response.text, reponse.status_code)
            msg = "Could not fetch calendar from URL: {}".format(self.meetup_ical_url)
            raise RuntimeError(msg)

        return response.text

    def make_calendar_path(self) -> str:
        return os.path.join(self.radicale_dir, "collections/collection-root/noisebridge/meetup")

    def split_and_add_events(self, content: str):
        '''Split the file up into individual ics events'''
        events = split_ics(content)

        calendar_path = self.make_calendar_path()

        for uid, event in events.items():
            path = os.path.join(calendar_path, '{}.ics'.format(uid))
            with open(path, 'w') as fp:
                fp.write(event)


if __name__ == '__main__':
    radicale_dir = "/var/lib/radicale"
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    logger.info("Running meetup scraper at %s", now)
    calendar_url = "https://www.meetup.com/noisebridge/events/ical/"
    download_path = "/tmp/meetup_events.ics"

    scraper = Scraper(calendar_url, radicale_dir)
    content = scraper.download_calendar()
    scraper.split_and_add_events(content)
