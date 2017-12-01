from TwitterAPI import TwitterAPI

# Initialize some variables
consumerkey     = ""
consumersecret  = ""
accesstoken     = ""
accesssecret    = ""

for linetoken in open("tokens.txt"):

    # Remove the newline
    linetoken = linetoken[0:len(linetoken)-1]

    # Check the specific tokens and assign them
    if ("consumerkey" in linetoken):
        consumerkey = linetoken.split(":")[1]
    if ("consumersecret" in linetoken):
        consumersecret = linetoken.split(":")[1]
    if ("accesstoken" in linetoken):
        accesstoken = linetoken.split(":")[1]
    if ("accesssecret" in linetoken):
        accesssecret = linetoken.split(":")[1]

# Some debugging prints

print("consumerkey: " + consumerkey + ":")
print("consumersecret: " + consumersecret)
print("accesstoken: " + accesstoken)
print("accesssecret: " + accesssecret)

# Call the TwitterAPI construct
api = TwitterAPI(consumerkey, consumersecret, accesstoken, accesssecret)

# Search some tweets
tweets = api.request('search/tweets', {'q': 'h1b', 'count': 100})

# Print them
print(tweets.text)


# This line should be in R1 only - after being merged