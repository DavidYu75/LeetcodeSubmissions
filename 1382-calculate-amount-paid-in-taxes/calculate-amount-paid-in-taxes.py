class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # 3 * .5 = 1.5
        # (7 - 3) = 4 * .1 = 0.4
        # 12 - 7 = 3 * 0.25 = .75
        # 1.5 + 0.4 + 0.75 = 2.65
        total_tax = 0
        prev = 0

        for upper, percent in brackets:
            if income >= upper:
                total_tax += (upper - prev) * percent / 100
                prev = upper
            else:
                total_tax += (income - prev) * percent / 100
                return total_tax
        return total_tax