import torch
import torch_neuron
#model_path= '/home/erem/yolov5/best.pt'
#model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)  # whatever version do you need
model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
for m in model.modules():
    if hasattr(m, 'inplace'):
        m.inplace = False

fake_image = torch.zeros([1, 3, 640, 640], dtype=torch.float32) # customize size here 640x640 is common

try:
    torch.neuron.analyze_model(model, example_inputs=[fake_image])
except Exception:
    torch.neuron.analyze_model(model, example_inputs=[fake_image])

model_neuron = torch.neuron.trace(model,
                                example_inputs=[fake_image])

## Export to saved model
model_neuron.save("bestneuron_yolov5n.pt")