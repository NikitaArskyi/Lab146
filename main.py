import copy
class Polynom:
    def __init__(self):
        self.__data = {}
    def _process_line(self, line):
        rec = line.split()
        if len(rec) > 0:
            assert len(rec) == 2
            try:
                pwr = int(rec[0])
            except:
                print("Some data in the file are incorrect. The wrong data were skipped.")
                return
            assert pwr >= 0
            try:
                coef = float(rec[1])
            except:
                print("Some data in the file are incorrect. The wrong data were skipped.")
                return
            assert pwr not in self.__data
            try:
                self.__data[pwr] = coef
            except:
                print("Some powers appeared more than once. The first value was taken.")
                return
        else:
            return

    def read_from_file(self, file_name):
        self.__data = {}
        with open(file_name) as f:
            for line in f:
                self._process_line( line.strip() )
    def read_from_keyboard(self):
        self.__data = {}
        print("Input powers & coefs, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line( s )

    def show(self):
        print(self.__data)

    def evaluate(self, x):
        result = 0
        for pwr, cf in self.__data.items():
            result += x**pwr * cf
        return result

    def get_coef(self, pwr):
        #return self._data.get(pwr, 0.0)
        if pwr in self.__data:
            return self.__data[pwr]
        else:
            return 0.0

    def set_coefs(self, coefs_dict):
        assert isinstance(coefs_dict, dict)
        self.__data = coefs_dict.copy()

    def get_powers(self):
        return self.__data.keys()

    @staticmethod
    def add(p1, p2):
        r = {}
        powers1 = p1.get_powers()
        powers2 = p2.get_powers()
        for pw in set(powers1) | set(powers2):
            cf = p1.get_coef(pw) + p2.get_coef(pw)
            r[pw] = cf
        rslt = Polynom()
        rslt.set_coefs(r)
        return rslt
    def subtract(p1, p2):
        r = {}
        powers1 = p1.get_powers()
        powers2 = p2.get_powers()
        for pw in set(powers1) | set(powers2):
            cf = p1.get_coef(pw) - p2.get_coef(pw)
            r[pw] = cf
        rslt = Polynom()
        rslt.set_coefs(r)
        return rslt
    def multiply(p1,p2):
        r = {}
        powers1 = p1.get_powers()
        powers2 = p2.get_powers()
        for pw in set(powers1) | set(powers2):
            cf=0
            for i in range(pw+1):
                cf+=p1.get_coef(i)*p2.get_coef(pw-i)
            r[pw]=cf
        rslt=Polynom()
        rslt.set_coefs(r)
        return rslt
P1 = Polynom()
P1.read_from_file('input01.txt')

P2 = Polynom()
P2.read_from_file('input02.txt')

sum = Polynom.add(P1, P2)
prod = Polynom.multiply(P1, P2)
diff = Polynom.subtract(P1,P2)
q = Polynom.add(diff,prod)
h=Polynom.multiply(P2,Polynom.multiply(diff,diff))
print("Please, insert a real number.")
while True:
    s = input()
    try:
        x = float(s)
        a=q.evaluate(x)
        b=h.evaluate(x)
        print(a)
        print(b)
        f=open("output.txt", "w")
        print(a, file=f)
        print(b,file=f)
        f.close()
        break
    except:
        print("Please, insert a real number!")
