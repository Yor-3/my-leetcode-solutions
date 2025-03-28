class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        # Make both versions equal length by appending "0" if necessary
        while len(v1) < len(v2):
            v1.append("0")
        while len(v2) < len(v1):
            v2.append("0")

        # Compare each revision
        for i in range(len(v1)):
            num1 = int(v1[i])
            num2 = int(v2[i])

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0