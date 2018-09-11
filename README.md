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
   ``` html
   oshua Bonatt (554th in this Competition) | 4 months ago | Reply
    I'm relatively new to Kaggle so figuring out anything was non-intuitive for me. I'm seeing this Topic just now, but for others who want explicit directions which I did not have:

    1. Click the [<] button at top-right of Kernel screen
    2. Click Settings
    3. Enter "LAL/trackml-library", e.g., into "GitHub user/repo" space at the bottom
    4. Click the (->) button to the left of that
    5. Restart Kernel by clicking the circular refresh/recycle-y button at the bottom-right of the screen, in the Console
    6. Custom libraries will now import when imported, as shown here by Wesam
   ```
   * library template github: https://github.com/LAL/trackml-library