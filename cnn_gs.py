from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline

from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.utils import to_categorical


data = fetch_lfw_people(min_faces_per_person=70)

X = data.data
X = X / 255.
X = X.reshape(X.shape[0], 62, 47, 1)
y = to_categorical(data.target)

X_train, X_test, y_train, y_test = train_test_split(X,y)


def model_func(n1=30, s1=5, p1=2, n2=40, s2=4, p2=2, n3=30, n4=7):
    model = Sequential()
    model.add(Conv2D(n1, (s1, s1), input_shape=(62, 47, 1), activation='relu'))
    model.add(MaxPool2D((p1, p1)))
    model.add(Conv2D(n2, (s2, s2), activation='relu'))
    model.add(MaxPool2D((p2, p2)))
    model.add(Flatten())
    model.add(Dense(n3, activation='relu'))
    model.add(Dense(n4, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'], )

    return model

model = KerasClassifier(build_fn=model_func, epochs=15, verbose=1)

pipe = Pipeline([
    ('model', model)
])

params = {
    'model__epochs': [15, 20, 30],
    'model__n1': [30, 40, 50],
    'model__s1': [4,5,6],
    'model__p1': [1,2,3],
    'model__n2': [40,60,80],
    'model__s2': [3,4,5],
    'model__p2': [1,2,3],
    'model__n3': [15,30,50]
}

gs = GridSearchCV(pipe, param_grid=params)
gs.fit(X_train, y_train)

print('Train Score: ', gs.best_score_)
print('Best Param Dict: ', gs.best_params_)
print('Test Score: ', gs.score(X_test,y_test))