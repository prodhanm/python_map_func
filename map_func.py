names = ["Mufassa Whatta", "Sabina Whatta", "Fazwan Whattta", \
         "Nuaym Whatta"]

def email_join(item):
    try:
        name= item.replace(" ", ".")
        return name + "@whatta.com"
    except TypeError as err:
        print(err)

def main():
    try:
        email_list = list(map(email_join,names))
        for email in range(len(email_list)):
            email_list[email]

        dict_name = dict(zip(names,email_list))
        print(f"email data = {dict_name}")
    except (KeyError, ValueError) as err:
        print(err)

if __name__ == "__main__":
    main()