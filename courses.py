import os
import sqlite3

# poistaa tietokannan alussa (kätevä moduulin testailussa)
os.remove("courses.db")

db = sqlite3.connect("courses.db")
db.isolation_level = None

# luo tietokantaan tarvittavat taulut
def create_tables():
    db.execute("CREATE TABLE Opettajat (id INTEGER PRIMARY KEY, nimi TEXT)")
    db.execute("CREATE TABLE Kurssit (id INTEGER PRIMARY KEY, nimi TEXT, opintopisteet INTEGER)")
    db.execute("CREATE TABLE KurssinOpettajat (kurssi_id INTEGER REFERENCES Kurssit, opettaja_id INTEGER REFERENCES Opettajat)")
    db.execute("CREATE TABLE Opiskelijat (id INTEGER PRIMARY KEY, nimi TEXT)")
    db.execute("CREATE TABLE Suoritukset (id INTEGER PRIMARY KEY, opiskelija_id INTEGER REFERENCES Opiskelijat, kurssi_id INTEGER REFERENCES Kurssit, pvm TIMESTAMP, arvosana INTEGER)")
    db.execute("CREATE TABLE Ryhmat (id INTEGER PRIMARY KEY, nimi TEXT)")
    db.execute("CREATE TABLE RyhmanOpettajat (ryhma_id INTEGER REFERENCES Ryhmat, opettaja_id INTEGER REFERENCES Opettajat)")
    db.execute("CREATE TABLE RyhmanOpiskelijat (ryhma_id INTEGER REFERENCES Ryhmat, opiskelija_id INTEGER REFERENCES Opiskelijat)")

# lisää opettajan tietokantaan
def create_teacher(name):
    ope = db.execute("INSERT INTO Opettajat (nimi) VALUES (?)",[name])
    return ope.lastrowid

# lisää kurssin tietokantaan
def create_course(name, credits, teacher_ids):
    kurssi = db.execute("INSERT INTO Kurssit (nimi, opintopisteet) VALUES (?,?)", [name, credits])
    kid = kurssi.lastrowid

    for teacher in teacher_ids:
         db.execute("INSERT INTO KurssinOpettajat (kurssi_id, opettaja_id) VALUES (?, ?)", [kid, teacher])

    return kid
   

# lisää opiskelijan tietokantaan
def create_student(name):
    opiskelija = db.execute("INSERT INTO Opiskelijat (nimi) VALUES (?)",[name])
    return opiskelija.lastrowid

# antaa opiskelijalle suorituksen kurssista
def add_credits(student_id, course_id, date, grade):
    suoritus = db.execute("INSERT INTO Suoritukset (opiskelija_id, kurssi_id, pvm, arvosana) VALUES (?,?,?,?)",[student_id, course_id, date, grade ])
    return suoritus.lastrowid




# lisää ryhmän tietokantaan
def create_group(name, teacher_ids, student_ids):
    id = db.execute("INSERT INTO Ryhmat (nimi) VALUES (?)", [name] )
    ryhmaId = id.lastrowid
    
    for teacher in teacher_ids:
       db.execute("INSERT INTO RyhmanOpettajat (ryhma_id, opettaja_id) VALUES (?,?)",[ryhmaId,teacher])
    for student in student_ids:
       db.execute("INSERT INTO RyhmanOpiskelijat (ryhma_id, opiskelija_id) VALUES (?,?)", [ryhmaId, student])
    
    return ryhmaId



# hakee kurssit, joissa opettaja opettaa (aakkosjärjestyksessä)
def courses_by_teacher(teacher_name):
    kurssit = db.execute("SELECT DISTINCT K.nimi FROM Kurssit K LEFT JOIN KurssinOpettajat Q ON K.id = Q.kurssi_id LEFT JOIN Opettajat O ON O.id = Q.opettaja_id WHERE O.nimi = ? AND O.id IS NOT NULL ORDER BY K.nimi", [teacher_name]).fetchall()
    k = [t[0] for t in kurssit]
    return k

