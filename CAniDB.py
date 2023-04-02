import sqlite3


#
class CAniDB:
    def __init__(self):
        self.con = sqlite3.connect('Animate.db3')
        self.cursor = self.con.cursor()

    def close(self):
        self.con.close()

    def create_table_animate_list(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS animate_all (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                            name TEXT NOT NULL, \
                            sn INTEGER NOT NULL, \
                            score DOUBLE NOT NULL, \
                            score_people INTEGER NOT NULL);")

    def create_table_episode(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS episode (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                    animate_id INTEGER NOT NULL, \
                                    episode TEXT NOT NULL, \
                                    sn INTEGER NOT NULL);")

    def update_animate(self, name, sn, score, score_people):
        sql = "SELECT id, name FROM animate_all WHERE name = \"" + name + "\""
        cursor = self.cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            # update data
            sql = "UPDATE animate_all SET score = " + str(score) + ", score_people = " + str(score_people) + " WHERE id = " + str(row[0])
            self.cursor.execute(sql)
            rowid = row[0]
        else:
            # Insert data to table: animate_all
            sql = "INSERT INTO animate_all(name, sn, score, score_people) VALUES(\"" + name + "\", " + sn + ", " + str(score) + ", " + str(score_people) + ");"
            self.cursor.execute(sql)
            rowid = self.cursor.lastrowid
        return rowid

    def update_episode(self, animate_id, episode, sn):
        sql = "UPDATE episode SET animate_id = " + str(animate_id) + ", episode = \"" + episode + "\" WHERE sn = " + sn + ";"
        self.cursor.execute(sql)
        if self.cursor.rowcount < 1:
            # Insert episode info
            sql = "INSERT INTO episode(animate_id, episode, sn) VALUES(" + str(animate_id) + ", \"" + episode + "\", " + sn + ");"
            self.cursor.execute(sql)

    def commit(self):
        self.con.commit()

    def get_max_sn(self):
        sql = "SELECT count(*) FROM episode;"
        cursor = self.cursor.execute(sql)
        row = cursor.fetchone()
        if row and row[0] > 0:
            sql = "SELECT MAX(sn) FROM episode;"
            cursor = self.cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                return row[0]
        return 0

    def query_animate_sn_list(self):
        sql = "SELECT sn FROM animate_all;"
        cursor = self.cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def query_animates_by_score(self, score):
        sql = "SELECT name, sn, score, score_people FROM animate_all WHERE score = " + str(score) + " ORDER BY score_people DESC"
        cursor = self.cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def query_animates_by_score_people(self):
        sql = "SELECT name, sn, score, score_people FROM animate_all ORDER BY score_people DESC"
        cursor = self.cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
