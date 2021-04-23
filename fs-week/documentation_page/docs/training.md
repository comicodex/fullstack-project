In order to run the training script to classify as valid or not valid - ie "ants/bees" or "random", use:

```
python3 train_first_model.py --download-data
python3 train_first_model.py --train --epochs 2 --optmizer adam
```

When the training finishes, the best model weights will be saved to a file called `first_model.pth`.

---

In order to run the training script to classify the valid images as "bees" or "ants", use:

```
python3 train_second_model.py --download-data
python3 train_second_model.py --train --epochs 2 --optimizer adam
```

When the training finishes, the best model weights will be saved to a file called `second_model.pth`
