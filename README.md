Jak to będzie działać?

Można używać API bez logowanie się ale tylko 1 filmik na godzine
Użytkownik który jest zalogowany może 10 na godzine
Wchodząc na stronę użytkownik ma wybór do zalogowania się aby sprawdzić swoją historie pobrań, zmiany hasła/emailu oraz sprawdzenia limitu api.

Funkcje:

- Zmiana Hasła
- Zmiana Email
- założenie konta
- logowanie
- sprawdzenie limitu
- kopiowanie / resetowanie kluczu API
  -sprawdzenie historii

Co potrzeba do projektu aby działał?
-instalacja biblioteki
-instalacja modules
-zaprojetkowanie interfejsu
-end point do pobierania api
-tworzenie api do konwertowania/pobierania
-authentication

Elementy projekty np. co robi backend / frontend?

Backend endpoints:

**Konwerter**
Endpoint: POST /api/convert
Parameters:
link: string
type: string
api_key: string

**Download**
Endpoint: GET /api/download
Parameters:
id: string

**Rejestracja**

Endpoint: POST /api/auth/register
Parameters:
username: string
password: string
confirm_password: string
captcha: string

**Logowanie**

Endpoint: POST /api/auth/login
Parameters:
username: string
password: string
captcha: string

**Ustawienia**

Endpoint: POST /api/settings
Parameters:
Change_password: string
Change_email: string

**Widok Historii pobrań**

Endpoint: GET /api/history
Parameters:
History: array

history: {
[ 'link': 'URL', 'timestamp': '06-01-2024 18:04:53']
[ 'link': 'URL', 'timestamp': '06-01-2024 18:04:53']
[ 'link': 'URL', 'timestamp': '06-01-2024 18:04:53']
[ 'link': 'URL', 'timestamp': '06-01-2024 18:04:53']
}
