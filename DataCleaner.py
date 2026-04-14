def clean_data(data):
  seen = set()
  clean_list = []
  removed_count = 0
  for item in data:
        if item is None or item == "":
            removed_count += 1
            continue
        if item in seen:
            removed_count += 1
            continue
        seen.add(item)
        clean_list.append(item)
  clean_list.sort()
  return clean_list, removed_count
data= [10, None, 20, 10, "", 30, None, 40]
cleaned, removed = clean_data(data)
print("Cleaned List:", cleaned)
print("Removed Count:", removed)