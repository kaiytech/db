# db
Kajetan Krawczyk 25719

Building:
```
docker build https://github.com/kaiytech/db.git -t redrest
```

Running:
```
docker run -p 5000:5000 redrest
```

Endpoints:
- POST /user/<used_id>

Tworzenie nowego uzytkownika LUB aktualizowanie istniejącego

- DELETE /user/<user_id>

Usuwanie uzytkownika po ID

- GET /user/<user_id>

Zwrócenie użytkownika konkretnego po ID

- GET /users

Zwrócenie wszystkich użytkowników

- POST /user/<user_id>/vote

Głosowanie na użytkownika
