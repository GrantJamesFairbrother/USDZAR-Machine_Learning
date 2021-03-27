import numpy as np
test = [[0.96529057],
        [0.98689497],
        [0.9651579],
        [0.09324097],
        [0.09540782],
        [0.10177571]]

test2 = [[1],
         [2],
         [3],
         [4],
         [5],
         [6]]

#print(test[0:3, :])

train_data = np.array(test2)

print(test2)

x_train = []
y_train = []

for i in range(2, len(train_data)):
    x_train.append(train_data[i-2:i, 0])
    y_train.append(train_data[i, 0])

    print(x_train)
    print(y_train)

print(type(x_train))

x_train = np.array(x_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

print(x_train[0])
