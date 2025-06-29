import json

urls = []
with open("./output.txt", "r") as file:
    for line in file:
        if line.startswith("-"):        
            urls.append(line.split()[1])
     
with open("./output.json", "w") as file:
    json.dump(urls, file, indent=4)       

print("Done")