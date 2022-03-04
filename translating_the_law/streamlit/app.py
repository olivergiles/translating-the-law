import streamlit as st

def main():
    st.title("Translating the Law")

    options = st.multiselect(
        'What features do you want',
        ['Summary', 'Charts'],
        [])

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def remote_css(url):
        st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

    def icon(icon_name):
        st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

    local_css("translating_the_law/streamlit/style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    icon("search")
    selected = st.text_input("", "Search...")
    button_clicked = st.button("OK")

    button_show = st.button("Show")

    search_page_css = """
    .css {
        display: none;
    }
    .css-10trblm {
        display: none;
    }
    """
    display_search_page_css = """
    .css {
        display: none;
    }
    .css-10trblm {
        display: center;
    }
    """
    if button_clicked:
        #st.markdown("<style>.css-10trblm {display: none;}</style>", unsafe_allow_html=True)
        st.markdown(f"<style>{search_page_css}</style>", unsafe_allow_html=True)
    
    if button_show:
        st.markdown(f"<style>{display_search_page_css}</style>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()