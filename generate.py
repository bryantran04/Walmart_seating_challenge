if __name__ == "__main__":
    file_name = sys.argv[1]

    f = open(file_name+"_"+"results", "w+")
    for i in range(len(movie_theater.reservations)):
        reservation_id = movie_theater.reservations[i][0]
        output = reservation_id + " "
        for seat in movie_theater.reservation_id_to_seats[reservation_id]:
            output += row_to_char[seat[0]]+str(seat[1]+1)+","
        f.write(output[:-1]+"\n")
