import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import matplotlib.pyplot as plt
from keras import utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from keras.optimizers import Adam


for e in utils.image_dataset_from_directory('data', labels='inferred', label_mode='int', image_size=(300, 300)):
    x_train, y_train = e

x_train /= 255

number_of_classes = 2

y_train = utils.to_categorical(y_train, number_of_classes)

model = Sequential()
model.add(Conv2D(64, (16, 16), input_shape=(x_train.shape[1], x_train.shape[2], 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(64, (8, 8), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(number_of_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

his = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=80, batch_size=100)
model.save('er.keras')
plt.plot(his.history['loss'])
plt.plot(his.history['val_loss'])
plt.show()

plt.plot(his.history['accuracy'])
plt.plot(his.history['val_accuracy'])
plt.show()
