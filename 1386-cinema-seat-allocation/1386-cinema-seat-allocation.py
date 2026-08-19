from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map row -> bitmask of reserved seats (1-indexed mapping to bit positions)
        seats = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                seats[row] |= (1 << (seat - 2))
        
        # Max families for completely unreserved rows
        max_families = (n - len(seats)) * 2
        
        # Masks for seat groups:
        # Left:   seats 2,3,4,5 -> bits 0,1,2,3 -> 0b00001111 (15)
        # Right:  seats 6,7,8,9 -> bits 4,5,6,7 -> 0b11110000 (240)
        # Middle: seats 4,5,6,7 -> bits 2,3,4,5 -> 0b00111100 (60)
        LEFT, RIGHT, MIDDLE = 15, 240, 60
        
        for mask in seats.values():
            left_ok = (mask & LEFT) == 0
            right_ok = (mask & RIGHT) == 0
            
            if left_ok and right_ok:
                max_families += 2
            elif left_ok or right_ok or ((mask & MIDDLE) == 0):
                max_families += 1
                
        return max_families