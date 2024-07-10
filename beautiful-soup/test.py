import requests
from bs4 import BeautifulSoup

url = "https://zenn.dev/cykinso/articles/e1566fd95641c3/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# クラス名が適切か確認するために、すべてのクラス名を表示
for tag in soup.find_all(True):
    if 'class' in tag.attrs:
        # print(tag.name, tag.attrs['class'])
        # print(tag.text)
        # test.txtに書き込む
        with open("test.txt", "a") as f:
            f.write(tag.name)
            f.write(tag.text)
            f.write("\n")
        # print("ttttt")

# 具体的なクラス名でフィルタリング
# target_tags = soup.find_all(class_=["p2"])
# for tag in target_tags:
#     print("sssss")
#     print(tag.text)
