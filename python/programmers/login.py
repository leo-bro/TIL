def solution(id_pw, db):
    dbdict = dict(db)
    id = id_pw[0]
    pw = id_pw[1]
    if id in dbdict.keys():
        if pw == dbdict.get(id):
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
