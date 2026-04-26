import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv) 

base = communicator.stringToProxy("SimplePrinter:default -p 11000")

base2 = communicator.stringToProxy("SimpleCalculator:default -p 11000")

printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

calculator = Demo.CalculatorPrx.checkedCast(base2)
if not calculator: 
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
print(printer.sum(1, 10))
print(calculator.divisor(10, 2))

communicator.destroy()
