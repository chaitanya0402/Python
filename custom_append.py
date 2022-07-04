from operator import attrgetter
class Country:
    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area
    def __repr__(self):
        return((self.name,self.population,self.area))
countries=[Country("India",1200,300),
           Country("China",1200,200),
           Country("USA",1200,400)]
countries.append(Country("Russia",3200,700))
countries.sort(key=attrgetter('population'))
print(countries)

