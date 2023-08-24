names = ["Mufassa Whatta", "Sabina Whatta", "Fazwan Whattta", \
         "Nuaym Whatta"]

def email_join(names):
    for name in range(len(names)):
        join_name = names[name].replace(" ", ".")
        email_name = join_name + '@gmail.com'
        print(email_name.lower())
            

def main():
    email_join(names)

if __name__ == "__main__":
    main()

'''
if name[n] == " ":
                dot_name = name[:len(name)//2] + '.' + name[len(name)//2:len(name)]
                print(dot_name)
'''