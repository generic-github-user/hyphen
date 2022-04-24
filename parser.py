import string
sample = '1::10**4 $ !+(2:x^.5 ; !x%y) join\n'
sample2 = ''
sample3 = """
# levels of syntactic abstraction?
constants: null, Infinity

# more general form?
recrel

func range = a, b -> n in N | a <= n <= b
func range = a, b ->

func reduce =
func compose = f

# analogies?

func min = xx -> reduce(xx, a,b -> b<a?b:a)
func max = xx -> reduce(xx, a,b -> b<a?b:a)
# func invert

func sum = x -> reduce( '+)
func mean = x -> sum(x) / x.length

func abs

set(func) summary = (min, max, sum, mean)

# class string = (
#
# )

func for = a,b,c -> a; while(b, c)
"""
sample4 = """
x+y
"""
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
    '^': lambda a, b: a ^ b,
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '<=': lambda a, b: a <= b,
    '>=': lambda a, b: a >= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
}
