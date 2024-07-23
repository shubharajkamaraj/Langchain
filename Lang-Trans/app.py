import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator object with your API key
translator = Translator()

# Streamlit UI
def main():
    st.title('Language Translator using Google Translate API')

    # Get language codes and names for dropdowns
    lang_codes = list(LANGUAGES.keys())
    lang_names = list(LANGUAGES.values())
    
    # Input text and language selection
    text = st.text_area('Enter text to translate', height=150)
    from_lang = st.selectbox('From Language', lang_names, index=lang_codes.index('en'))
    to_lang = st.selectbox('To Language', lang_names, index=lang_codes.index('fr'))
    
    # Translate button
    if st.button('Translate'):
        if text:
            try:
                translated_text = translator.translate(text, src=from_lang, dest=to_lang).text
                st.write('Translated Text:')
                st.write(translated_text)
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")
        else:
            st.warning('Please enter text to translate')

    # Copyright notice
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #888;
        font-size: 12px;
    }
    </style>
    <div class="footer">
        <p>&copy; Copyright 2024 shubharaj.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
