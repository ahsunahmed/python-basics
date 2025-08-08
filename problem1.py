def unique_value_count(string):
    string_set = set(list(string))
    for i in string_set:
        if i!= " ":
            print(f"{i} = {string.count(i)}")

unique_value_count("Hello How Are You")