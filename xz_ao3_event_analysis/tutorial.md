#### class 5

~~~python
r = requests.get(url)
r.headers
r.text (string)
r.content (bytes)
r.headers
r.apparent_encoding

cookies
auth

~~~
http headers 字段charset对应返回encoding;
requests提供apparent_encoding猜测

#### class 6 - 9
- 六种异常
ConnectionError
HTTPError
URLRequired


requests.request(method, url, **kwargs)  
- 12 个kwargs:  
	verify
	cert
	stream
	allow_redirects
参考资料:
	你将使用 Pomegranate 库构建隐马尔可夫模型，并使用通用标签集进行词性标注。在使用更大型的标签集对实际文本语料库进行标注时，隐马尔可夫模型的准确率达到了 96% 以上。隐马尔可夫模型还用于语音识别和语音生成、机器翻译、生物信息学基因识别和计算机视觉人类手势识别等等。


