names = ["Mufassa Whatta", "Sabina Whatta", "Fazwan Whattta", \
         "Nuaym Whatta"]

def email_join(item):
    name= item.replace(" ", ".")
    return name + "@gmail.com"
        
def main():
    email_list = list(map(email_join,names))
    print(email_list)

if __name__ == "__main__":
    main()

'''
join_name = li[name].replace(" ", ".")
        email_name = join_name + '@gmail.com'
        print(email_name.lower())
'''