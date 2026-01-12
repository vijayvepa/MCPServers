TOKEN=$(curl --request POST \
  --url https://dev-41wmpjgak53sapxa.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data @TokenRequest.json | jq -r .access_token)

curl --request GET \
  --url https://todos-api.vijay-k-vepakomma.workers.dev/api/me \
  --verbose \
  --header "authorization: Bearer $TOKEN" | jq