from heapq import heappop, heappush

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return str.format("Title: {}, Year: {}", self.title, self.year)

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return not self.__eq__(other)
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

movie1 = Movie("Citizen Kane", 1941)
movie2 = Movie("Back to the Future", 1985)
movie3 = Movie("Forrest Gump", 1994)
movie4 = Movie("The Silence of the Lambs", 1991);
movie5 = Movie("Gia", 1998)

array = [movie1, movie2, movie3, movie4, movie5]

for movie in heap_sort(array):
    print(movie)