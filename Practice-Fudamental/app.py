# import Module
import streamlit as st

#title
st.title("Kelas Awan Pintar - Arief Fadhillah R")

#header
st.header("Belajar fungsi dasar streamlit")

#subheader
st.subheader("Let's go belajar streamlit")

#Text
st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam molestie erat vitae turpis rhoncus pretium. Nam rhoncus ante vitae velit lobortis, ac porta nibh aliquet. Proin in ante nibh. Maecenas interdum dui vitae imperdiet sollicitudin. Sed iaculis, elit sit amet ullamcorper scelerisque, augue magna commodo orci, vitae varius nisi lorem quis lectus. Pellentesque eget tellus eu neque bibendum lobortis. Suspendisse aliquam pellentesque posuere. Cras laoreet nisl ac nulla ullamcorper aliquam. Donec vitae nulla a leo consectetur pretium.")

#markdown
st.markdown("# Markdown1")
st.markdown("## Markdown2")
st.markdown("### Markdown3")
st.markdown("##### Markdown4")

#markdown multi
st.markdown("""
# Test 1
## Test 2
### Test 3
""",True)

#code block
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

#latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')