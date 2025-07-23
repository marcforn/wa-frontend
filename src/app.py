import streamlit as st

def page_one():
    st.title("Page One")
    if st.button("Click me on Page One"):
        print("Button on Page One clicked!")
        st.success("Button on Page One clicked!")
        

def page_two():
    st.title("Page Two")
    if st.button("Click me on Page Two"):
        st.success("Button on Page Two clicked!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Page One", "Page Two"))

    if page == "Page One":
        page_one()
    else:
        page_two()

if __name__ == "__main__":
    main() 