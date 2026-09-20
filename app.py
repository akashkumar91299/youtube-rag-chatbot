import streamlit as st

from src.rag_pipeline import YouTubeRAG
# Page Configuration

st.set_page_config(
    page_title="YouTube RAG Assistant",
    page_icon="🎥",
    layout="wide"
)
# Custom Title

st.title("🎥 YouTube RAG Assistant")

st.write(
    "Ask questions about any YouTube video "
)

# Session State

if "rag" not in st.session_state:
    st.session_state.rag = None

if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar

with st.sidebar:

    st.header("🎬 Video")

    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    load_video = st.button(
        "Load Video",
        use_container_width=True
    )

    if st.button(
        "Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

# Load Video

if load_video:

    if not youtube_url.strip():

        st.warning(
            "Please enter a YouTube URL."
        )

    else:

        with st.spinner(
            "Loading Video"
        ):

            try:

                rag = YouTubeRAG()

                video_data = rag.load_video( youtube_url )

                st.session_state.rag = rag
                st.session_state.video_loaded = True

                st.session_state.messages = []

                st.success(
                    f"Video loaded successfully! "
                    f"Created {len(video_data['chunks'])} chunks."
                )

            except Exception as e:

                st.error(
                    f"Error loading video: {str(e)}"
                )

# Status

if st.session_state.video_loaded:

    st.success(
        "✅ Video is ready. Ask your question below."
    )
else:
    st.info(
        "👈 Enter a YouTube URL and click  load video"    
    )

# Display Chat History

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# Chat Input

question = st.chat_input(
    "Ask something about the video..."
)
# Process Question
if question:
    if not st.session_state.video_loaded:
        st.warning(
            "Please load a YouTube video first."
        )
    else:
        # Display user question
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )
        with st.chat_message("user"):

            st.markdown(question)
        # Generate answer
        with st.chat_message("assistant"):
            
            with st.spinner("Thinking..."):
                
                try:
                    
                    result = (
                        st.session_state.rag
                        .ask(question)
                    )

                    answer = result["answer"]
                    sources = result["sources"]

                    st.markdown(answer)

                    # Sources

                    with st.expander(
                        "Retrieved Sources"
                    ):

                        for i, doc in enumerate(
                            sources,
                            start=1
                        ):

                            st.markdown(
                                f"**Source {i}**"
                            )

                            st.write(
                                doc.page_content
                            )

                            st.divider()

                    # Save assistant response

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    st.error(
                        f"Error generating answer: {str(e)}"
                    )