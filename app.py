import streamlit as st
from streamlit_echarts import st_echarts

#Open CSS file
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#Testing to see if CSS applies to text
st.title("Custom Font Example")
st.write("Hi! This is an example text")

# Define ECharts options
options = {
    "textStyle": {
        "fontFamily": "Jost" #Doesn't work for me
    },
    "title": {
        "text": "Sample Chart",
        "left": "center",
    },
    "tooltip": {
        "trigger": "item",

    },
    "xAxis": {
        "type": "category",
        "data": ["A", "B", "C"],

    },
    "yAxis": {
        "type": "value",
    },
    "series": [{
        "type": "bar",
        "data": [120, 200, 150],
        "label": {
            "show": True,
        },
    }],
}

# Display the ECharts visualization
st_echarts(options=options, height="400px",renderer="svg")
