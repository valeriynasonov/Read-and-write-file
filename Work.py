with open("Поваренная книга", "rt") as f:
    cook_book = {}
    while f:
        line = f.readline().strip()
        common_list = []
        cook_book[line] = common_list
        line = int(f.readline().strip())
        while line > 0:
            line -= 1
            list_of_ingr = f.readline().strip().split("|")
            c = {"ingredient_name": list_of_ingr[0], "quantity": list_of_ingr[1], "measure": list_of_ingr[2]}
            common_list.append(c)
        print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        t = {}
        for k, v in cook_book.items():
            if k == dishes:
                for element in v:
            t[element["ingredient_name"]] = element
            del element["ingredient_name"]
            element["quantity"]=int(element["quantity"])
            element["quantity"]*=person_count
        return t
  print(get_shop_list_by_dishes("Фахитос", 8))

