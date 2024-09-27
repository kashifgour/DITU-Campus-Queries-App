import streamlit as st
from main import get_qa_chain, create_vector_db

# Add the DIT University logo at the top
st.image("https://upload.wikimedia.org/wikipedia/commons/2/2e/DIT_University_Dehradun_Logo.jpg", width=200)

# Title of the application
st.title("Campus Queries App")

# Sliding link for important notices
st.markdown(
    """
    <style>
    .slide-text {
        font-size: 20px;
        font-weight: bold;
        animation: slide 10s infinite linear;
        white-space: nowrap;
        overflow: hidden;
    }
    @keyframes slide {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    </style>
    <div class="slide-text">
        <a href="https://www.dituniversity.edu.in/happenings/important-notices" target="_blank" style="text-decoration:none;color:#ff4b4b;">
            Click here to see updated notices
        </a>
    </div>
    """, unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_option = st.sidebar.radio("Choose an option:", ["Ask a Question", "Create Knowledgebase"])

# Password for creating/updating the knowledgebase
knowledgebase_password = "ahmad@123"  # Replace this with a strong password

# Create Knowledgebase section
if selected_option == "Create Knowledgebase":
    st.header("Create Knowledgebase")

    # Password input for authentication
    password_input = st.text_input("Enter password to create/update knowledgebase:", type="password")
    if password_input == knowledgebase_password:
        btn = st.button("Create Knowledgebase")
        if btn:
            with st.spinner("Creating knowledgebase..."):
                create_vector_db()
                st.success("Knowledgebase created successfully!")
        st.write("Click the button above to create or update the knowledgebase.")
    else:
        st.error("You do not have permission to create/update the knowledgebase.")

# Ask a Question section
elif selected_option == "Ask a Question":
    st.header("Ask a Question")

    question = st.text_input("Type your question here:")

    # Frequently Asked Questions (FAQs)
    with st.expander("Some Frequently Asked Questions"):
        st.write("**1. How are the placement records at DIT University?**")
        st.write("**2. What is the fee structure for B.Tech CSE at DIT University?**")

    if question:
        with st.spinner("Getting the answer..."):
            chain = get_qa_chain()
            response = chain({"query": question})

            # Display the answer and source documents
            st.subheader("Answer")
            st.write(response["result"])

# Footer
st.markdown("""
    ---
    - Built by Kashif Ahmad
    - [GitHub](https://github.com/kashifgour)
    - [LinkedIn](https://www.linkedin.com/in/kashif-ahmad-548983220/)
""")