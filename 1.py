import json


hobbies = ["Chess","Watching"]

biodata = {
	"name" : "Gian",
	"address" : "Makassar",
	"hobbies" : hobbies,
	"is_Married" : False,
	"school" : {"HighSchool":"SMAN 4 Kendari", "University":"Uinversitas Hasanuddin"},
	"Skills" : [{"Name of skills" : "Chess"},{"Score":555}]
}

cvtJson = json.dumps(biodata)
print(cvtJson)