def can_sleep(i: int, sviller: str, bakke: str, alv: dict):
    # Dersom hele underlaget er jord og det ikke er noen sviller kan han fint sove der også.
    alv_length = sum(alv.values())
    if (
        all(bakke[i + j] == "j" for j in range(alv_length))
        and not any(sviller[i + j] == "*" for j in range(alv_length))
    ):
        return True
    
    # Han vil ha minst én sville som pute under hodet.
    head_offset = alv_length- alv["H"]
    if not any(sviller[i + head_offset + j] == "*" for j in range(alv["H"])):
        return False
    
    # Han liker ikke å ha noe trykkende på nakken, ingen sviller der. 
    neck_offset = alv_length - alv["N"] - alv["H"]
    if any(sviller[i + neck_offset + j] == "*" for j in range(alv["N"])):
        return False
    
    # Selvfølgelig liker han heller ikke sand i nakken!
    if any(bakke[i + neck_offset + j] == "s" for j in range(alv["N"])):
        return False
    
    # Han kan ha opp til én sville under bena som støtte.
    c = 0
    for j in range(alv["B"]):
        if sviller[i + j] == "*":
            c += 1
    if c > 1:
        return False
    
    # Han liker ikke grus! Det kan ikke være grus på noen del av underlaget, også under sviller.
    if any(bakke[i + j] == "g" for j in range(alv_length)):
        return False
    
    return True
    
data = open("el-paso_santa-cruz.txt").read().rstrip()
sviller, bakke = data.split("\n")
alv = {
    "H": 5,
    "N": 2,
    "O": 9,
    "R": 3,
    "B": 10
}
print(sum(1 if can_sleep(i, sviller, bakke, alv) else 0 for i in range(len(sviller) - sum(alv.values()))))