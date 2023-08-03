import gradio as gr
import torch
from loaded_model import CNNModel
import loaded_model

model = CNNModel()
model.load_state_dict(torch.load(f="./mnist_model.pt"))


# Define a function to make predictions with your model
def classify_image(image):
    # Preprocess the image
    preprocess = loaded_model.create_transformer()
    
    image_tensor = preprocess(image)
    image_tensor = image_tensor.unsqueeze(0)

    # Make prediction
    with torch.no_grad():
        output = model(image_tensor)
    _, predicted_class = torch.max(output, 1)

    return f"Predicted class: {predicted_class.item()}"


gr.Interface(fn=classify_image, inputs="sketchpad", outputs="label").launch()




