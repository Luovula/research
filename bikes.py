import sqlite3

db = sqlite3.connect("bikes.db")
db.isolation_level = None

def distance_of_user(user):
    distance = db.execute("SELECT SUM(T.distance) FROM Trips T, Users U WHERE U.id = T.user_id AND U.name = ?", [user]).fetchone()
    return distance
    

def speed_of_user(user):
    distance = distance_of_user(user)
    duration = db.execute("SELECT SUM(T.duration) FROM Users U, Trips T WHERE U.id = T.user_id AND U.name = ?",[user]).fetchone()
    hours = duration[0]/60
    km = distance[0] / 1000
    speed = km/hours
    return round(speed,2)

def duration_in_each_city(day):
    duration = db.execute("SELECT C.name, SUM(T.duration) FROM Cities C JOIN Bikes B ON C.id = B.city_id JOIN TRIPS T ON B.id = T.bike_id WHERE T.day = ? GROUP BY C.name", [day]).fetchall()
    return duration

def users_in_city(city):
    users = db.execute("SELECT COUNT(DISTINCT U.id) FROM Users U JOIN Trips T ON U.id = T.user_id JOIN Bikes B ON B.id = T.bike_id JOIN Cities C ON C.id = B.city_id WHERE C.name = ?", [city]).fetchone()
    return users

def trips_on_each_day(city):
    trips = db.execute("SELECT T.day, COUNT(T.id) FROM Trips T JOIN Bikes B ON B.id = T.bike_id JOIN Cities C ON C.id = B.city_id WHERE C.name = ? GROUP BY T.day", [city]).fetchall()
    return trips

def most_popular_start(city):
    popular = db.execute("SELECT S.name, COUNT(T.id) FROM Stops S JOIN Trips T ON S.id = T.from_id JOIN Cities C ON C.id = S.city_id WHERE C.name = ? GROUP BY S.id ORDER BY COUNT(T.id) DESC", [city]).fetchone()
    return popular