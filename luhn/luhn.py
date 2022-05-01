"""Luhn
"""
import re
from typing import List


class Luhn:
    """Validate credit card number.

    """

    def __init__(self, card_num: str) -> None:
        self.card_num = card_num.replace(' ', '')[::-1]

    def valid(self) -> bool:
        """Card number is valid?

        :return: True if valid, false otherwise.
        """
        if len(self.card_num) <= 1:
            return False
        digit_sum: int = 0
        nums: List[str] = list(self.card_num)
        for i, char in enumerate(nums):
            if re.search(r'^\d$', char) is None:
                return False
            num = int(char)
            if i % 2 != 0:
                if num >= 5:
                    digit_sum += num * 2 - 9
                else:
                    digit_sum += num * 2
            else:
                digit_sum += int(char)
        return digit_sum % 10 == 0
