import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
	'1列目': [1,2,3,4],
	'2列目': [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))
# staticeなテーブル
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""

df2 = pd.DataFrame(
	np.random.rand(20, 3),
	columns=['a','b','c']
)

# 折れ線グラフ
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# マップのプロット
df3 = pd.DataFrame(
	np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
	columns=['lat','lon']
)

st.map(df3)

# # 画像表示
# st.write('Display Image')

# img = Image.open('sample.jpg')
# st.image(img, caption='sample', use_column_width=True)
