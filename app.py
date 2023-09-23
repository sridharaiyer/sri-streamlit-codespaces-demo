import streamlit as st
import random

# Function to read facts from "facts.txt" file
def read_facts(filename):
    with open(filename, 'r') as file:
        facts = file.read().split('\n\n')
    return [fact.strip() for fact in facts if fact.strip()]

# Main Streamlit app
def main():
    st.title("Random Fact Generator")
    
    # Read facts from the file
    facts = read_facts("facts.txt")
    
    if not facts:
        st.error("No facts found in the file.")
    else:
        # Button to generate a random fact
        if st.button("Generate A Random Fact"):
            random_fact = random.choice(facts)
            # Style the fact text with a nice font and larger font size
            st.markdown(f"<p style='font-family: Arial; font-size: 20px;'>{random_fact}</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
