class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __convert_to_km__(self, other):
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other):
        return Distance(self.km + self.__convert_to_km__(other))

    def __iadd__(self, other):
        self.km += self.__convert_to_km__(other)

    def __mul__(self, other):
        return Distance(self.km * self.__convert_to_km__(other))

    def __truediv__(self, other):
        return Distance(round(self.km / self.__convert_to_km__(other), 2))

    def __lt__(self, other):
        return self.km < self.__convert_to_km__(other)

    def __gt__(self, other):
        return self.km > self.__convert_to_km__(other)

    def __eq__(self, other):
        return self.km == self.__convert_to_km__(other)

    def __le__(self, other):
        return self.km <= self.__convert_to_km__(other)

    def __ge__(self, other):
        return self.km >= self.__convert_to_km__(other)
