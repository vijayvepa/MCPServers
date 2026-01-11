TOKEN=$(curl --request POST \
  --url https://dev-41wmpjgak53sapxa.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data @TokenRequest.json | jq -r .access_token)

curl --request GET \
  --url http://127.0.0.1:8789/api/me \
  --header "authorization: Bearer $TOKEN" | jq