import gradio as gr
import ollama

# Function to process user queries
def solve_math_problem(problem):
    response = ollama.chat(model='gemma3:4b', messages=[{'role': 'user', 'content': problem}])
    # Extract only the assistant's message content
    return response['message']['content']

# Define Gradio Interface
Interface = gr.Interface(
    fn=solve_math_problem,
    inputs=gr.Textbox(label="Enter a math problem"),
    outputs=gr.Textbox(label="Solution", lines=10),  # multiline output
    title="AI-Powered Math Solver by Akramuddoula",
    description="Ask any math question, and Gemma will provide a step-by-step solution."
)

# Launch the App
Interface.launch(share=True)