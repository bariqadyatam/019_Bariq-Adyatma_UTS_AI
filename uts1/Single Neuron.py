#Bariq Adyatma
#2109139019
#single neuron

#mengimport library numpy dan memberi inisial
import numpy as np

#layer input 10 features
inputs = [2.5, 3.5, 1.0, 3.0, 2.5, 3.0, 1.5, 2.0, 2.2, 3.0]

#neuron 1
weights = [[0.2, 0.5, 0.1, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7],]

#bias dari layer
biases = [2.0, 3.0, 1.0, 1.5, 2.5]

#menghitung output
layer_outputs = np.dot(weights, inputs) + biases

#memunculkan output
print(layer_outputs)