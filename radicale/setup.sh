#!/bin/bash

set -e

USER=noisebridge


make_calendar() {
  curl -u $USER -X MKCOL "http://localhost:5232/$USER/calendar" --data "$(cat calendar.xml)"
}
   

make_calendar
