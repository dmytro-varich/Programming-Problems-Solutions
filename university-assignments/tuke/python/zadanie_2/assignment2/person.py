class Person:
    def __init__(self, interests, age, bedtime, tolerance):
        self.interests = interests
        self.age = age
        self.bedtime = bedtime
        self.tolerance = tolerance

    def is_interested(self, movie):
        if movie.genre in self.interests:
            return True
        return False

    def is_allowed(self, movie):
        if self.age >= movie.age_limit:
            return True
        return False

    def can_attend(self, screening):
        if screening.get_end_time()[0] < self.bedtime and self.is_allowed(screening.movie):
            return True
        return False

    def will_attend(self, screening):
        if self.tolerance > screening.get_occupancy():
            return True
        return False


if __name__ == '__main__':
    # you can run your tests here
    pass
