import sys
import os

# get name of current directory
current = os.path.dirname(os.path.realpath(__file__))

# get parent directory
parent = os.path.dirname(current)

sys.path.append(parent)

from chapter1inheritance import LogicGate, BinaryGate, AndGate

class TestLogicGate:
    def func(self, x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4

    def test_lg_init(self):
        lg = LogicGate('test_LG')
        assert lg.name == 'test_LG'
        assert lg.output == None

class TestBinaryGate:
    def test_binary_init(self):
        bg = BinaryGate('test_BG')
        assert bg.name == 'test_BG'
        assert bg.a == None
        assert bg.b == None

    def test_binary_user_input(self, monkeypatch):
        bb = BinaryGate('test_BB')
         # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        monkeypatch.setattr('builtins.input', lambda _: 1)

        # go about using input() like you normally would:
        i = input("Enter Pin A input for gate " + bb.get_name() + ':')
        assert i == 1
        assert bb.get_a() == 1

class TestAndGate:
    def test_and_init(self):
        ag = AndGate('test_AND')
        assert ag.name == ('test_AND')

    def test_rgf(self):
        ag = AndGate('test_AND')
        ag.binary_quickset(1, 0)
        assert ag.run_gate_function() == 0
