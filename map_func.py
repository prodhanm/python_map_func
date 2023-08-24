names = ["Mufassa Whatta", "Sabina Whatta", "Fazwan Whattta", \
         "Nuaym Whatta"]

def email_join(item):
    name= item.replace(" ", ".")
    return name + "@whatta.com"
        
def main():
    email_list = list(map(email_join,names))
    for index, email in enumerate(email_list, 1):
        print(email.lower())

if __name__ == "__main__":
    main()