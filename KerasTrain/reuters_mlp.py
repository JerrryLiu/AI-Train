#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:Jerry Liu
@file: reuters_mlp.py 
@version:
@time: 2018/12/25 
@email:liudongbing8@163.com
@function： https://github.com/keras-team/keras/blob/master/examples/reuters_mlp.py

        路透社新闻专题主题分类任务中训练和评估一个简单的MLP
"""

import numpy as np
import keras
from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
from keras.preprocessing.text import Tokenizer

max_words = 1000
batch_size = 32
epochs = 5

print("Loading data...")
(x_train,y_train),(x_test,y_test) = reuters.load_data(num_words=max_words,test_split=0.2)

print(len(x_train),"train sequences")
print(len(x_test),"test sequences ")

num_classes = np.max(y_train)+1

print(num_classes,"classes")

# tokenizer 标签生成器 sequences 序列
print("Vectorizing sequence data ...")
tokenizer = Tokenizer(num_words=max_words)
x_train = tokenizer.sequences_to_matrix(x_train,mode="binary")
x_test = tokenizer.sequences_to_matrix(x_test,mode="binary")

print("x_train shape:",x_train.shape)
print("x_test shape:",x_test.shape)

print("Covert class vector to binary class matrix""(for use with categorical)")

# to_categorical 1,2,3,4 转换为[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)
print("y_train shape:",y_train.shape)
print("y_test shape:",y_test.shape)

print("Building Model...")
model = Sequential()
model.add(Dense(512,input_shape=(max_words,)))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])


history = model.fit(x_train,y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_split=0.1)


print("*********************")
score = model.evaluate(x_test,y_test,
                       batch_size=batch_size,verbose=1)

print("Test score:",score[0])
print("Test accuracy:",score[1])



