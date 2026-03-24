import sqlite3

class LeaderboardTable:
    def __init__(self, db_path="leaderboard.db", max_entries=10):
        self.db_path = db_path
        self.max_entries = max_entries
        self._connect()
        self._create_table()

    def _connect(self):
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
    
    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            time REAL NOT NULL
            )
        """)
        self.connect.commit()
    
    def add_score(self, name, time):
        if name.strip() == "":
            name = "Player"
        
        self.cursor.execute(
            "INSERT INTO leaderboard (player_name, time) VALUES (?, ?)",
            (name, time)
        )
        self.connect.commit()

    def get_top_scores(self):
        self.cursor.execute("""
            SELECT player_name, time
            FROM leaderboard
            ORDER BY time ASC
            LIMIT ?
        """, (self.max_entries,))
        
        return self.cursor.fetchall()