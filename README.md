# Streamlit Cheatsheet

Streamlit is a Web Framework which is build for Data Scientist to readily convert their projects/analysis into a web application.

## Installation
To install streamlit run the following command at the prompt, after cloning this repo.

```shell
$ sudo pip3 install -r requirements.txt
```

```shell
$ streamlit run app.py
```

## Getting Started
```python3
# The well known alias

import streamlit as st
```

### altair_chart
```python3
# c is the altair chart object

st.altair_chart(c, use_container_width=True)
```

### area_chart
```python3
# chart_data is a pd.DataFrame object

st.area_chart(chart_data)
```

### audio
```python3
# audio_bytes is a BytesIO object

st.audio(audio_bytes, format='audio/ogg')
```

### checkbox
```python3
# data is a pd.DataFrame object

show_data = st.checkbox('Show Raw Data')

if show_data:
    st.write(data)
```

### selectbox
```python3
option = st.selectbox('Which Language do you know?', ('C', 'Python', 'Java'))

st.write('You Know:', option)
```
