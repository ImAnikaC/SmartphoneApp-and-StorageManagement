'''
Anika Chowdhury 5/4/22 
'''

class Smartphone:
  
    def __init__(self, capacity, name):
        self.capacity = int (capacity)
        self.available = self.capacity
        self.name = name
        self.dic = {}
        self.total = 0
        print ("Smartphone created!")
        
        
    def add_app(self, appname, appsize):
        self.appname = appname
        self.appsize = appsize

        #if it exists
        if self.appname in self.dic:
            print ("Rejected", self.appname, "already exists")

        #not enough storage
        elif self.available-self.appsize <= 0:
            print ("Cannot install app, no available space")

        elif self.available-self.appsize > 0:
            self.dic[self.appname] = self.appsize
            self.available -= self.appsize
            self.total += self.appsize

        print ()

    def remove_app(self, appname):
        self.appname = appname
        
        #check to see if it exits  
        if self.appname in self.dic:
            apps = self.dic.get(self.appname)
            self.total -= apps
            self.available +=apps
            del self.dic[self.appname]
            print ("App removed:", appname) 

        #if app doesn't exist
        else:
            print ("App does not exist")

        print ()

    def has_app(self, appname):
        self.appname = appname
        if self.appname in self.dic:
            return True
        else:
            return False

        print ()

    def get_available_space(self):
        return self.available

    def report (self):
        print ("Name:", self.name)
        print ("Capacity:", self.total, "out of", self.capacity, "GB")
        print ("Available space:", self.available)
        print ("Apps installed:", len(self.dic))
        ordered_dic = dict(sorted(self.dic.items()))
        for key,value in ordered_dic.items():
            print ('*', key, 'is using', value, 'GB')

        print ()
        
#Tester Code
size = int (input ("Size of your new smartphone (GB): "))
phonename = input ("Smartphone name: ")
phone = Smartphone(size,phonename)
phone.report()

choice = input ("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
choice = choice.lower()

while choice != 'q':
    
    if choice == 'r':
        phone.report()

    elif choice == 'a':
        appsname = input ("App name to add: ")
        appssize = int (input ("App size in GB: "))
        phone.add_app(appsname,appssize)

    elif choice == 'e':
        remove = input ("App name to remove: ")
        phone.remove_app(remove)

    choice = input ("(r)eport, (a)dd app, r(e)move app or (q)uit: ")

    if choice == 'q':
        print ("Goodbye!")
