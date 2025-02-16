# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dic = {}
    dic["name"] = name
    dic["director"] = director
    dic["year"] = year
    dic["runtime"] = runtime
    return database.append(dic)

if __name__=="__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)