
consumerkey     = ""
consumersecret  = ""
accesstoken     = ""
accesssecret    = ""

for linetoken in open("tokens.txt"):
    if ("consumerkey" in linetoken):
        consumerkey = linetoken.split(":")[1]
    if ("consumersecret" in linetoken):
        consumersecret = linetoken.split(":")[1]
    if ("accesstoken" in linetoken):
        accesstoken = linetoken.split(":")[1]
    if ("accesssecret" in linetoken):
        accesssecret = linetoken.split(":")[1]

print("consumerkey: " + consumerkey)
print("consumersecret: " + consumersecret)
print("accesstoken: " + accesstoken)
print("accesssecret: " + accesssecret)

