### 安装Snowboy

```
git clone https://github.com/Kitt-AI/snowboy
```

```
python3 setup.py install
```

编译
```
cd swig/Python3
make 
cp _snowboydetect.so PYTHON_PATH
cp _snowboydetect.so /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/snowboy-1.2.0b1-py3.6.egg/snowboy
```

```
cp -r resources /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/snowboy-1.2.0b1-py3.6.egg/snowboy
```
