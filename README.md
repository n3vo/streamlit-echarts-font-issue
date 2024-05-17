This is the github repository to a question in Streamlit forums
feel free to check out the post in the forum via the link below:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://discuss.streamlit.io/t/how-can-i-change-the-fontfamily-of-a-chart/69977)


# Introduction
Hello everyone! I'm working on a simple bar chart using streamlit-echarts and I'm having trouble changing the font. Despite my efforts, the chart doesn't seem to pick up the font specified in my CSS. Other Streamlit features like `st.write` apply the font correctly without any issues.
I set the renderer to 'svg' intentionally because I read that it is supposed to work better than 'canvas,' as explained in this [issue](https://github.com/apache/echarts/issues/11899#issuecomment-1809275017)

# Required Information
1. Are you running your app locally or is it deployed?
   
   **Locally**

2. Share the link to your app's public GitHub repository:
   
   **[Link To Repository](https://github.com/n3vo/streamlit-echarts-font-issue)**

3. Share the full text of the error message (not a screenshot):
 

<details>
     <summary>Click me</summary>

``` 
        GET https://cdn.segment.com/analytics.js/v1/iCkMy7ymtJ9qYzQRXkQpnAJEq7D4NyMU/analytics.min.js net::ERR_BLOCKED_BY_CLIENT
   actuallySendMetrics.e.load @ main.7e6f4f72.js:2
   (anonymous) @ main.7e6f4f72.js:2
   initialize @ main.7e6f4f72.js:2
   Cp.handleOneTimeInitialization @ main.7e6f4f72.js:2
   Cp.handleNewSession @ main.7e6f4f72.js:2
   newSession @ main.7e6f4f72.js:2
   (anonymous) @ main.7e6f4f72.js:2
   Cp.handleMessage @ main.7e6f4f72.js:2
   handleMessage @ main.7e6f4f72.js:2
   await in handleMessage (async)
   websocket.onmessage @ main.7e6f4f72.js:2
   
   main.7e6f4f72.js:2
   Unrecognized feature: 'ambient-light-sensor'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'battery'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'document-domain'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'layout-animations'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'legacy-image-formats'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'oversized-images'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'vr'.
   main.7e6f4f72.js:2
   Unrecognized feature: 'wake-lock'.
   index.html:1
   An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing.
 
   ```    
   </details>
   
4. Share the Streamlit and Python versions:
   - **Streamlit version: 1.34.0**
   - **Python version: 3.10.4**

Any insights on how to get the chart to recognize the font from the CSS would be greatly appreciated. Thanks in advance for your help!
