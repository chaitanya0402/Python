class Book:
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author

    def reps(self):
        return repr((self.id,self.name,self.author))

    def add_review(self,review):
        self.add_review.append(review)


class Review:
    def __init__(self,id,desc,rating):
        self.id=id
        self.desc=desc
        self.rating=rating


    def __repr__(self):
        return repr((self.id,self.desc,self.rating))


b=Book(123,"OOPs","ABC")
r=Review(10,"Great book",5)
print(b)
print()
