## Neural network

weights
- how input is multiplied
- modified in training

biases
- added to the product of weights and inputs to make sure neurons are passing something as output

weighted sum
- multiply each input by the corresponding weight, add the bias and sum all of these results up

activation function
- function applied to the weighted sum to transform output to a value that indicates whether neuron fires it's value
- ReLu
    - replace Sigmoid and TanH to solve vanishing gradient problem (values approaching 0)
- Softmax

TanH: inputs produce output between -1 and 1

Sigmoid: inputs produce output between 0 and 1

ReLu: inputs produce output between 0 and the input