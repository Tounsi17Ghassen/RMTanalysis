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
    t=multisplit(txt,[" ",",","-","_","/","(",")",":","?",".","[","]","'","|","*","#",";","+"])
    for tt in t:
        try:
            f.write(tt)
        except:
            f.write("")

        f.write("\n")
f.close()


stops=open('stops.txt').read()
f = open("comments.txt", "r")
merge =open("synonyms.txt", "r")
outfile = "cleaned_file.txt"
fout = open(outfile, "w")
stops=multisplit(stops,["\n"])
for line in f:
    for word in stops:
        if(str(line)==str(word+"\n")):
            line=""
    fout.write(line)

'''    for word in merge:
        m=word.split(":")
        mk=m[0]
        mv=m[1].split(",")
        if(line in mv):
            print('yes')
            line=mk
'''
fout.close()
f.close()
merge.close()
f = open(outfile, "r")


fw = open("c1.txt", "w")

#print (stops,"    ")
(r,b) =process_tokens(f)
i=-1
for m1 in r.values():
    i+=1
    j=-1
    for m2 in r.keys():
            j+=1
            if(i==j):
                    zstr=str(m1)+" "+m2
                    fw.write(zstr)

fw.close()
