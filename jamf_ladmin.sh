#!/bin/sh

get_token=$(curl -X POST 'https://casper.district65.net:8443/api/v1/auth/token' --header 'Accept: application/json' --header 'Authorization: Basic' --header 'Authorization: Basic c2xhc2hqYW1mYXBpOmpmal9GV0M4eWZnNGN6ajBycXc=')

echo "TOKEN="$get_token > .env/token.tmp

jamfQuery=$()

token_grep = $(grep -i token .env/token.tmp | sed /^*=//)

curl -X GET \
  'https://casper.district65.net:8443/api/v1/computers-inventory?section=GENERAL&section=EXTENSION_ATTRIBUTES&page=0&page-size=100&sort=id:asc&filter=userAndLocation.username=="slatterym"' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdXRoZW50aWNhdGVkLWFwcCI6IkdFTkVSSUMiLCJhdXRoZW50aWNhdGlvbi10eXBlIjoiSlNTIiwiZ3JvdXBzIjpbXSwic3ViamVjdC10eXBlIjoiSlNTX1VTRVJfSUQiLCJ0b2tlbi11dWlkIjoiNTgwYzAyMDgtOTk0NC00YjcwLTljNGYtNDUyMThjNWUzMDk2IiwibGRhcC1zZXJ2ZXItaWQiOi0xLCJzdWIiOiI0NSIsImV4cCI6MTY2OTY4NDQ4NX0.5rjvtK9JINxsFgRXe5TW9r2dsJLBgWDQ_A7CHHSirOY'