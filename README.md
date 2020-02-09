# webdriver-detection-bypassing
Bypass webdriver detection using pyppeteer(python3.7)



## Usage

python3.7

```
pip3 install pyppeeteer
python3 bypass.py
```



## How

If you just visit https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html with headless chrome, you will be detected. This page shows the principles that most pages are using to detect your webdriver.



Here I refer https://github.com/intoli/intoli-article-materials/tree/4bec59bd3f936d729340fefadb5b4f144bc70658/articles/not-possible-to-block-chrome-headless and modify it to python version.



And If you want to bypass the webdriver detection, you can just do what I show in `bypass.py`. By doing this, you can use webdriver to visit almost every page that your chrome can visit.

