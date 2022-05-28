class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = int(age)
        self.tracks = [tracks]
        self.score = float(score)

    def change_name(self, new_name):
        self.name=new_name
        return self.name
        #return new_name

    def change_age(self,new_age):
        self.age= new_age
        return self.age
        #return new_age

    def add_track(self,new_track):
        self.tracks = (new_track) 
        return self.tracks
        #return new_track

    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())