curl -X 'POST' \
  'http://127.0.0.1:8000/users/auth/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "a@mail.com",
  "password": "qwerty"
}'