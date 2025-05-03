class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        order = ["", "Thousand", "Million", "Billion"]
        
        def chunk_to_words(chunk):
            words = []
            if chunk >= 100:
                words.append(ones[chunk // 100] + " Hundred")
                chunk %= 100
            if 10 <= chunk < 20:
                words.append(teens[chunk - 10])
            else:
                if chunk >= 20:
                    words.append(tens[chunk // 10])
                    chunk %= 10
                if chunk > 0:
                    words.append(ones[chunk])
            return ' '.join(words)

        
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        
        words = []
        for i in range(len(chunks)):
            if chunks[i] > 0:
                words.append(f"{chunk_to_words(chunks[i])} {order[i]}".strip())

        return ' '.join(reversed(words))