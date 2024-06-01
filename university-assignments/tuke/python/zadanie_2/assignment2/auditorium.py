class Auditorium:
    def __init__(self, capacity):
        self.capacity = capacity
        self.screenings = list()

    def is_available(self, new_screening):
        if new_screening == ' ':
            return True
        for screening in self.screenings:

            t1_start = int(screening.time[0]) * 60 + int(screening.time[1])
            t1_end = t1_start + screening.movie.length

            t2_start = int(new_screening.time[0]) * 60 + int(new_screening.time[1])
            t2_end = t2_start + new_screening.movie.length

            if t1_start < t2_start < t1_end or t1_start < t2_end < t1_end:
                return False
        return True

    def add_screening(self, new_screening):
        if self.is_available(new_screening):
            self.screenings.append(new_screening)
            return True
        return False


if __name__ == '__main__':
    # you can run your tests here
    # test_screening = Screening(Movie("GHI", 80, "comedy", 16, "2023/03/31"), 105, (19, 35))
    # auditorium = Auditorium(100)
    # print(auditorium.add_screening(test_screening))
    pass
