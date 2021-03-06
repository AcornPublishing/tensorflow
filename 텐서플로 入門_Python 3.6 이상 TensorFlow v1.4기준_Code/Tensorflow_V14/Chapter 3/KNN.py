import numpy as np
import tensorflow as tf
import input_data
# Download input_data_old.py
# https://github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/examples/tutorials/mnist/input_data.py

#Build the Training Set

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

train_pixels,train_list_values = mnist.train.next_batch(100)
test_pixels,test_list_of_values  = mnist.test.next_batch(10)


train_pixel_tensor = tf.placeholder\
                     ("float", [None, 784])
test_pixel_tensor = tf.placeholder\
                     ("float", [784])

#Cost Function and distance optimization

distance = tf.reduce_sum\
           (tf.abs\
            (tf.add(train_pixel_tensor, \
                    tf.negative(test_pixel_tensor))), \
            reduction_indices=1)

pred = tf.argmin(distance, 0)

# Testing and algorithm evaluation

accuracy = 0.
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(len(test_list_of_values)):
        nn_index = sess.run(pred,\
		feed_dict={train_pixel_tensor:train_pixels,\
		test_pixel_tensor:test_pixels[i,:]})
        print("Test N:", i,"Predicted Class: ", \
		np.argmax(train_list_values[nn_index]),\
		"True Class: ", np.argmax(test_list_of_values[i]))
        if np.argmax(train_list_values[nn_index])\
		== np.argmax(test_list_of_values[i]):
            accuracy += 1./len(test_pixels)
    print("Result = ", accuracy)
