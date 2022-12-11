# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
class Country:
    def __init__(self, area, language, religion, capital, GDP, growth, population ) -> None:
        self.area = area
        self.language = language
        self.religion = religion
        self.capital = capital
        self.GDP = GDP
        self.growth = growth
        self.population = population
        
        

spain = Country(505370, 'Castilian Spanish', 'Roman Catholic', 'Madrid', 1715 , 0.13, 47163418)
switzerland = Country(41277,'German', 'Roman Catholic', 'Bern',591 ,0.65 ,8508698)

print (switzerland.language == spain.language)
print (switzerland.religion == spain.religion)
print (len(spain.capital) != len(switzerland.capital))
print (switzerland.GDP > spain.GDP)
print (spain.growth < 1 and switzerland.growth < 1)
print (spain.population > 10000000 or switzerland.population > 10000000)
print (spain.population >10000000 and switzerland.population < 10000000 or spain.population < 10000000 and switzerland.population > 10000000)