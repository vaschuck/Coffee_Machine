max_cats = -1
while True:
    cats = input()
    if cats == 'MEOW':
        break
    cat_info = cats.split()
    cat_count = int(cat_info[1])
    if cat_count > max_cats:
        max_cats = cat_count
        name_max = cat_info[0]

print(name_max)
