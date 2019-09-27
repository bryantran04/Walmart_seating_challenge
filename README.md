# Walmart_seating_challenge

<p>To use the script:<br>
/python3 seating.py <file_name> </p>

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