# hakee opettajan antamien opintopisteiden määrän
def credits_by_teacher(teacher_name):
    pisteet = db.execute("SELECT SUM(K.opintopisteet) FROM Opettajat O LEFT JOIN KurssinOpettajat Q ON O.id = Q.opettaja_id LEFT JOIN Kurssit K ON K.id = Q.kurssi_id LEFT JOIN Suoritukset S ON K.id = S.kurssi_id WHERE O.nimi = ?",[teacher_name]).fetchone()
    return pisteet[0]

# hakee opiskelijan suorittamat kurssit arvosanoineen (aakkosjärjestyksessä)
def courses_by_student(student_name):
    suoritukset = db.execute("SELECT K.nimi, S.arvosana FROM Opiskelijat O LEFT JOIN Suoritukset S ON O.id = S.opiskelija_id LEFT JOIN Kurssit K ON K.id = S.kurssi_id WHERE O.nimi = ? ORDER BY K.nimi", [student_name]).fetchall()
    return suoritukset

# hakee tiettynä vuonna saatujen opintopisteiden määrän
def credits_by_year(year):
    pisteet = db.execute("SELECT SUM(K.opintopisteet) FROM Kurssit K, Suoritukset S WHERE K.id = S.kurssi_id AND strftime('%Y',S.pvm) = ?",[str(year)]).fetchone()
    return pisteet[0]

# hakee kurssin arvosanojen jakauman (järjestyksessä arvosanat 1-5)
def grade_distribution(course_name):
    jakauma = db.execute("SELECT S.arvosana, COUNT(*) FROM Suoritukset S LEFT JOIN Kurssit K  ON K.id = S.kurssi_id WHERE K.nimi = ? GROUP BY S.arvosana ORDER BY S.arvosana ASC ", [course_name]).fetchall()
    arvosanat = {}
    for i in range(1,6):
        j = next((x for arvosana, x in jakauma if arvosana == i), 0)
        arvosanat.update({i:j})
    
    return arvosanat
# hakee listan kursseista (nimi, opettajien määrä, suorittajien määrä) (aakkosjärjestyksessä)
def course_list():
    lista = db.execute("SELECT K.nimi, COUNT(DISTINCT Q.opettaja_id), COUNT(DISTINCT S.opiskelija_id) FROM Kurssit K LEFT JOIN Suoritukset S ON K.id = S.kurssi_id LEFT JOIN KurssinOpettajat Q ON K.id = Q.kurssi_id GROUP BY K.nimi ORDER BY K.nimi").fetchall()
    return lista

# hakee listan opettajista kursseineen (aakkosjärjestyksessä opettajat ja kurssit)
def teacher_list():
    lista = db.execute("SELECT O.nimi, K.nimi FROM Opettajat O LEFT JOIN KurssinOpettajat Q ON O.id = Q.opettaja_id LEFT JOIN Kurssit K ON K.Id = Q.kurssi_id ORDER BY O.nimi").fetchall()
    return lista

# hakee ryhmässä olevat henkilöt (aakkosjärjestyksessä)
def group_people(group_name):
    Opettajat = db.execute("SELECT O.nimi FROM Ryhmat R LEFT JOIN RyhmanOpettajat Q ON R.id = Q.ryhma_id LEFT JOIN Opettajat O ON O.id = Q.opettaja_id WHERE R.nimi = ? ", [group_name]).fetchall()
    Opiskelijat = db.execute("SELECT O.nimi FROM Ryhmat R LEFT JOIN RyhmanOpiskelijat Q ON R.id = Q.ryhma_id LEFT JOIN Opiskelijat O ON O.id = Q.opiskelija_id WHERE R.nimi = ?", [group_name]).fetchall()
    henkilot=[]
    for opettaja in Opettajat:
        henkilot.append(opettaja[0])
    for opiskelija in Opiskelijat:
        henkilot.append(opiskelija[0])
    jarjestetty = sorted(henkilot)
    return jarjestetty

# hakee ryhmissä saatujen opintopisteiden määrät (aakkosjärjestyksessä)
def credits_in_groups():
    pass

# hakee ryhmät, joissa on tietty opettaja ja opiskelija (aakkosjärjestyksessä)
def common_groups(teacher_name, student_name):
    pass