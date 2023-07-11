from frequencybyelement import *
from generateRandomList import *

data = generateData()

frequencies = FrequencyByElement(data, 'elements')
frequencies.set_fqcy()
frequencies.generateJson()