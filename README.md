# 💸 Expense Tracker

A simple personal expense tracking web app built with **Flask** and **Microsoft SQL Server**. Add expenses, categorize them, filter by category or month, and keep track of where your money is going.

---

## ✨ Features

- ➕ **Add Expenses** — amount, category, date, and optional notes
- 📂 **Manage Categories** — create and delete categories
- 📋 **View All Expenses** — clean table with category names via SQL JOIN
- 🔍 **Filter Expenses** — by category, by month, or both together
- 🗑️ **Delete** — remove expenses or categories anytime

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** Microsoft SQL Server (localhost)
- **Driver:** pyodbc (ODBC Driver 13 for SQL Server)
- **Frontend:** HTML, CSS, Jinja2 templates

---

## 📁 Project Structure

```
expense_app/
├── app.py                  # Flask routes
├── db.py                   # Database connection
├── templates/
│   ├── categories.html     # Manage categories
│   ├── add_expense.html    # Add new expense form
│   └── expenses.html       # List + filter expenses
└── static/
    └── style.css           # Styling
```

---

## 🗄️ Database Schema

```sql
CREATE DATABASE ExpenseDB;

CREATE TABLE Categories (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(50)
);

CREATE TABLE Expenses (
    id INT PRIMARY KEY IDENTITY,
    amount DECIMAL(10,2),
    category_id INT FOREIGN KEY REFERENCES Categories(id),
    expense_date DATE,
    note VARCHAR(200)
);
```

---

## 🚀 Setup

### 1. Install requirements
```bash
pip install flask pyodbc
```

Make sure **ODBC Driver for SQL Server** is installed on your machine.

### 2. Create the database
Open SSMS and run the schema above to create `ExpenseDB` with both tables.

### 3. Configure connection
Update `db.py` if your server name or auth method is different:
```python
"DRIVER={ODBC Driver 13 for SQL Server};"
"SERVER=localhost;"
"DATABASE=ExpenseDB;"
"Trusted_Connection=yes;"
```

### 4. Run the app
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 🧭 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home |
| `/categories` | GET, POST | List and add categories |
| `/categories/delete/<id>` | GET | Delete a category |
| `/expenses` | GET | List expenses (with filters) |
| `/expenses/add` | GET, POST | Add a new expense |
| `/expenses/delete/<id>` | GET | Delete an expense |

---

## 📚 What I Learned

- Connecting Flask with MSSQL using **pyodbc**
- Writing **parameterized SQL queries** (`?` placeholders) to prevent SQL injection
- Using **INNER JOIN** to fetch related data across tables
- Building **dynamic SQL queries** based on user filters
- Handling **GET vs POST** in the same route
- Jinja2 templating (loops, conditionals, variable rendering)
- Debugging common errors:
  - ODBC driver mismatch
  - `KeyError` from form field typos
  - Missing spaces in concatenated SQL strings
  - Case-sensitive format strings (`yyyy-MM` not `YYYY-MM`)
  - Variable name overwrites

---

## 🔮 Future Ideas

- Edit functionality for expenses
- Dashboard with totals and charts (GROUP BY queries)
- Export to CSV
- Monthly budget limits with alerts
- User authentication

---

## 👨‍💻 Author

Built as a hands-on learning project to move from SQLite to MSSQL and get comfortable with full-stack Flask development.

*First real project — built step by step, debugged error by error.* 🚀
