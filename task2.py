def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats.append({
                    "id": id,
                    "name": name,
                    "age": age
                    })
            return cats
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0 

cats_info = get_cats_info("cats.txt")
print(cats_info)