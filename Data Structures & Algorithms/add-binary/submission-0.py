class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # binary addition using string iteration and carry
        
        res = [0] * max(len(a), len(b))

        a = list(a)
        b = list(b)

        carry = 0
        i =  max(len(a), len(b)) - 1
        while a or b:
            # will expand the binary form to same len
            aNext = 0 if not a else int(a.pop())
            bNext = 0 if not b else int(b.pop())

            if aNext == 1 and bNext == 1:
                res[i] = carry
                carry = 1
            elif (aNext == 1) ^ (bNext == 1):
                res[i] = 1 if carry == 0 else 0
                carry = 0 if carry == 0 else 1
            else:
                res[i] = carry
                carry = 0

            i -= 1

        carry = '' if carry == 0 else carry
        return "".join(map(str, [carry] + res))
