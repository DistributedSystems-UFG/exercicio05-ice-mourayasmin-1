import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
    def sum(self, n1, n2, current=None):
        return n1+n2

class CalculatorI(Demo.Calculator):
    def divisor(self, n1, n2, current=None):
        return n1/n2

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, Ice.stringToIdentity("SimplePrinter"))

calc_object = CalculatorI()
adapter.add(calc_object, Ice.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()