import streamlit as st
from PIL import Image

def show_primary_sector():
    st.title("Primary Sector")
    if st.button("Go to Home"):
        st.session_state.page = "home"
        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.user_answers = []
        st.session_state.correct_answers_list = []
        st.experimental_rerun()
    
    st.write(
        """- Involves the extraction and harvesting of natural resources.
- Includes activities such as agriculture, mining, fishing, and forestry.
- It’s about raw materials and resources.
- The primary sector is called 'primary' because it is the first sector that must be established in order for a country to begin to industrialise.
- It provides the foundation for all other economic activity.
- India is the largest employer of the Primary Sector."""
    )
    # st.image("Images/Primary.jpg")  # Replace with your image path
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_primary"
        st.experimental_rerun()

def show_secondary_sector():
    st.title("Secondary Sector")
    if st.button("Go to Home"):
        st.session_state.page = "home"
        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.user_answers = []
        st.session_state.correct_answers_list = []
        st.experimental_rerun()
    
    st.write(
        """- Focuses on manufacturing and industry.
- Involves transforming raw materials from the primary sector into finished products.
- Examples include automobile manufacturing, construction, and food processing.
- It is also called the Industrial Sector."""
    )
    # st.image("Images/Secondary.jpg")  # Replace with your image path
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_secondary"
        st.experimental_rerun()

def show_tertiary_sector():
    st.title("Tertiary Sector")
    if st.button("Go to Home"):
        st.session_state.page = "home"
        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.user_answers = []
        st.session_state.correct_answers_list = []
        st.experimental_rerun()
    
    st.write(
        """- Provides services rather than goods.
- Includes retail, entertainment, healthcare, education, and financial services.
- The emphasis here is on providing services to consumers and businesses.
- Services are also called "intangible goods"."""
    )
    # st.image("Images/Tertiary.jpg")  # Replace with your image path
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_tertiary"
        st.experimental_rerun()

def show_quiz(sector):
    st.title(f"{sector.capitalize()} Sector Quiz")
    if st.button("Go to Home"):
        st.session_state.page = "home"
        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.user_answers = []
        st.session_state.correct_answers_list = []
        st.experimental_rerun()
    
    questions = {
        "primary": [
            ("Primary Sector mainly consists of?", ["Artificial resources", "Technology", "Natural resources"], "Natural resources"),
            ("Primary Sector of economy is related to______?", ["Agriculture", "Information technology", "Transportation"], "Agriculture"),
            ("In which of the following countries is Primary Sector prominent?", ["Japan", "India", "United States"], "India"),
            ("The _______ continues to be the largest employer in India.", ["Secondary sector", "tertiary sector", "Primary sector"], "Primary sector")
        ],
        "secondary": [
            ("What does Secondary Sector mainly focus on?", ["Extraction", "Manufacturing", "Service"], "Manufacturing"),
            ("It comes after which sector of the economy?", ["Primary", "Quaternary", "Tertiary"], "Primary"),
            ("Secondary sector mainly involves?", ["Automobile manufacturing", "Services of a doctor", "Mining"], "Automobile manufacturing"),
            ("Secondary sector is also known as?", ["Service sector", "Natural sector", "Industrial sector"], "Industrial sector")
        ],
        "tertiary": [
            ("What does Tertiary Sector provide?", ["Natural Resources", "Services", "Goods"], "Services"),
            ("Which of the following is not included in Tertiary Sector?", ["Manufacturing", "Entertainment", "Retail"], "Manufacturing"),
            ("Tertiary Sector emphasises on services provided by", ["Business to Business", "Business to Consumers", "Consumers to Business"], "Business to Consumers"),
            ("Services are also known as?", ["Service Goods", "Manufacturing Goods", "Intangible Goods"], "Intangible Goods")
        ]
    }
    
    question_index = st.session_state.get('question_index', 0)
    user_answers = st.session_state.get('user_answers', [])
    correct_answers_list = st.session_state.get('correct_answers_list', [])
    
    if question_index < len(questions[sector]):
        question, options, correct_answer = questions[sector][question_index]
        st.write(question)
        choice = st.radio("Select an option", options)
        if st.button("Next"):
            user_answers.append(choice)
            correct_answers_list.append(correct_answer)
            if choice == correct_answer:
                st.write("Correct!")
                st.session_state.correct_answers = st.session_state.get('correct_answers', 0) + 1
            else:
                st.write(f"Wrong! The correct answer is: {correct_answer}")
            
            st.session_state.question_index = question_index + 1
            st.session_state.user_answers = user_answers
            st.session_state.correct_answers_list = correct_answers_list
            st.experimental_rerun()  # Force rerun to update question
    else:
        st.write(f"Quiz completed! You got {st.session_state.get('correct_answers', 0)} out of {len(questions[sector])} correct.")
        st.write("Here is a summary of your answers:")
        
        for i, (question, options, correct_answer) in enumerate(questions[sector]):
            user_answer = user_answers[i]
            st.write(f"**Q{i + 1}:** {question}")
            st.write(f"Your Answer: {user_answer}")
            st.write(f"Correct Answer: {correct_answer}")
            if user_answer != correct_answer:
                st.write("**Result:** Wrong")
            else:
                st.write("**Result:** Correct")
            st.write("")  # Blank line for better readability

        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.session_state.question_index = 0
            st.session_state.correct_answers = 0
            st.session_state.user_answers = []
            st.session_state.correct_answers_list = []
            st.experimental_rerun()  # Force rerun to return to home

def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        st.title("Beginners in Economics")
        st.write("Click on a sector to explore:")
        
        # Create three columns for the sectors
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Primary Sector", key="primary"):
                st.session_state.page = "primary"
                st.experimental_rerun()  # Force rerun to update page

            st.image("Images/Primary.jpg", use_column_width=True)  # Replace with your image path
            st.write("Primary Sector")

        with col2:
            if st.button("Secondary Sector", key="secondary"):
                st.session_state.page = "secondary"
                st.experimental_rerun()  # Force rerun to update page

            st.image("Images/Secondary.jpg", use_column_width=True)  # Replace with your image path
            st.write("Secondary Sector")

        with col3:
            if st.button("Tertiary Sector", key="tertiary"):
                st.session_state.page = "tertiary"
                st.experimental_rerun()  # Force rerun to update page

            st.image("Images/Tertiary.jpg", use_column_width=True)  # Replace with your image path
            st.write("Tertiary Sector")
    
    elif st.session_state.page == "primary":
        show_primary_sector()
    elif st.session_state.page == "secondary":
        show_secondary_sector()
    elif st.session_state.page == "tertiary":
        show_tertiary_sector()
    elif st.session_state.page in ["quiz_primary", "quiz_secondary", "quiz_tertiary"]:
        sector = st.session_state.page.replace("quiz_", "")
        show_quiz(sector)

if __name__ == "__main__":
    main()
