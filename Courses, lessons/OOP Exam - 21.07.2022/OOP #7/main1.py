from orange1 import Orange
from apple1 import Apple
from tangerine1 import Tangerine
from banana1 import Banana

orange = Orange('Verna', ['a', 'b1', 'c', 'b2'], 4.5, 'Orange')
apple = Apple('Antonovka', ['a', 'b2', 'c', 'd'], 2, 'Apple')
banana = Banana('Africa', ['b1', 'c', 'd', 'e'], 3.5, 'Apple', 24)
tangerine = Tangerine('Orangevie', ['b1', 'c2', 'c', 'd'],5, 'Tangerine')

apple.cut()
orange.clear()
banana.clear()