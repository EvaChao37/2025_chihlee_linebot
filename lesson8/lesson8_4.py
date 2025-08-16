import gradio as gr
with gr.Blocks() as demo:
    gr.Markdown("""# 歡迎使用 Gradio
    請輸入您的姓名，會即時顯示輸入的內容。
    """)
    input_textbox = gr.Textbox(placeholder="請輸入文字", label="輸入框")
    output_textbox = gr.Textbox(placeholder="輸入結果會顯示在這裡", label="輸出框")

    @input_textbox.change(inputs=input_textbox, outputs=output_textbox)
    def update_output(text):
        return text
    demo.launch()
    ##這段程式碼建立了一個 Gradio 的 Blocks 架構，包含一個輸入框和一個輸出框，當使用者在輸入框中輸入文字時
    # ，輸出框會即時顯示相同的文字。這是一個簡單的互動範例，展示了 Gradio 的基本功能。