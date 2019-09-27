# Walmart_seating_challenge

<p>To use the script:<br>
/python3 seating.py file_name </p>

### Planning Notes

- Maximize Customer Satisfaction
  - Customers to prefer the back more
    - First assign customers in the back
    - even rows expand from the left
    - odd rows expand from the right
  - Customers prefer to have their own personal space
  - Customers want to be with their friends
    - If there is a ground with 10 or more, we should split them
    - We could keep them together, in adjcaent rows, or not.
- Theater utilization.
  - Have the customers spread out as much as possible
- Problems
  - Request that is more than a row length
    - Split between two halves and put the groups near each other
- Heap to prioritize requests:
  - Bigger groups should have higher priority
  - If you're by youself, it's easier to find a seat for you, since you don't want to be part of a group

### My algorithm

1. Input reservation request
2. Initialize my class

   - Class variables
     - reservations - list of reservations with the number of people in each request
     - heap - Tuples of reservation id, and the number of people
     - reservation_id_to_seats - hashtable that maps the reservation id to a list of seats
     - max_consec - List of ints, where the index maps to the number of consecutive seats open in that row
     - movie_theater_seats - Matrix representation of movie theater
     - num_of_people - total number of people in all requests

3. Loop through each row and put a tuple of (num_people,reservation_id) onto a max heap
   - Easier to deal with larger groups first, because smaller groups can fill in the gaps
4. While there are items on the heap
   - Pop an item off the heap
   - If the number of people in that item is more than the max of number of consecutive seats open in any row or greater than 10.
     - Break that tuple in half, and push it back onto the heap
   - Find the furthest row in the back with the max consecutive seats, fill in those rows first
   - even rows expand from the left
   - odd rows expand from the right
   - Assign seats for that specfic reservation id
   - Recalculate the max of number of consecutive seats open in that specific row we just used
