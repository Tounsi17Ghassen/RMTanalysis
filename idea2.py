import json
from tokenization import process_tokens


def sblit(ch,c):
    s=[]
    for h in ch:
        for y in h.split(c):
            if(y!=""):
                s.append(y)
    return s

def multisplit(ch,c):
    s=[]
    s.append(ch)
    for k in c:
        s=sblit(s,k)
    return s



with open("entry.json", "r") as read_file:
    data = json.load(read_file)

#with open("data_file.json", "w") as write_file:
#    json.dump(data,write_file, indent=4)


data=data[1]
data=data["data"]
data=data["children"]
f = open("comments.txt", "w")
data = data[:-1]
for d in data:
    d = d["data"]
    txt = d["body"]
    try:
            f.write(txt)
    except:
            f.write("")
    f.write("\n")
f.close()
p = open("players.txt", "r")
c = open("cleaned_file.txt", "w")
for dico in p:
    playTab=[]
    playTab.append(dico.split(":")[0])
    playTab.append(dico.split(":")[0].lower())
    playTab.append(dico.split(":")[0].upper())
    syns=dico.split(":")[1].split(",")
    for snm in syns:
        if(snm!="\n"):
            playTab.append(snm)
            playTab.append(snm.lower())
            playTab.append(snm.upper())
    f = open("comments.txt", "r")
    for line in f:
        for player in playTab:
            if player in line:
                c.write(playTab[0]);
                c.write("\n");
    f.close()

c.close()
p.close()
c = open("cleaned_file.txt", "r")
c1 = open("c1.txt", "w")
(r,b) =process_tokens(c)
i=-1
for m1 in r.values():
    i+=1
    j=-1
    for m2 in r.keys():
            j+=1
            if(i==j):
                    zstr=str(m1)+" "+m2
                    c1.write(zstr)

c.close()
c1.close()


f = open("comments.txt", "r")
p = open("players.txt", "r")
c = open("c_r.txt", "w")
playTab = []
for dico in p:
    playTab.append(dico.split(":")[0])
    playTab.append(dico.split(":")[0].lower())
    playTab.append(dico.split(":")[0].upper())
    syns=dico.split(":")[1].split(",")
    for snm in syns:
        if(snm!="\n"):
            playTab.append(snm)
            playTab.append(snm.lower())
            playTab.append(snm.upper())
for line in f:
    splitted= multisplit(line,[" ",",", "-", "_", "/", "(", ")", ":", "?", ".", "[", "]", "'", "|", "*", "#", ";", "+"])
    line=""
    for sp in splitted:
        line=line+"\n"+sp
    for player in playTab:
        if player in line:
            line=line.replace(player,"")
    c.write(line)
f.close()
c.close()
p.close()




f = open("c_r.txt", "r")
t = open("trash.txt", "w")
(br,bb)=process_tokens(f)
bi=-1
for bm in br.keys():
    bi+=1
    bj=-1
    for mz in br.values():
                bj+=1
                if(bi==bj):
                    zstr=str(mz)+" "+bm
                    t.write(zstr)

f.close()
t.close()

t = open("trash.txt", "r")
c1 = open("c1.txt", "r")
t1 = open("t1.txt", "w")
for tline in t:
    tt=tline.split(" ")[1]
    test=True
    for cline in c1:
        ct=cline.split(" ")[1]
        if(ct==tt):
            test=False
    if(test):
        t1.write(tline)
t.close()
t1.close()
c1.close()
