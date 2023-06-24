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
# Tworzenie nowego uzytkownika LUB aktualizowanie istniejącego
- POST /user/<used_id>
wymaga json body z wartościami do wpisania

# Usuwanie uzytkownika po ID
- DELETE /user/<user_id>

# Zwrócenie użytkownika konkretnego po ID
- GET /user/<user_id>

# Zwrócenie wszystkich użytkowników
- GET /users

# Głosowanie na użytkownika
- POST /user/<user_id>/vote
