class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        longitud = len(s)
        acumulativo = 0
        for i in range(longitud):
            if i == longitud - 1:
                z = s[i]
                valor_actual = roman.get(z)
                acumulativo = acumulativo + valor_actual
            else:
                b = s[i]
                valor_actual = roman.get(b)

                c = s[i + 1]
                valor_siguiente = roman.get(c)

                if valor_actual < valor_siguiente:
                    acumulativo = acumulativo - valor_actual
                else:
                    acumulativo = acumulativo + valor_actual

        return acumulativo