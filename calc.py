import math

class Calc:
    def __init__(self, nbone, nbtwo):
        self.nbone = nbone
        self.nbtwo = nbtwo

    def add(self, nbone, nbtwo):
        self.nbone = nbone
        self.nbtwo = nbtwo
        result = float(self.nbone) + float(self.nbtwo)
        return round(result,3)

    def less(self, nbone, nbtwo):
        self.nbone = nbone
        self.nbtwo = nbtwo
        result = float(self.nbone) - float(self.nbtwo)
        return round(result,3)

    def mult(self, nbone, nbtwo):
        self.nbone = nbone
        self.nbtwo = nbtwo
        result = float(self.nbone) * float(self.nbtwo)
        return round(result,3)

    def div(self, nbone, nbtwo):
        self.nbone = nbone
        self.nbtwo = nbtwo
        if self.nbtwo == 0:
            result = "Impossible"
            return result
        else:
            result = float(self.nbone) / float(self.nbtwo)
        return round(result,3)

    def cosi(self, nbtwo):
        self.nbtwo = float(nbtwo)
        self.nbtwo = math.radians(self.nbtwo)
        result = math.cos(self.nbtwo)
        return round(result,3)

    def sinu(self, nbtwo):
        self.nbtwo = float(nbtwo)
        print(self.nbtwo)
        self.nbtwo = math.radians(self.nbtwo)
        print(self.nbtwo)
        result = math.sin(self.nbtwo)
        print("result :", result)
        return round(result,3)

    def tang(self, nbtwo):
        self.nbtwo = float(nbtwo)
        self.nbtwo = math.radians(self.nbtwo)
        result = math.tan(self.nbtwo)
        return round(result,3)

    def expo(self, nbtwo):
        self.nbtwo = float(nbtwo)
        result = math.exp(self.nbtwo)
        return round(result,3)

    def loga(self, nbtwo):
        self.nbtwo = float(nbtwo)
        if self.nbtwo <= 0:
            result = "Impossible"
            return result
        else:
            result = math.log10(self.nbtwo)
            return round(result,3)

    def logn(self, nbtwo):
        self.nbtwo = float(nbtwo)
        if self.nbtwo <= 0:
            result = "Impossible"
            return result
        else:
            result = math.log(self.nbtwo)
            return round(result,3)

    def modu(self, nbone, nbtwo):
            self.nbone = float(nbone)
            self.nbtwo = float(nbtwo)
            result = self.nbone % self.nbtwo
            return round(result, 3)

    def powa(self, nbone, nbtwo):
        self.nbone = float(nbone)
        self.nbtwo = float(nbtwo)
        result = math.pow(self.nbone, self.nbtwo)
        return round(result,3)

    def my_sqrt(self, nbtwo):
            self.nbtwo = float(nbtwo)
            result = math.sqrt(self.nbtwo)
            return round(result, 3)
