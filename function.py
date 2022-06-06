# Function

def mycar():
    print("My first car was Nissan")
    print("My second car was Jeep")


mycar()


def familymembers(*memb):
    print("My sister :" + memb[2])

familymembers("Hari", "Gujesowari", "Ruja", "Rujan")

def mychild(child1: str, child2: str, child3: str) :
    print("My youngest child is :" +child1)
mychild(child1 = "rajat", child2 = "Rujan",child3 = "Ruja")


def my_detail(**person):
    print(f"My age is :{person['age']}")
person = {
    "name" :"rajat",
    "age" :25,
    "address":"banepa"
}
my_detail(**person)


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


"""def my_name(name:str,age:int,Dob:str,address:str):
    print("{name}")
    print("{age}")
    print("{Dob}")
    print("{address}")

my_name("Rajat",23,"sep17","banepa")"""