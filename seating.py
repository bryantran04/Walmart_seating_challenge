import heapq
import collections
import sys


class Movie_Theater_Seating_System():
    def __init__(self):
        self.reservations = []
        self.heap = []
        self.reservation_id_to_seats = collections.defaultdict(list)
        self.max_consec = [20 for i in range(10)]
        self.movie_theater_seats = [
            ["_" for i in range(20)] for j in range(10)]
        self.num_of_people = 0

    def input_reservation(self, file_name):
        for reservation in open(file_name):
            reservation_split = reservation.rstrip('\n').split()
            self.reservations.append(reservation_split)

            request_id = reservation_split[0]
            num_people_in_request = int(reservation_split[1])
            self.num_of_people += num_people_in_request
            heapq.heappush(self.heap, (-1*num_people_in_request, request_id))

    def start_assigning_seats(self):
        #While there are request that still needs to be processed
        while(self.heap):
            popped = heapq.heappop(self.heap)
            num_people = popped[0]*-1
            reservation_id = popped[1]
            if num_people > max(self.max_consec):
                first_split = num_people//2
                second_split = num_people-first_split
                heapq.heappush(self.heap, (first_split*-1, popped[1]))
                heapq.heappush(self.heap, (second_split*-1, popped[1]))
            elif num_people > 10:
                first_split = num_people//2
                second_split = num_people-first_split
                heapq.heappush(self.heap, (first_split*-1, popped[1]))
                heapq.heappush(self.heap, (second_split*-1, popped[1]))
            else:
                current_row = -1
                empty_seats = 0
                for i in range(len(self.max_consec)):
                    if self.max_consec[i] >= (num_people*-1):
                        if self.max_consec[i] >= empty_seats:
                            empty_seats = self.max_consec[i]
                            current_row = i
                if current_row % 2 == 0:
                    first_index = self.index_of_first_seat_left(
                        current_row, num_people)
                else:
                    first_index = self.index_of_first_seat_right(
                        current_row, num_people)
                self.seating_people(current_row, first_index,
                                    num_people, reservation_id)
                self.recalcuate_max_consecutive_seats_in_row(current_row)
    ##Find first index of n consecutive open seats

    def index_of_first_seat_left(self, row, number_of_consecutive):
        current = 0
        found = False
        index = 0
        while(not found):
            current = 0
            for i in range(index, index+number_of_consecutive):
                if self.movie_theater_seats[row][i] == '_':
                    current += 1
                    if current == number_of_consecutive:
                        return index
                else:
                    index = i + 1
                    break
            if index >= len(self.movie_theater_seats[0]):
                return -1
        if current < number_of_consecutive:
            return -1
        else:
            return index

    def index_of_first_seat_right(self, row, number_of_consecutive):
        current = 0
        found = False
        index = len(self.movie_theater_seats[row])
        while(not found):
            current = 0
            for i in reversed(range(index-number_of_consecutive, index)):
                if self.movie_theater_seats[row][i] == '_':
                    current += 1
                    if current == number_of_consecutive:
                        return i
                else:
                    index = i - 1
                    break
            if index < 0:
                return -1
        if current < number_of_consecutive:
            return -1
        else:
            return index

    def seating_people(self, row, index, num_people, reservation_id):
        for i in range(num_people):
            self.movie_theater_seats[row][index+i] = "t"
            self.reservation_id_to_seats[reservation_id].append((row, index+i))

    def recalcuate_max_consecutive_seats_in_row(self, row):
        max_consecutive = 0
        cur_max = 0
        for i in range(len(self.movie_theater_seats[row])):
            if self.movie_theater_seats[row][i] == "_":
                cur_max += 1
            else:
                cur_max = 0
            max_consecutive = max(max_consecutive, cur_max)
        self.max_consec[row] = max_consecutive

    def empty_theater(self):
        self.reservations = []
        self.heap = []
        self.reservation_id_to_seats = collections.defaultdict(list)
        self.max_consec = [20 for i in range(10)]
        self.movie_theater_seats = [
            ["_" for i in range(20)] for j in range(10)]
        self.num_of_people = 0


if __name__ == "__main__":
    file_name = sys.argv[1]

    row_to_char={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}
    movie_theater = Movie_Theater_Seating_System()
    movie_theater.input_reservation(file_name)
    movie_theater.start_assigning_seats()

    f = open(file_name+"_"+"results", "w+")
    for i in range(len(movie_theater.reservations)):
        reservation_id = movie_theater.reservations[i][0]
        output = reservation_id + " "
        for seat in movie_theater.reservation_id_to_seats[reservation_id]:
            output += row_to_char[seat[0]]+str(seat[1]+1)+","
        f.write(output[:-1]+"\n")

