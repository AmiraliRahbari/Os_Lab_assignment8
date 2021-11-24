class time(object):
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def __add__(self, other):
        s = self.second + other.second
        m = self.minute + other.minute
        h = self.hour + other.hour
        while s > 60:
            s -= 60
            m += 1
        while m > 60:
            m -= 60
            h += 1
        return time(h, m, s)

    def __sub__(self, other):
        s = self.second - other.second
        m = self.minute - other.minute
        h = self.hour - other.hour
        while s < 0:
            s += 60
        while m < 0:
            m += 60
        return time(h, m, s)

    def s_to_t(sec):

        h = sec // 3600
        sec = sec - h * 3600
        m = sec // 60
        s = sec - m * 60
        return time(h, m, s)

    def t_to_s(self):
        return (self.hour * 3600 + self.minute * 60 + self.second)


h = int(input("Enter hour time 1 : "))
m = int(input("Enter minute time 1 : "))
s = int(input("Enter second time 1 : "))
time1 = time(h, m, s)
print("time 1 : ", time1.hour, ':', time1.minute, ':', time1.second, end='')

h = int(input("\nEnter hour time 2 : "))
m = int(input("Enter minute time 2 : "))
s = int(input("Enter second time 2 : "))
time2 = time(h, m, s)
print("time 2 : ", time2.hour, ':', time2.minute, ':', time2.second, end='')
print('\nSum : ', (time1 + time2).hour, ':',
      (time1 + time2).minute, ':', (time1 + time2).second, end='')
print('\nSub : ', (time1 - time2).hour, ':',
      (time1 - time2).minute, ':', (time1 - time2).second, end='')
print('\ntime1 to seconds : ', time1.t_to_s(), end='')
s = int(input("\nEnter seconds for cinvert to time : "))
t = time.s_to_t(s)
print(s, 'to time : ', t.hour, ':',
      t.minute, ':', t.second, end='')
