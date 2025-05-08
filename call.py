class Person:
    def __init__(self, name,age,mark):   # Constructor with parameter
        self.name = name
        self.age = age
        self.mark= mark
                # Key-value pair: self.name is the key, value comes from the argument
                

    def greet(self):
        print(f"Hello, {self.name}!,Your age is  {self.age},Your mark is  {self.mark}")  # Accessing the key (attribute)
       
p = Person("Alice",23,400)
             # Creating object with name "Alice"
p.greet()                       # Output: Hello, Alice!
