# inheritance & logic gates
# what is the output value? 
# a powerful part of object-oriented programming is method that will use
# code that does not exist yet

class LogicGate(object):

    def __init__(self):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    # common pattern for child classes: call parent init then add whatever other information child needs
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return(int(input("Enter Pin A input for gate"+ self.get_label()+"----->")))

    def get_pin_b(self):
        return(int(input("Enter Pin B input for gate"+ self.get_label()+"----->")))
    
class UnaryGate(LogicGate):

    def __init(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return(int(input("Enter Pin input for gate"+ self.get_label()+"------>")))