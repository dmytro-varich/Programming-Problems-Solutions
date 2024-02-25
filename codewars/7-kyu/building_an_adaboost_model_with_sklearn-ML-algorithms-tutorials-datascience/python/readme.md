Hi there! Welcome to "Building an Adaboost model with Sklearn (Introductory Machine Learning)".

If you get stuck at any point I **strongly recommend** you read the relevant documentation: [http://scikit-learn.org/stable/index.html](http://scikit-learn.org/stable/index.html)

This kata can be broken up into the following steps:
1. Import the relevant sklearn libraries (i.e. AdaBoostClassifier, train_test_split)
2. Create the "train_ada_boost" function (more details below)
3. Split the data (X) into a test set and a training set (you **MUST USE** sklearns train_test_split for this)
4. **TRAIN** an adaBoostClassfier (Once again, you **MUST USE** sklearn for this).
5. Your "train_ada_boost" function **must return a three element tuple** (more details below).

The "train_ada_boost" function accepts the following arguments:
- X -- This would normally be a dataset (but in this kata it is a 1D numpy array)
- Target -- This is a 1D numpy array consisting of 1's and 0's. This argument is the set of values we are trying to predict with our model
- estimators -- **KEYWORD ARGUMENT** if no argument is passed in the default value should be set to **3**.
- random_seed -- **KEYWORD ARGUMENT** if no argument is passed in the default value should be set to **0**.

Your function should return a 3 element tuple consisting of the following values **in this exact order**:
- A **TRAINED** AdaBoostClassifer (return the actual model)
- A test set (1D numpy array, which was built by sklearns test_train_split function)
- A target array (1D numpy array, which was built by sklearns test_train_split function))

Details:
- Your model should be trained using the specified number of estimators, with a random state equal to seed.
- When splitting the data, be sure to set the random state equal to seed.
- ALL other parameters not mentioned here for both 'test_train_split' and 'AdaBoost' should be set to default values.
- Even though you are handling Numpy arrays there is no need to actually manipulate the arrays yourself (let sklearn to it for you!).

Good Luck!

> Note, in actual machine learning it is highly unlikely we would ever use AdaBoost with such a small number of estimators. However building models can be very time consuming and codewars.com has a 5000ms timeout.
