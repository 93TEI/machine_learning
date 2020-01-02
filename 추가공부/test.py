import tensorflow as tf
print(tf.__version__)

hello = tf.constant("Hello, Tensorflow") # 실제론 그래프에 위치하는 노드가 생성
#그래프는 session.run으로 실행가능
sess = tf.compat.v1.Session() #sess = tf.Session()

print(sess.run(hello))