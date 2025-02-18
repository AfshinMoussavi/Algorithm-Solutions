# Name: سایت فیلم
# URL:  https://quera.org/problemset/220672


def validateCommand(command, *args):
    if command == 'ADD-MOVIE':
        title = args[0]
        date = int(args[1])
        quality = args[2]
        movie = Movie(title, date, quality)
        print(f"added successfully {movie.id}")
    elif command == 'REM-MOVIE':
        movie_id = int(args[0])
        movie = Movie.remove(movie_id)
        print(f"removed successfully {movie.id}")
    elif command == 'ADD-CAST':
        name = args[0]
        cast = Cast(name)
        print(f"added successfully {cast.id}")
    elif command == 'REM-CAST':
        cast_id = int(args[0])
        cast = Cast.remove(cast_id)
        print(f"removed successfully {cast.id}")
    elif command == 'SHOW-MOVIE':
        movie_id = int(args[0])
        movie = Movie.get(movie_id)
        print(movie)
    elif command == 'SHOW-CAST':
        cast_id = int(args[0])
        cast = Cast.get(cast_id)
        print(cast)
    elif command == 'LINK-CAST-TO-MOVIE':
        cast_id = int(args[0])
        movie_id = int(args[1])
        link(cast_id, movie_id)
        print(f'successfully linked {cast_id} to {movie_id}')
    elif command == 'FILTER-MOVIES-BY-TITLE':
        print(Movie.filter(args[0], 'title'))
    elif command == 'FILTER-MOVIES-BY-DATE':
        print(Movie.filter(args, "date"))
    elif command == 'FILTER-MOVIES-BY-QUALITY':
        print(Movie.filter(args[0], 'quality'))

        
def link(cast_id, movie_id):
        cast = Cast.get(cast_id)
        movie = Movie.get(movie_id)
        if cast_id in movie.casts or movie_id in cast.movies:
            raise AlreadyLink
        cast.movies.append(movie.id)
        movie.casts.append(cast.id)

        

class InvalidMovieTitle(BaseException):
    def __str__(self):
        return "invalid title"

class InvalidMovieDate(BaseException):
    def __str__(self) -> str:
        return "invalid date"

class InvalidMovieQuality(BaseException):
    def __str__(self) -> str:
        return "invalid quality"

class InvalidMovieId(BaseException):
    def __str__(self) -> str:
        return "invalid movie id"

class InvalidCastName(BaseException):
    def __str__(self) -> str:
        return "invalid name"

class InvalidCastId(BaseException):
    def __str__(self) -> str:
        return "invalid cast id"

class AlreadyLink(BaseException):
    def __str__(self) -> str:
        return "already linked"



class Movie:
    last_id = 0
    objects = {}
    
    def __init__(self, title, date, quality):
        Movie.validate(title, date, quality)
        self.title = title
        self.date = date
        self.quality = quality
        self.casts = []
        self.id = Movie.last_id
        Movie.last_id += 1
        Movie.objects[self.id] = self
    
    @staticmethod
    def validate(title, date, quality):
        if len(title) > 20:
            raise InvalidMovieTitle
        if not 1888 <= date <= 2024:
            raise InvalidMovieDate
        if quality not in ['720p', '1080p', '4K']:
            raise InvalidMovieQuality
    
    @classmethod
    def remove(cls, id):
        if not id in Movie.objects:
            raise InvalidMovieId
        movie = cls.objects.pop(id)
        for cast_id in movie.casts:
            Cast.objects[cast_id].movies.remove(id)
        return movie
    
    @classmethod
    def get(cls, id):
        if  id not in cls.objects:
            raise InvalidMovieId
        return cls.objects[id]
    
    def __str__(self):
        return f'{{title:"{self.title}", date:"{self.date}", quality:"{self.quality}", casts:{list(sorted(self.casts))}}}'
        
    @classmethod
    def filter(cls,pattern,by):
        if by=="title":
            return list(sorted([
                x.id for x in cls.objects.values()
                  if x.title.startswith(pattern)]))
        
        elif by=="quality":
            return list(sorted([
                x.id for x in cls.objects.values()
                  if x.quality == pattern]))
            
        elif by=="date":
            ineq,n=pattern
            if ineq=="=":
                ineq="=="

            return list(sorted([
                x.id for x in cls.objects.values()
                  if eval(f"{x.date}{ineq}{n}") ]))
        else:
            raise Exception("invalid by parameter")

    
class Cast:
    last_id = 0
    objects = {}
    def __init__(self, name):
        Cast.validate(name)
        self.name = name
        self.movies = []
        self.id = Cast.last_id
        Cast.last_id += 1
        Cast.objects[self.id] = self
    
    @staticmethod
    def validate(name):
        if len(name)>20:
            raise InvalidCastName
        if not name.isalpha():
            raise InvalidCastName

    @classmethod
    def remove(cls,id):
        if not id in cls.objects:
            raise InvalidCastId
        cast= cls.objects.pop(id)
        for movie_id in cast.movies:
            Movie.objects[movie_id].casts.remove(id)
        return cast
    
    @classmethod
    def get(cls, id):
        if id not in cls.objects:
            raise InvalidCastId
        return cls.objects[id]
    
    def __str__(self):
        return f'{{name:"{self.name}", movies:{list(sorted(self.movies))}}}'
    
    

n = int(input())
for i in range(n):
    try:
        command, *data = input().split()
        validateCommand(command, *data)
    except BaseException as e:
        print(e)


