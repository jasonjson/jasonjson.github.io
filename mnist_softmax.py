from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

LEARNING_RATE = 0.5
TRAINING_EPOCHS = 10000
BATCH_SIZE = 100
DISPLAY_STEP = 1000
FLAGS = None

def layer(input, weight_shape, bias_shape):

    weigth_stddev = (2.0 / weight_shape[0]) ** 0.5
    weight_init = tf.random_normal_initializer(stddev=weigth_stddev)
    bias_init = tf.constant_initializer(value=0)
    W = tf.get_variable("W", weight_shape, initializer=weight_init)
    b = tf.get_variable("b", bias_shape, initializer=bias_init)
    return tf.nn.relu(tf.matmul(input, W) + b)

def inference(x):

    with tf.variable_scope('hidden_1'):
        hidden_1 = layer(x, [784, 256], [256])
    with tf.variable_scope('hidden_2'):
        hidden_2 = layer(hidden_1, [256, 256], [256])
    with tf.variable_scope('output'):
        y = layer(hidden_2, [256, 10], [10])
    return y

def training(y, y_):

    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))
    return tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cross_entropy)

def evaluation(y, y_):

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

def main(_):

    # load mnist train/test/validation data
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    x = tf.placeholder(tf.float32, [None, 784])
    y_ = tf.placeholder(tf.float32, [None, 10])
    # calculate logit
    y = inference(x)
    # training operation
    train_op = training(y, y_)
    # evaluation operation
    eval_op = evaluation(y, y_)

    # start a session
    sess = tf.InteractiveSession()
    tf.initialize_all_variables().run()
    # start training
    for epoch in range(TRAINING_EPOCHS):
        batch_xs, batch_ys = mnist.train.next_batch(BATCH_SIZE)
        sess.run(train_op, feed_dict={x: batch_xs, y_: batch_ys})
        if epoch % DISPLAY_STEP == 0:
            print("Accuracy after {0}'s epoch".format(epoch))
            print(sess.run(eval_op, feed_dict={x:mnist.validation.images, y_:mnist.validation.labels}))
    # compare with test data
    print("Test accuracy")
    print(sess.run(eval_op, feed_dict={x:mnist.test.images, y_:mnist.test.labels}))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default="/home/yliu903/mbig/automation/tensorflow/mnist/input_data")
    FLAGS = parser.parse_args()
    tf.app.run()
