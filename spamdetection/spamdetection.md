# Spam detection

## Text classification
- Spam messages are more likely to contain words and word combinations like 'free', 'free money' etc.

## Naïve Bayes

- Bayes theorem
- Naïve Bayes spam filtering    
    - p: propability
    - s: spam
    - ¬s: not spam
    - w: word
    - p(w|s): propability that a message containig word w is spam
    - p(s): propability that a message is spam to begin with

```
              p(w|s)p(s)
p(s|w)= -----------------------
        p(w|s)p(s)+p(w|¬s)p(¬s)
```

p(w|s)p(s): w in spam

p(w|¬s)p(¬s): w in not spam

All of the numbers can be defined from email data.

https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering

## Why 'naïve'?
```

p(s|w1,w2,w3...wn)= --------------------

```
Handling sequences and different combinations can be really hard to compute.

We should 'naïvely' assume that all the words are independent. Sho we can split it like this:
```

p(w1,w2,w3...wn|s) ->p(w1|s)p(w2|s)...p(wn|s) 

```

Pick the outcome that is most likely:
```
ŷ = argmax p(y)[p(w1|y)...p(wn|y)]
      y
                 n
                ___
  = argmax p(y) | | p(wi|y)
      y         i=1
```
Different naïve Bayes -algorithms use different ways to find value of `p(wi|y)`

## Numerical representation of text
"word embedding"
- word2vec
- tsne
- pca

### Onehot vector
Vector where there is only one "1".

```
 "dog" "cat" "fox" "bird"
[   0,   0,     0,   0  ]
[1,0,0,0] = vector representing "dog"
[0,1,0,0] = vector representing "cat"
[0,0,1,0] = vector representing "fox"
[0,0,0,1] = vector representing "bird"
```
Makes the vectors and matrices so sparse so it's easier to compute.

## Term frequency

Term frequency (tf): divide by total nr. of words. 

Long text has more word occurences. Term frequency helps to add a "scale" to word occurences.

## Inverse document frequency
Inverse document frequency (idf): some words occur more frequently than others

tf * idf = tfidf

Can be used in different algorithms.

https://en.wikipedia.org/wiki/Tf%E2%80%93idf

F.ex. a sum of multiple onehot vectors: 
```
|9| "dog"
|3| "cat"
|7| "fox"
|0| "bird"
```