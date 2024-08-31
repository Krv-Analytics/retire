# Coal API

A lightweight pip installable package for pulling our coal dataset into ML applications.


## Ideas

* Can we use our analysis to define a predictive task? Maybe this incorporates textual data as well re KRAG in order to do real strategy matching?
* Idea is to just have a few files that pull a csv from our online version (that we can keep updated) and then format into standard formats for predictive tasks (scikit learn or pytorch).


## Imagined Usage

```
pip install krv-coal-api
```

```
import coalphaseout
from coalphaseout import feature_breakdown

# See whats in the data
print(feature_breakdown)

# Unsupervised
df = coalphaseout.pull_data(supervised=False)

# Documents
corpus = coalphaseout.pull_articles(minDate=2017)

# Supervised
X,y = coalphaseout.pull_data(supervised=True)
```
