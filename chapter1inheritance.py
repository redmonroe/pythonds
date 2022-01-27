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
#Nand gate: work like AndGate except that were And returns 1, Nand return 0
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


def main():
#    g1 = AndGate("G1")
#    g2 = AndGate("G2")
#    g3 = OrGate("G3")
#    g4 = NotGate("G4")
#    c1 = Connector(g1,g3)
#    c2 = Connector(g2,g3)
#    c3 = Connector(g3,g4)
#    print(g4.getOutput())

#    g5 = NandGate("G5")
#    g6 = NorGate("G6")
   g7 = XorGate("G7")
   print(g7.getOutput())


def half_adder():
    print('this is a half adder')
    a = 1
    b = 0

    if a + b == 1:
        sum1 = 1
    else:
        sum1 = 0

    if sum1 == 0:
        carry = 1
    else:
        carry = 0

    assert sum1 == 1
    assert carry == 0
    # sum1 = XorGate("S1")
    # carry = AndGate("C1")
    # ha = Connector(sum1, carry)
    # print(carry.getOutput())
    # print(sum1.getOutput())
    # print(sum1)
    # print(ha)

half_adder()
# main()