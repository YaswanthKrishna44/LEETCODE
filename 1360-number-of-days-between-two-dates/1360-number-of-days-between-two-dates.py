class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Helper to check for leap year
        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
        # Helper to convert a "YYYY-MM-DD" string to total days from year 1971
        def get_total_days(date_str: str) -> int:
            year = int(date_str[:4])
            month = int(date_str[5:7])
            day = int(date_str[8:])
            
            normal_year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            leap_year_days   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            total = 0
            # Add days for all full years passed since 1971
            for y in range(1971, year):
                total += 366 if is_leap(y) else 365
                
            # Add days for months in the current year
            current_months = leap_year_days if is_leap(year) else normal_year_days
            for m in range(month - 1):
                total += current_months[m]
                
            # Add days of the current month
            total += day
            return total
        
        return abs(get_total_days(date1) - get_total_days(date2))

        