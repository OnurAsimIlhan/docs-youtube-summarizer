import streamlit as st
import validators
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

## creating streamlit app
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title('Langchain Summarizer')
st.subheader('Summmarize URL')

## Get groq key and url to summarize

with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

url=st.text_input("URL",label_visibility="collapsed")

prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}

"""
llm =ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please enter the groq api key and url to summarize")

    elif not validators.url(url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in url:
                    loader=YoutubeLoader.from_youtube_url(url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                ## Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.error(f"Exception:{e}")