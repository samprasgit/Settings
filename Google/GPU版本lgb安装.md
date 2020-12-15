```shell
!git clone https://github.com/Microsoft/LightGBM

%cd LightGBM/
!mkdir build
!cmake -DUSE_GPU=1 #avoid ..
!make -j$(nproc)

!sudo apt-get -y install python-pip

!sudo -H pip install setuptools pandas numpy scipy scikit-learn -U

%cd LightGBM/python-package
!sudo python setup.py install


```



```python
params = {
 ‘boosting_type’: ‘gbdt’,
 ‘objective’: ‘regression’,
 ‘device_type’:’gpu’,
 ‘metric’: {‘l2’, ‘l1’},
 ‘num_leaves’: 31,
 ‘learning_rate’: 0.05,
 ‘feature_fraction’: 0.9,
 ‘bagging_fraction’: 0.8,
 ‘bagging_freq’: 5,
 ‘verbose’: 0
}


```

Cmake升级

```shell
!pip install cmake -U
```



## 参考

- https://blog.csdn.net/linyuanthocr/article/details/106440487