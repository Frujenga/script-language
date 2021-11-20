from flask import Flask, json
import sqlite3


cDbase = Flask(__name__)


@cDbase.route('/characters')
def get_characters():
    con = sqlite3.connect('Characters.sql')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * from Characters')
    rors = cur.fetchall()
    characters = []
    for row in rors:
        d = dict(zip(row.keys(), row))
        characters.append(d)
    return json.dumps(characters)


if __name__ == '__main__':
    cDbase.run(debug=True)
