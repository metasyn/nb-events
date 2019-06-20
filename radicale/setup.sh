#!/bin/bash

set -e

USER=noisebridge


make_calendar() {
  for file in $(ls calendars); do
    name="${file%%.*}"
    curl -u $USER -X MKCOL "http://localhost:5232/$USER/$name" --data "$(cat calendars/$file)"
  done;
}
   

make_calendar
