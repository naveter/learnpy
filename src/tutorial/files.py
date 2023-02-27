import json

with open('../../resource/filesDiff1.txt', encoding="utf-8") as f:
    for line in f:
        print(line.replace("\n", ""), end='; ')

    f.seek(0)
    read_data = f.read()    # return to begin

f.closed
print()
print(read_data.replace("\n", ", "))

x = [1, 'simple', 'list']
print(json.dumps(x))
# json.dump(x, f)   # serialize to file
# x = json.load(f)  # read json from file



