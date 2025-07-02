import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title('My To-do app')
st.subheader('This is my to-do app.')
st.write('This app is to increase your productivity.')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Type task here...",
              on_change=add_todo, key='new_todo')

