from screening import Screening


class Cinema:
    def __init__(self, auditoriums):
        self.auditoriums = auditoriums
        self.screenings = list()

    def add_movie(self, movie, screening_times):
        for time in screening_times:
            time_tuple = (int(time[0]), int(time[1]))
            found_auditorium = False

            for auditorium in self.auditoriums:
                if auditorium.is_available(Screening(movie, auditorium, time_tuple)):
                    self.screenings.append(Screening(movie, auditorium, time_tuple))
                    auditorium.add_screening(self.screenings[-1])
                    found_auditorium = True
                    break
            if not found_auditorium:
                raise RuntimeError(f"Could not add movie {movie.title} at {time[0]:02d}:{time[1]:02d}")

    def get_movies_shown(self):
        return list(set([screening.movie for screening in self.screenings]))

    def get_screenings_for_movie(self, movie):
        return [screening for screening in self.screenings if screening.movie == movie]


if __name__ == '__main__':
    # you can run your tests here
    pass
