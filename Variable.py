	
import tensorflow.compat.v1 as tf
	
tf.compat.v1.disable_eager_execution()
state = tf.Variable(4,name='count')
print(state.name)
one = tf.constant(2)

new_value= tf.add(state,one)
update = tf.assign(state,new_value)

init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
