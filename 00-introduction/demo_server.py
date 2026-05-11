import gradio as gr
from transformers import pipeline

# 注意：用 9b02143... 这个快照路径
MODEL_PATH = "/data1/xyh/.cache/huggingface/hub/models--uer--roberta-base-chinese-extractive-qa/snapshots/9b02143727b9c4655d18b43a69fc39d5eb3ddd53"

qa = pipeline(
    "question-answering",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

gr.Interface.from_pipeline(qa).launch(server_name="0.0.0.0", server_port=7860)