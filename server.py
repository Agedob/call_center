class Call(object):
    def __init__(self, id, name, number , time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display_all(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason
        return self

class Call_Center(object):
    def __init__(self, calls):
        self.calls = []
        self.que = len(self.calls)

    def add(self,addme):
        self.calls.append(addme)
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def remove_num(self,num):
        for i in range(0, len(self.calls)):
            v = self.calls[i].number
            if v == num:
                self.calls.pop(i)
                print 'hi'
        return self

    def info(self):
        for i in self.calls:
            print i.id,
            print i.number,
            print i.name
        return self


call1 = Call( 1 , 'bob' , '916-666-2555', '12:00pm' , 'headache')
call2 = Call( 2 , 'bobby' , '916-255-6626', '11:00am' , 'headache')
call3 = Call( 3 , 'bill' , '916-255-8888', '7:00am' , 'backache')
callcent = Call_Center('')
callcent.add(call1)
callcent.add(call2)
callcent.add(call3)
callcent.remove_num('916-255-6626').info()
