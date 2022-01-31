# inheritance & logic gates
# what is the output value? 
# a powerful part of object-oriented programming is method that will use
# code that does not exist ye

class LogicGate:

    def __init__(self, name):
        self.name = name
        self.output = None

    def get_name(self):
        return self.name
    
    def get_output(self):
        self.output = self.run_gate_function()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.a = None
        self.b = None

    def binary_quickset(self, a, b):
        self.a = a
        self.b = b


    def get_a(self):
        if self.a == None:
            return int(input("Enter Pin A input for gate " + self.get_name() + ':'))
        # if gate has received logic from another pin, don't prompt user, instead use following flow
        else:
            return self.a

    def get_b(self):
        if self.a == None:
            return int(input("Enter Pin B input for gate "+self.get_name()+ ":"))
        else:
            return self.b
'''

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
'''
class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def run_gate_function(self):

        a = self.get_a()
        b = self.get_b()
        if a==1 and b==1:
            return 1
        else:
            return 0

def understand_and():
    ag = AndGate('first')
    ag.binary_quickset(1, 1)
    print(ag)



understand_and()
'''

class NandGate(AndGate):
    # functionality does not require a new __init__ method
    def performGateLogic(self):
        if super().performGateLogic() == 1: # call performGateLogic in the parent
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

#Nor gate: works like OrGate except that were OrGate returns 0, NorGate returns a 1
class XorGate(OrGate):
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a + b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
'''

'''
class HalfAdder(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a + b == 1:
            sum1 = 1
        else:
            sum1 = 0

        if sum1 == 0:
            carry = 1
        else:
            carry = 0

        print('sum:', sum1, 'carry:', carry)
        return sum1, carry

class FullAdder(BinaryGate):

    def __init__(self, input_list=None):
        self.a = input_list[0]
        self.b = input_list[1]
        self.c = input_list[2] 
        self.subsum = None
        self.subxor = None
        self.sumfinal = None
        self.carryfinal = None
        self.output = None
        # self.carryterm_left = None
        self.carry_middle = None
        self.carryterm_right = None

    def assert_block(self):
        assert self.a == 1
        assert self.b == 0
        assert self.c == 0
        assert self.subxor == 1
        assert self.sumfinal == 1
        assert self.carryfinal == 0

    def sum1(self):
        # C xor (A xor B)
        # (A xor B)
        if self.a + self.b == 1:
            self.subxor = 1
        else:
            self.subxor = 0

        # C xor (A xor B)
        if self.subxor + self.c == 1:
            self.sumfinal = 1
        else:
            self.sumfinal = 0

    def carry(self):

        if self.b == 1 or self.c == 1:
            self.carry_middle = 1
        else:
            self.carry_middle = 0

        if self.a == 1 or self.b == 1:
            self.carryterm_left = 1
        else:
            self.carryterm_left = 0

        if self.a == 1 or self.c == 1:
            self.carryterm_right = 1
        else:
            self.carryterm_right = 0

        if self.carryterm_left == 1 & self.carry_middle == 1 & self.carryterm_right == 1:
            print('hi')
            self.carryfinal = 1
        else:
            self.carryfinal = 0

        
    def return1(self):
        print('a:', self.a, 'b:', self.b, 'c:', self.c, 'subxor:', self.subxor, '|', 'sumfinal:', self.sumfinal, 'carryfinal:', self.carryfinal )



def half_adder():
    print('this is a half adder')
    ha1 = HalfAdder('ha1')
    print(ha1.getOutput())

def full_adder(testing=False):
    input_list = [1, 1, 0]
    if testing:
        input_list = [1, 0, 0]
    fa = FullAdder(input_list=input_list)
    fa.sum1()
    fa.carry()
    fa.return1()
    if testing:
        fa.assert_block()

full_adder(testing=False)
'''