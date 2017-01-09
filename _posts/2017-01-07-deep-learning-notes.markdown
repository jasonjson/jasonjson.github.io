---
layout: post
title: Deep Learning Notes
date: 2017-01-07 13:31
categories:
- A note
author: Jason
---
<p><strong><em>Deep learning notes</em></strong></p>

# Implementing neural network

## The delta Rule and learning Rates
* Convergence problem: if we pick a learning rate that’s too small, we risk taking too long during the training process. But if we pick a learning rate that’s too big, we’ll mostly likely start diverging away from the minimum.

## Gradient Descent with Sigmoidal Neurons
* The new modification rule is just like the delta rule, except with extra multiplicative terms included to account for the logistic component of the sigmoidal neuron.

## The back-propagation Algorithm
* The strategy will be one of dynamic programming. Once we have the error derivatives for one layer of hidden units, we’ll use them to compute the error derivatives for the activites of the layer below. And once we find the error derivatives for the activities of the hidden units, it’s quite easy to get the error derivatives for the weights leading into a hidden unit.

## Stochastic and Mini-Batch Gradient Descent
* The idea behind **batch gradient descent** is that we use our entire dataset to compute the error surface and then follow the gradient to take the path of steepest descent.
* Another potential approach is stochastic gradient descent, where at each iteration, our error surface is estimated only with respect to a single example. Instead of a single static error surface, our error surface is dynamic. As a result, descending on this stochastic surface significantly improves our ability to avoid local minima.
* In mini-batch gradient descent, at every iteration, we compute the error surface with respect to some subset of the total dataset (instead of just a single example). Mini-batches strike a balance between the efficiency of batch gradient descent and the local-minima avoidance afforded by stochastic gradient descent.

## Test Sets, Validation Sets, and Overfitting
* By building a very complex model, it’s quite easy to perfectly fit our dataset. But when we evaluate such a complex model on new data, it performs very poorly. In other words, the model does not generalize well. This is a phenomenon called overfitting, and it is one of the biggest challenges that a machine learning engineer must combat. 
* This leads to three major observations. First, the machine learning engineer is always working with a direct trade-off between overfitting and model complexity. Second, it is very misleading to evaluate a model using the data we used to train it. Third, it’s quite likely that while we’re training our data, there’s a point in time where instead of learning useful features, we start overfitting to the training set. 
* Let’s outline the workflow we use when building and training deep learning models. 
    1. First we define our problem rigorously.
    2. We need to build a neural network architecture to solve it.
    3. Finally, we’re ready to begin gradient descent.

## Preventing Overfitting in Deep Neural Networks
* One method of combatting overfitting is called *regularization*. Regularization modifies the objective function that we minimize by adding additional terms that penalize large weights.
    1. The most common type of regularization is *L2 regularization*. It can be implemented by augmenting the error function with the squared magnitude of all weights in the neural network.
    2. Another common type of regularization is *L1 regularization*. Neurons with L1 regularization end up using only a small subset of their most important inputs and become quite resistant to noise in the inputs. L1 regularization is very useful when you want to understand exactly which features are contributing to a decision.
    3. *Max norm constraints* have a similar goal of attempting to restrict  from becoming too large, but they do this more directly. Max norm constraints enforce an absolute upper bound on the magnitude of the incoming weight vector for every neuron and use projected gradient descent to enforce the constraint.
    4. *Dropout* is a very different kind of method for preventing overfitting that can often be used in lieu of other techniques. While training, dropout is implemented by only keeping a neuron active with some probability  (a hyperparameter), or setting it to zero otherwise. Intuitively, this forces the network to be accurate even in the absence of certain information.
