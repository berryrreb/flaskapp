from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'prompts.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        conn = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

@app.route('/')
def index():
    search_query = request.args.get('q', '')
    conn = get_db_connection()
    if search_query:
        query = 'SELECT * FROM prompts WHERE title LIKE ? OR category LIKE ?'
        prompts = conn.execute(query, (f'%{search_query}%', f'%{search_query}%')).fetchall()
    else:
        prompts = conn.execute('SELECT * FROM prompts').fetchall()
    conn.close()
    return render_template('index.html', prompts=prompts, search_query=search_query)

@app.route('/add', methods=('GET', 'POST'))
def add_prompt():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        conn = get_db_connection()
        conn.execute('INSERT INTO prompts (title, content, category) VALUES (?, ?, ?)',
                     (title, content, category))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_prompt.html')

@app.route('/prompt/<int:prompt_id>')
def view_prompt(prompt_id):
    conn = get_db_connection()
    prompt = conn.execute('SELECT * FROM prompts WHERE id = ?', (prompt_id,)).fetchone()
    conn.close()
    if prompt is None:
        return "Prompt not found", 404
    return render_template('view_prompt.html', prompt=prompt)

@app.route('/edit/<int:prompt_id>', methods=('GET', 'POST'))
def edit_prompt(prompt_id):
    conn = get_db_connection()
    prompt = conn.execute('SELECT * FROM prompts WHERE id = ?', (prompt_id,)).fetchone()

    if prompt is None:
        conn.close()
        return "Prompt not found", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        conn.execute('UPDATE prompts SET title = ?, content = ?, category = ? WHERE id = ?',
                     (title, content, category, prompt_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit_prompt.html', prompt=prompt)

@app.route('/delete/<int:prompt_id>', methods=('POST',))
def delete_prompt(prompt_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM prompts WHERE id = ?', (prompt_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

import click

@app.cli.command('init-db')
def init_db_command():
    "Clear the existing data and create new tables."
    init_db()
    click.echo('Initialized the database.')

if __name__ == '__main__':
    app.run(debug=True)
