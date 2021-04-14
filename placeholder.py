import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7], input2: [3]}))
