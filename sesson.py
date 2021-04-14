import tensorflow as tf
tf.compat.v1.disable_eager_execution()
matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [3]])
product = tf.matmul(matrix1, matrix2)  # matrix multiply np.dot(m1, m2)

# method 1
sess = tf.compat.v1.Session()
result = sess.run(product)
print(result)
sess.close()
