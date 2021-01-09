import random as rand


class CinemaHall:
    def __init__(self, hall_name, movie, movie_time, movie_length, price, row, col):
        self.hall_name, self.movie, self.movie_time, self.movie_length, \
        self.price, self.row, self.col = hall_name, movie, movie_time, movie_length, price, row, col
        self.create_seats_in_the_hall(self.row, self.col)
        self.automatic_places_filling()

    def reservation_seat_in_the_hall(self, row, col):
        """Бронирование места в зале"""
        if self.seats_in_the_hall[row - 1][col - 1] != "[*]":
            self.seats_in_the_hall[row - 1][col - 1] = "[*]"
            return True
        return False

    def create_seats_in_the_hall(self, row, col):
        """Создание кресел с нужным кол-вом рядов и мест"""
        self.seats_in_the_hall = [["[ ]" for _ in range(self.col)] for _ in
                                  range(self.row)]  # Места в зале

    def automatic_places_filling(self):
        """Заполняет места в кинозале в зависимости от времени суток"""
        percent = 30
        try:
            hours, minutes = int(self.movie_time.split(":")[0]), int(self.movie_time.split(":")[1])
            if (hours, minutes) >= (18, 00):
                percent = 10
        except IndexError:
            percent = 30
        num = round(self.row * self.col * (percent / 100))
        for _ in range(num):
            row = rand.randint(1, self.row)
            col = rand.randint(1, self.col)
            self.seats_in_the_hall[row - 1][col - 1] = "[*]"

    def get_occupied_seat(self):
        """Кол-во занятых мест в зале"""
        total = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.seats_in_the_hall[i - 1][j - 1] == "[*]":
                    total += 1
        return total

    def replace_film(self, new_movie, new_movie_time, new_movie_length):
        self.movie, self.movie_time, self.movie_length = new_movie, new_movie_time, new_movie_length


class Cinema:
    def __init__(self, cinema_name):
        self.cinema_name = cinema_name
        self.cinema_halls = []

    def add_cinema_hall(self, cinema_hall_name, movie, movie_time, movie_length, price, row,
                        col):
        """Добавление зала в кинотеатр"""
        if len(self.cinema_halls) != 3:
            self.cinema_halls.append(CinemaHall(cinema_hall_name, movie, movie_time,
                                                movie_length, price, row, col))
            return True
        return False

    def change_seats(self, cinema_hall_name, new_row, new_col):
        """Изменение кол-ва мест в зале"""
        if new_row <= 7 and new_col <= 14:
            for cinema_hall in self.cinema_halls:
                if cinema_hall.hall_name == cinema_hall_name:
                    cinema_hall.row = new_row
                    cinema_hall.col = new_col
                    cinema_hall.create_seats_in_the_hall(cinema_hall.row, cinema_hall.col)
            return True
        return False

    def get_hall_with_want_name(self, want_cinema_name):
        """Получить экземпляр класса кинозала по названию"""
        for cinema_hall in self.cinema_halls:
            if want_cinema_name == cinema_hall.hall_name:
                return cinema_hall

    def get_cinema_hall_names(self):
        """Функция возвращает список имён залов кинотеатра"""
        cinema_hall_names = []
        for cinema_hall in self.cinema_halls:
            cinema_hall_names.append(cinema_hall.hall_name)
        return cinema_hall_names


class CinemaNetwork:
    def __init__(self):
        self.cinemas = []
        self.create_start_configuration()

    def add_cinema(self, cinema_name):
        """Добавление кинотеатра в сеть кинотеатров"""
        if len(self.cinemas) != 5:
            self.cinemas.append(Cinema(cinema_name))
            return True
        return False

    def get_cinema_names(self):
        """Функция возвращает список имён кинотеатров"""
        cinema_names = []
        for cinema in self.cinemas:
            cinema_names.append(cinema.cinema_name)
        return cinema_names

    def get_cinema_with_want_name(self, want_cinema_name):
        """Получить экземпляр класса кинотеатра по названию"""
        for cinema in self.cinemas:
            if want_cinema_name == cinema.cinema_name:
                return cinema

    def delete_cinema(self, cinema_name):
        """Удаление кинотеатра"""
        self.cinemas.remove(self.get_cinema_with_want_name(cinema_name))

    def create_start_configuration(self):
        """Функция создаёт начальные кинотетры и фильмы в них"""
        self.add_cinema("Киномакс")
        self.add_cinema("Кино Хауз")
        self.add_cinema("Синема парк")
        for cinema in self.cinemas:
            if self.cinemas.index(cinema) == 0:
                cinema.cinema_halls = [
                    CinemaHall("Первый зал", "Интерстеллар", "14:50", 169, 250, 7, 14),
                    CinemaHall("Второй зал", "Мстители: Финал", "21:50", 181, 250, 7, 14)]
            elif self.cinemas.index(cinema) == 1:
                cinema.cinema_halls = [
                    CinemaHall("Первый зал", "Побег из Шоушенка", "15:35", 144, 250, 7, 14),
                    CinemaHall("Второй зал", "Список Шиндлера", "12:35", 195, 250, 7, 14)]
            else:
                cinema.cinema_halls = [
                    CinemaHall("Первый зал", "Начало", "23:20", 148, 250, 7, 14),
                    CinemaHall("Второй зал", "Властелин колец", "18:30", 301, 250, 7, 14)]
