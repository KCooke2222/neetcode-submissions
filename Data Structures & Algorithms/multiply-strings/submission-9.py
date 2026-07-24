class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        if num1 == "0" or num2 == "0":
            return "0"


        def addRes(i, num):
            new = num + res[i]
            res[i] = new % 10
            carry = new // 10

            if carry: 
                addRes(i + 1, carry)


        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                offset = i + j
                mult = int(n1) * int(n2)

                while mult:
                    add = mult % 10

                    addRes(offset, add)

                    mult = mult // 10
                    offset += 1

        i = len(res) - 1
        while res[i] == 0:
            res.pop()
            i -= 1


        res = [str(i) for i in res[::-1]]
        return "".join(res)
