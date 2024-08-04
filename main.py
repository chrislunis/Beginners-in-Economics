import streamlit as st
from PIL import Image

def show_primary_sector():
    st.title("Primary Sector")
    st.write(
        """• This involves the extraction and harvesting of natural resources.
        • It includes activities such as agriculture, mining, fishing, and forestry.
        • Essentially, it’s about raw materials and resources.
        • The primary sector is called 'primary' because it is the first sector that must be established in order for a country to begin to industrialise.
        • It provides the foundation for all other economic activity.
        • India is the largest employer of Primary Sector."""
    )
    # Uncomment if needed: st.image("Images/Primary.jpg", use_column_width=True)
    
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_primary"
        st.session_state.question_index = 0

def show_secondary_sector():
    st.title("Secondary Sector")
    st.write(
        """• This sector focuses on manufacturing and industry.
        • It involves transforming raw materials from the primary sector into finished products.
        • Examples include automobile manufacturing, construction, and food processing.
        • It is also called the Industrial Sector."""
    )
    # Uncomment if needed: st.image("Images/Secondary.jpg", use_column_width=True)
    
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_secondary"
        st.session_state.question_index = 0

def show_tertiary_sector():
    st.title("Tertiary Sector")
    st.write(
        """• This sector provides services rather than goods.
        • It includes retail, entertainment, healthcare, education, and financial services.
        • The emphasis here is on providing services to consumers and business.
        • Services are also called "intangible goods"."""
    )
    # Uncomment if needed: st.image("Images/Tertiary.jpg", use_column_width=True)
    
    if st.button("Take Quiz"):
        st.session_state.page = "quiz_tertiary"
        st.session_state.question_index = 0

def show_quiz(sector):
    st.title(f"{sector.capitalize()} Sector Quiz")
    
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
    if 'responses' not in st.session_state:
        st.session_state.responses = []

    if question_index < len(questions[sector]):
        question, options, correct_answer = questions[sector][question_index]
        st.write(question)
        choice = st.radio("Select an option", options)
        if st.button("Next"):
            is_correct = choice == correct_answer
            st.session_state.responses.append((question, choice, is_correct, correct_answer))
            st.session_state.question_index = question_index + 1
    else:
        st.write("Quiz completed!")
        # Show results summary
        st.write("Results Summary:")
        for q, user_answer, correct, answer in st.session_state.responses:
            st.write(f"**Question:** {q}")
            st.write(f"**Your Answer:** {user_answer} ({'Correct' if correct else 'Incorrect'})")
            if not correct:
                st.write(f"**Correct Answer:** {answer}")
            st.write("")

        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.session_state.question_index = 0
            st.session_state.responses = []

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
                st.session_state.question_index = 0

            # Uncomment if needed: st.image("Primary.jpg", use_column_width=True)
            st.write("Primary Sector")

        with col2:
            if st.button("Secondary Sector", key="secondary"):
                st.session_state.page = "secondary"
                st.session_state.question_index = 0

            # Uncomment if needed: st.image("Secondary.jpg", use_column_width=True)
            st.write("Secondary Sector")

        with col3:
            if st.button("Tertiary Sector", key="tertiary"):
                st.session_state.page = "tertiary"
                st.session_state.question_index = 0

            # Uncomment if needed: st.image("Tertiary.jpg", use_column_width=True)
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
