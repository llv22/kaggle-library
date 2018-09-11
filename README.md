# kaggle_library
imported library for kaggle to avoid duplicate code

## 1. How to build dist and wheel
* build wheel
```bash
python setup.py bdist_wheel
```
* build dist
```bash
python setup.py bdist
```

## 2. Library Summary

| Time      | Usage                |  Implementation          | Key Points                   |             Summary         |
|:---------:|:--------------------:|:------------------------:|:----------------------------:|:---------------------------:|
|2018-08-24 |Pyplot for Loss Analysis| kaggleml/plotlib.py    |  matplotlib library wrapper  | Refer from LiMu's [MXNet Gluon Guilde](https://github.com/mli/gluon-tutorials-zh/blob/master/chapter_deep-learning-basics/kaggle-house-price.md)  |

## Other Tips
1. Kaggle don't allow library name with '_' (underline): so refine kaggle_library to kaggle-library
2. How to import library and construct library
 
   * import guidline: https://www.kaggle.com/c/trackml-particle-identification/discussion/55753
   * library template github: https://github.com/LAL/trackml-library