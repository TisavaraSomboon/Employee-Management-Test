# Employee-Management-Test

# Er diagram

<img width="627" height="422" alt="Screen Shot 2569-10-09 at 09 28 28" src="https://github.com/user-attachments/assets/bf3ed48f-1dbe-44d1-b2e3-0821504ad6b0" />

# endpoint

- Create
```bash
POST /api/employees
```
- Read
```bash
GET /api/employees or /api/employees/[id]
```
- Update
```bash
PUT/PATCH /api/employees/[id]
```
- Delete
```bash
DELETE /api/employees/[id]
```

# Advanced Queries

- filter
```bash
GET /api/employees/?status=normal
```
- searching
```bash
GET /api/employees/?search=Alex
```
