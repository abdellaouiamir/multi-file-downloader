import json

loded_lines = []

with open("./output.json", "r") as file:
    loded_lines = json.load(fp=file)
    
print(loded_lines[0])