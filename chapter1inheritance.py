# inheritance & logic gates
# what is the output value? 
# a powerful part of object-oriented programming is method that will use
# code that does not exist yet
class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

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

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.subsum = None
        self.subxor = None
        self.sumfinal = None
        self.carryfinal = None
        self.output = None

    def sum1(self):
        if self.a + self.b == 1:
            self.subxor = 1
        else:
            self.subxor = 0

        if self.subxor + self.c == 1:
            self.sumfinal = 1
        else:
            self.sumfinal = 0

    def carry(self):
        # A and B
        if self.a==1 and self.b==1:
            self.subsum = 1
        else:
            self.subsum = 0

        if self.subxor + self.subsum == 1:
            self.carryfinal = 1
        else:
            self.carryfinal = 0
        
    def return1(self):
        print('a:', self.a, 'b:', self.b, 'c:', self.c, 'subxor:', self.subxor, 'sumfinal:', self.sumfinal, 'carryfinal:', self.carryfinal )



def half_adder():
    print('this is a half adder')
    ha1 = HalfAdder('ha1')
    print(ha1.getOutput())

def full_adder():
    fa = FullAdder(1, 0, 0)
    fa.sum1()
    fa.carry()
    fa.return1()

full_adder()