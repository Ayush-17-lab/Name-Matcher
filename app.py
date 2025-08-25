import re
import unicodedata
import streamlit as st

def normalize_name(s: str) -> str:
    """Lowercase, remove punctuation, normalize spaces."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)  # keep only letters/numbers/spaces
    s = re.sub(r"\s+", " ", s).strip()
    return s

def similarity(a: str, b: str) -> float:
    """Return 1.0 if normalized strings are exactly the same, else 0.0."""
    return 1.0 if normalize_name(a) == normalize_name(b) else 0.0

st.set_page_config(page_title="Name Similarity Checker", page_icon="🔎")

st.title("🔎 Name Similarity Checker")

name1 = st.text_input("Enter Name 1")
name2 = st.text_input("Enter Name 2")

if st.button("Check Similarity"):
    if not name1.strip() or not name2.strip():
        st.warning("Please enter both names.")
    else:
        sim = similarity(name1, name2)
        percent = round(sim * 100, 2)

        st.metric("Similarity", f"{percent}%")

        if sim == 1.0:
            st.success("✅ Names match exactly.")
        else:
            st.error("❌ Names don't match (0% similarity).")

