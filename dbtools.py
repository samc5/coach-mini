import sqlite3
import os
import pandas as pd

def create_table():
    """Creates table in database"""
    # connect to database
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # create table
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, name TEXT, email TEXT, phone TEXT, address TEXT, city TEXT, state TEXT, zip TEXT, creditcard TEXT, security TEXT, expiration TEXT)")
    # save changes
    db.commit()
    # close database
    db.close()

def player_stats_create():
    print("player_stats_create")
    """Creates table with player name, score for column 1, 2, 3"""
    # connect to database
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # create table with explicit PRIMARY KEY constraint
    c.execute("CREATE TABLE IF NOT EXISTS player_stats (player_name TEXT PRIMARY KEY, score1 TEXT, score2 TEXT, score3 TEXT)")
    db.commit()
    db.close()

def add_or_create(player_name, score1, score2, score3):
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    c.execute("SELECT * FROM player_stats WHERE player_name = ?", (player_name,))
    data = c.fetchall()
    if len(data) == 0:
        print("len(data) == 0")
        #c.execute("INSERT INTO player_stats VALUES (?,?,?,?)", (player_name, score1, score2, score3))
        c.execute("INSERT INTO player_stats VALUES (?,?,?,?)",(player_name,score1,score2,score3))
    else:
        print("len(data) != 0")
        c.execute("UPDATE player_stats SET score1 = ?, score2 = ?, score3 = ? WHERE player_name = ?", (score1, score2, score3, player_name))
    db.commit()
    db.close()


def print_players():
    """Prints all players in player_stats table"""
    print("print_players")
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # select all players
    c.execute("SELECT * FROM player_stats")
    data = c.fetchall()
    for row in data:
        print(row)
    db.commit()
    db.close()

def clear_players():
    """Clears all players in player_stats table"""
    print("clear_players")
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # delete all players
    c.execute("DELETE FROM player_stats")
    db.commit()
    db.close()

# def delete_tables():
#     """Deletes both tables"""
#     print("delete_tables")
#     db = sqlite3.connect("data/database.db")
#     c = db.cursor()
#     # delete both tables
#     c.execute("DROP TABLE users")
#     c.execute("DROP TABLE player_stats")
#     db.commit()
#     db.close()

def get_average_scores():
    """Returns a list of the average score all players in the db"""
    averages = []
    print("get_average_scores")
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # select all players
    c.execute("""SELECT ROUND(AVG(score1), 2) AS av1, ROUND(AVG(score2),2) AS av2, ROUND(AVG(score3),2) AS av3 FROM player_stats""")
    data = c.fetchall()
    for row in data:
        averages.append(row[0])
        averages.append(row[1])
        averages.append(row[2])
    return averages

def list_player_names():
    """Returns a list of all player names in the db"""
    names = []
    print("list_player_names")
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    # select all players
    c.execute("""SELECT player_name FROM player_stats""")
    data = c.fetchall()
    for row in data:
        names.append(row[0])
    return names
# def pandas_read_sql():
#     """Reads table into pandas dataframe"""
#     print("pandas_read_sql")
#     db = sqlite3.connect("data/database.db")
#     c = db.cursor()
#     # read table into pandas dataframe
#     df = pd.read_sql_query("SELECT * FROM player_stats", db)
    
#     print(df)
#     db.commit()
#     db.close()


#clear_players()
player_stats_create()
get_average_scores()
print_players()

