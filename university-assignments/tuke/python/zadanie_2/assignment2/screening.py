class Screening:
    def __init__(self, movie, auditorium, time):
        self.movie = movie
        self.auditorium = auditorium
        self.time = time
        self.tickets_sold = 0

    def sell_tickets(self, count):
        if self.auditorium.capacity >= self.tickets_sold + count:
            self.tickets_sold += count
            return True
        else:
            return False

    def get_occupancy(self):
        return self.tickets_sold / self.auditorium.capacity

    def get_end_time(self):
        time_start = int(self.time[0]) * 60 + int(self.time[1])
        total_minutes = time_start + self.movie.length
        hours, minutes = divmod(total_minutes, 60)
        return (hours, minutes)


if __name__ == '__main__':
    # you can run your tests here
    pass
