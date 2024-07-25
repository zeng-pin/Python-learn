class Instrument:
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('erhu')

class Piano(Instrument):
    def make_sound(self):
        print('piano')

class Violin(Instrument):
    def make_sound(self):
        print('violin')

def play(a):
    a.make_sound()

er=Erhu()
pi=Piano()
vi=Violin()
play(er)
play(vi)
play(pi)




