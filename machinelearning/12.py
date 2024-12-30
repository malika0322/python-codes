# 12. Write a Python program that creates a TensorFlow tensor with a string data type and print 
# its value. 
import tensorflow as tf 
string_tensor = tf.constant("TensorFlow Exercises!", dtype=tf.string) 
print("String Tensor Value:", string_tensor.numpy().decode())
#output
''''''