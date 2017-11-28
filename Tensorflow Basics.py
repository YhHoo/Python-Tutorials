import tensorflow as tf

# Perform the operation a=(b+c)*(c+2), lets say b=5, c=6 (known)

# Declare the operation that does Variable n Const initialization
const = tf.constant(2.0, name='const')
b = tf.Variable(5.0, name='b')
c = tf.Variable(6.0, name='c')

# Declare arithmetic operation
add1 = tf.add(b, c, name='add1')
add2 = tf.add(c, const, name='add2')
mult1 = tf.multiply(add1, add2, name='mult1')

# setup the variable initialization
init_op = tf.global_variables_initializer()

# start the session
with tf.Session() as sess:
    # initialize the variable
    sess.run(init_op)
    # compute the output of the graph
	# Note that mult1 is an operation, not a variable 
	# and therefore it can be run.
    mult1_out = sess.run(mult1)
    print("Variable a is {}".format(mult1_out))

# Output: Variable a is 88.0


# If the b variable is not fixed, or u want it to be a series of values
# use the tf.placeholder
### Replace the line 7 with:
b = tf.placeholder(tf.float32, [None, 1], name='b')
# the [None, 1] is a shape of the matrix, none means it can be 
# any no of rows 
### Replace the line 25 with:
mult1_out = sess.run(mult1, feed_dict={b: np.arange(0, 10)[:, np.newaxis]})
# this means, we now specify the value of the variable b we declared in
# the placeholder. We want it to be 0,1,...9, and we want it to be in the 
# matrix of any no of rows, bt only 1 unit for each row, so np.newaxis which 
# is also alias of None, will do the work.








