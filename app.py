import streamlit as st
from langchain_community.llms import CTransformers

# Function to generate a blog response using LLama
def generate_blog_response(input_topic, word_count, target_audience):
    # Initialize LLama model
    llama_model = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                                model_type='llama',
                                config={'max_new_tokens': 256,
                                        'temperature': 0.01})
    
    # Define prompt template
    template = '''
        Write a blog for {target_audience} job profile for the topic {input_topic}
        within {word_count} words.
            '''
    prompt = template.format(target_audience=target_audience, input_topic=input_topic, word_count=word_count)
    
    # Generate response
    response = llama_model(prompt)
    
    return response

# Set Streamlit page configuration
st.set_page_config(page_title="Blog Generator",
                   page_icon='👩‍🚀', 
                   layout='centered',
                   initial_sidebar_state='collapsed')

# Main title
st.header("Generate Blogs 👩‍🚀")

# Input fields
input_topic = st.text_input("Enter the Blog Topic")
word_count = st.text_input('Desired Word Count')
target_audience = st.selectbox('Writing the Blog For', ('Researchers', 'Applied Scientist', 'All People'), index=0)

# Button to trigger blog generation
submit_button = st.button("Generate")

# Generate and display blog response upon button click
if submit_button:
    blog_response = generate_blog_response(input_topic, word_count, target_audience)
    st.write(blog_response)
