


class a:
    def f1(self):
        print('In a f1')



class b(a):
    def f2(self):
        print('In b f2')


class c(b):
    def f3(self):
        print('In c f3')
        super().f2()


obj1=c()

obj1.f1()
obj1.f2()
obj1.f3()
