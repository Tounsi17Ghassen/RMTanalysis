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
f = open("comments.txt", "r")
p = open("players.txt", "r")
c = open("cleaned_file.txt", "w")
t = open("trash.txt", "w")
azerty=0
for l in p:
        player=l.split(":")
        gg=player[1].split(",")
        gg = gg[:-1]
        gg.insert(0,player[0])
        for g in gg:
            for line in f:
                azerty += 1;
                for cx in [",", "-", "_", "/", "(", ")", ":", "?", ".", "[", "]", "'", "|", "*", "#", ";", "+"]:
                    line = line.replace(cx, " ")
                    print(azerty)
                mxm=line.count(g)
                if (mxm!=0):
                    c.write(player[0])
                    c.write("\n")
                    line=line.replace(g,"")


t.close()
c.close()
p.close()
f.close()

c = open("cleaned_file.txt", "r")
t = open("trash.txt", "r")
c1 = open("c1.txt", "w")
t1 = open("t1.txt", "w")
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

(r,b) =process_tokens(t)
i=-1
for m1 in r.values():
    i+=1
    j=-1
    for m2 in r.keys():
            j+=1
            if(i==j):
                    zstr=str(m1)+" "+m2
                    t1.write(zstr)


t.close()
c.close()
c1.close()
t1.close()
