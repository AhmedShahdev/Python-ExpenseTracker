from flask import Flask, render_template, redirect, request, url_for
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Working"

# @app.route('/db')
# def test_db():
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT COUNT(*) FROM Categories")
#         count = cursor.fetchone()[0]
#         conn.close()
#         return f"Connected! Categories mein {count} rows hain"

#     except Exception as e:
#         return f"Error: {str(e)}"

# Ye agaya categories table k lie
#  isme get or post method hai
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        cursor.execute('INSERT INTO Categories (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('categories'))
    
    cursor.execute("SELECT id, name FROM Categories")
    rows = cursor.fetchall()
    conn.close()
    return render_template('categories.html', categories=rows)


# ab agaya delete method 
@app.route('/categories/delete/<int:id>')
def delete_category(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Categories WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('categories'))


# ab agaya hai dusre table yani expenses ki working 
@app.route('/expenses/add', methods=['GET', 'POST'])
def add_expense():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        amount = request.form['amount']
        category_id = request.form['category_id']
        expense_date = request.form['expense_date']
        note = request.form['note']

        cursor.execute(
            "INSERT INTO Expenses (amount, category_id, expense_date, note) VALUES (?, ?, ?, ?)",
            (amount, category_id, expense_date, note)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('add_expense'))

    cursor.execute("SELECT id, name FROM Categories")
    categories = cursor.fetchall()
    conn.close()
    return render_template('add_expenses.html', categories=categories)


@app.route('/expenses')
def list_expenses():
    conn = get_connection()
    cursor = conn.cursor()

# ab mje ye values filter karwani hai wo ye hain
    category_id = request.args.get('category_id')
    month = request.args.get('month')

# ab ye wo query ru kr hi h
    query = """
        SELECT e.id, e.amount, c.name AS category, e.expense_date, e.note
        FROM Expenses e
        INNER JOIN Categories c ON e.category_id = c.id
        WHERE 1=1
    """
    params = []

    if category_id:
        query += " AND e.category_id = ?"
        params.append(category_id)

    if month:
        query += " AND FORMAT(e.expense_date, 'yyyy-MM') = ?"
        params.append(month)

    query += " ORDER BY e.expense_date DESC"

    cursor.execute(query, params)
    expenses = cursor.fetchall()

    # ab ajao dropdown k lie
    cursor.execute("SELECT id, name from Categories")
    categories = cursor.fetchall()

    conn.close()
    return render_template('expenses.html'
                           ,expenses=expenses,
                            categories= categories,
                            selected_category = category_id,
                            selected_month = month
                            )


@app.route('/expenses/delete/<int:id>')
def delete_expense(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_expenses'))

if __name__ == '__main__':
    app.run(debug=True)