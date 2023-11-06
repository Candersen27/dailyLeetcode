"""

1845. Seat Reservation Manager

Design a system that managers the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

- SeatManager(int n) Initializes a seatManager object that will manage n seats numbered from 1 to n. All seats are initially available.

- int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.

- void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

Example 1:
    Input
        ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
    Output
        [null, 1, 2, null, 2, 3, 4, 5, null]

    Explanation
        SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
        seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
        seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
        seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
        seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
        seatManager.reserve();    // The only available seat is seat 5, so return 5.
        seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

    constraints:
        1 <= n <= 10^5
        1 <= seatNumber <= n
        For each call to reserve, it is guaranteed that there will be at least one unreserved seat
        For each call to unreserve, it is guaranteed that seatNumber will be reserved.
        At most 10^5 calls in total will be made to reserve and unreserve.
"""


class SeatManager:

    
    def __init__(self, n) :
        # Create the seats array, if a seat is occupied it will contain true, if not, false.  initially all the seats are vacant.
        self.seats = [False] * n
        

    def reserve(self):
        # Use binary search to find an empty seat.
        left = 0
        right = len(self.seats) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check to see if the seat is vacant
            if not self.seats[mid]:
                # if we're in the first seat or if the seat to the left is occupied, then this must be the first vacant seat available.
                if mid == 0 or self.seats[mid - 1]:
                    self.seats[mid] = True
                    return mid + 1
                
                # Redefine the right bound and reenter the loop
                else:
                    right = mid - 1
                    
            # Redefine the left bound and reenter the loop
            else:
                left = mid + 1




    def unreserve(self, seatNumber):
        
        self.seats[seatNumber - 1] = False






def main_function():
    variable = 5

    def helper_function(some_variable):
        # Manipulate the passed variable
        variable = some_variable
