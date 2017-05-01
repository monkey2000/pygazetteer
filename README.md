# pygazetteer
Location extractor by looking up gazetteer naïvely

```shell
pip install pygazetteer
```

## Usage

`pygazetteer` provides an embedded gazetteer for English and Chinese.

```python3
from pygazetteer import Gazetteer
g = Gazetteer()
g.print()

print(a.match('诶，连任也要按照香港的法律啊，对不对？要要……要按照香港的……当然我们的决定权也是很重要的。香港的特区……特别行政区是属于中国……人民共和（中华人民共和国）的中央人民政府啊。啊？到那个时候我们会表态的！'))
print(a.match('U.S. President Donald Trump’s warm words for Chinese President Xi Jinping as a “good man” will reassure Beijing that he finally understands the importance of good ties but risk leaving America’s allies in the region puzzling over where they fit into the new order.'))
```

It will return things like:

```python3
{'1819730': (('1819730', '2', '1814991', 'Hong Kong', '香港', 'Hong Kong Special Administrative Region'), 3), '1814991': (('1814991', '1', '0', 'China', '中国', "People's Republic of China", '中华人民共和国', '中華人民共和國', 'People’s Republic of China'), 2)}
{'6252001': (('6252001', '1', '0', 'United States', '美国', 'America', 'United States of America'), 1), '2038349': (('2038349', '2', '1814991', '北京市', '北京', 'Beijing Municipality', 'Beijing'), 1)}
```

which follows a pattern:

```
{'geoname_id', (raw_data_from_gazetteer, mentioned_times)}
```

To assign an external dictionary:

```python3
g = Gazetteer(path_to_your_gazetteer)
```

