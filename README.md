Here's a **clean, professional, and improved `README.md`** tailored for your **Late Show API project** — perfect for clarity, grading, or sharing with teammates or recruiters.

---

```markdown
# Late Show Guest Management API

This project is a RESTful API built with Flask to manage guests appearing on a fictional Late Show. It allows users to add, view, and delete guest entries. The project is designed to demonstrate backend development skills, including model creation, routing, database migrations, and API testing.

---

## Features

- View all guests
- Add a new guest
- Delete a guest by ID
- Tested using Postman or Thunder Client
- Built with modular structure (MVC pattern)

---

## Tech Stack

- Python 3.12
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Postman or Thunder Client for API testing

---

## Project Structure

```

late-show-api-challenge/
├── server/
│   ├── app.py                 # App factory
│   ├── config.py              # App configuration & DB setup
│   ├── models/
│   │   └── guest.py           # Guest model
│   └── controllers/
│       └── guest\_controller.py # API routes for guests
├── migrations/                # Database migration history
├── Pipfile / requirements.txt # Python dependencies
├── challenge-4-lateshow\.postman\_collection.json
└── README.md

````

---

## Setup Instructions

### 1. Clone the Project
```bash
git clone https://github.com/your-username/late-show-api-challenge.git
cd late-show-api-challenge
````

### 2. Create a Virtual Environment

Using Pipenv:

```bash
pipenv install
pipenv shell
```

Or with venv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database

Ensure PostgreSQL is running and create a database:

```bash
createdb late_show_db
```

### 4. Run Migrations

```bash
flask --app server.app:create_app db init
flask --app server.app:create_app db migrate -m "Initial setup"
flask --app server.app:create_app db upgrade
```

### 5. Run the Application

```bash
flask --app server.app:create_app run
```

Visit: `http://127.0.0.1:5000`

---

## API Endpoints

| Method | Endpoint       | Description          |
| ------ |              
| GET      `/guests`      | Get all guests       |
| POST   | `/guests`      | Add a new guest      |
| DELETE | `/guests/<id>` | Delete a guest by ID |

### Sample POST Body

```json
{
  "name": "Trevor Noah",
  "profession": "Comedian"
}
```

---

## Testing the API

### Option 1: Postman

1. Visit [Postman Web](https://web.postman.co/)
2. Import the file `challenge-4-lateshow.postman_collection.json`
3. Run GET, POST, and DELETE requests to test your API

### Option 2: Thunder Client (VS Code Extension)

1. Install "Thunder Client" from the Extensions tab
2. Import the collection or manually create requests
3. Run API tests directly inside VS Code

---

## What You’ll Learn from This Project

* Structuring a Flask app using blueprints and app factories
* Setting up a PostgreSQL database and performing migrations
* Building RESTful endpoints
* Using Postman or Thunder Client to test API behavior
* Writing clean, modular Python code

---



---

## License

This project is for educational purposes under Moringa School Phase 4 backend challenge guidelines.


