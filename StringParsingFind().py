email = "From seanteamsy@unb.ca Sat Jan 2019 09:14:16 2020"
atpos = email.find("@")
#print(atpos)
#testing coords
sppos = email.find(" ", atpos)
#print(sppos)
host= email[atpos+1 : sppos]
print(host)