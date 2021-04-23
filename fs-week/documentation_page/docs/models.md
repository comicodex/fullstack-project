

## Model description

These models are binary classifiers. The first model is to ensure that a valid image is being input by the user. It will classify as valid or not valid. If valid, it will pass through to the second model where it will classify between **ants** and **bees**.
The training data includes 20 images of each class for training and 4 images of each class for validation #bigdata.

Jokes apart, this is done on purpose to make it easier to experiment. Once you feel confortable with your workflow, you can try with bigger datasets.
Remember to change the model if you need to!

## Remember to always start with good baselines

For example. In computer vision a resnet18 is a good starting point. In text classification an LSTM may be a good starting point.
