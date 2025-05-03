class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                    "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]

        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        def three_digit_to_words(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
            else:
                return below_20[n // 100] + " Hundred" + (
                    " " + three_digit_to_words(n % 100) if n % 100 != 0 else "")

        res = []
        for idx in range(len(thousands)):
            if num % 1000 != 0:
                chunk = three_digit_to_words(num % 1000)
                res.append(chunk + " " + thousands[idx] if thousands[idx] else chunk)
            num //= 1000

        return " ".join(reversed(res)).strip()
