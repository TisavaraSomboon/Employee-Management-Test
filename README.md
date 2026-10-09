# Employee-Management-Test

# ER diagram

<img width="627" height="422" alt="Screen Shot 2569-10-09 at 09 28 28" src="https://github.com/user-attachments/assets/bf3ed48f-1dbe-44d1-b2e3-0821504ad6b0" />

# endpoint

- Create
```bash
POST /api/employees
```
  Postman curl
```bash
curl --location 'http://127.0.0.1:8000/api/employees/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0' \
--data '{
    "name": "ลลิศา มโนบาล",
    "address": "London Rd",
    "image": "/Users/tisavara/Documents/employeeManagementTest/media/images/avatar2.jpg",
    "status": "normal",
    "position": null,
    "manager": 1
}'
```
- Read
```bash
GET /api/employees or /api/employees/[id]
```
  Postman curl
```bash
curl --location 'http://127.0.0.1:8000/api/employees/' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0' \
--data ''
```
- Update
```bash
PUT/PATCH /api/employees/[id]
```
  Postman curl
```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/employees/11/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0' \
--data '{
    "name": "ลลิศา",
    "position": 6
}'
```
- Delete
```bash
DELETE /api/employees/[id]
```
  Postman curl
```bash
curl --location --request DELETE 'http://127.0.0.1:8000/api/employees/11/' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0' \
--data ''
```

# Advanced Queries

- filter
```bash
GET /api/employees/?status=normal
```
  Postman curl
```bash
curl --location 'http://127.0.0.1:8000/api/employees/?status=normal' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0'
```
- searching
```bash
GET /api/employees/?search=Alex
```
  Postman curl
```bash
curl --location 'http://127.0.0.1:8000/api/employees/?search=Alex' \
--header 'Authorization: Basic dGlzYXZhcmE6VGVzdEAxMjM0'
```
