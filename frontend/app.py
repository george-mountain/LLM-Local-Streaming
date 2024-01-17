import requests
import streamlit as st

st.title("LocalGpt Streaming")
st.header("Ask anything ... 🤖")

chat_container = st.container()


def get_query():
    input_text = st.text_input("Ask any question...")
    return input_text


# retrieve the user input
user_input = get_query()

if user_input:
    st.write(user_input)
    with chat_container:
        url = f"http://backend:8000/query-stream/?query={user_input}"

        output_placeholder = st.empty()

        # Send a request to initiate streaming
        response = requests.get(url, stream=True)

        content = ""

        div_width = "700px"
        div_height = "700px"

        div_style = f"width: {div_width}; height: {div_height}; overflow: auto; border: 1px solid #ddd; padding: 10px;"

        # Iterate over the generator and update the content dynamically
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                content += chunk.decode("utf-8")

                output_placeholder.markdown(
                    f'<div style="{div_style}">{content}</div>', unsafe_allow_html=True
                )

        # Close the response stream
        response.close()
