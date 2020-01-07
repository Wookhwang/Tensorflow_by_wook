import tensorflow as tf

'''
tensorflow 2.0 support eager execute.
Today I start printing string. but constant type is class.
So i use numpy function. this fuction allows you to print out immediately.
And then if you want to change 'bytes' type to 'str' type?
You just use decode('utf-8').

'''
tensor_a = tf.constant('hello world')

print(type(tensor_a))
print(type(tensor_a.numpy()))
print(type(tensor_a.numpy().decode('utf-8')))

'''
Easy Arithemetic example
(2 + 3) * 5 = ?
'''
tensor_b = tf.constant(100)
print(tensor_b.numpy())
print(type(tensor_b.numpy()))

tensor_c = tf.constant(2)
tensor_d = tf.constant(3)
tensor_e = tf.constant(5)

tensor_c.numpy()
tensor_d.numpy()
tensor_e.numpy()

#Use function
tensor_f = tf.add(tensor_c, tensor_d)
tensor_g = tf.multiply(tensor_f, tensor_e)
print(tensor_g.numpy())

#Use operator
tensor_f = tensor_c + tensor_d
tensor_g = tensor_f * tensor_e
print(tensor_g.numpy())

'''
Easy Matrix example
|1 2| => [[1,2],[3,4]]
|3 4|
'''
tensor_matrix_A =  tf.constant([[1,2],[3,4]])
tensor_matrix_B =  tf.constant([[2,0],[0,2]])

#Can't use operation in matrix.
tensor_matrix_C = tf.matmul(tensor_matrix_A, tensor_matrix_B)
print(tensor_matrix_C.numpy())
