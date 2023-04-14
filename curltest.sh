query=$(curl -X POST   'https://casper.district65.net:8443/api/v1/auth/token'   --header 'Accept: application/json'   --header 'Authorization: Basic c2xhc2hqYW1mYXBpOmpmal9GV0M4eWZnNGN6ajBycXc=')

$query > cResponse.txt

KEY=$(cat cResponse.txt | awk '$1 ~ /token/ {print $3}' | sed 's/.$//')


search_term=$1

lookup=$(curl -X GET \
  'https://casper.district65.net:8443/api/v1/computers-inventory?section=GENERAL&section=EXTENSION_ATTRIBUTES&page=0&page-size=100&sort=id:asc&filter=userAndLocation.username=="*$search_term*"' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer $KEY)

