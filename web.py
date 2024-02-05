import streamlit as st
import functions
todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state['new_todo'] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("Todo tracker")
st.subheader("You can new todo items and also make them complete them")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()
st.text_input(label="none", label_visibility="collapsed", placeholder="Add new todo... ", on_change=add_todo,
              key="new_todo")
