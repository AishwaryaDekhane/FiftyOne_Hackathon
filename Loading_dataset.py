import fiftyone as fo
import fiftyone.utils.huggingface as fouh
from ultralytics import YOLO
import fiftyone.utils.ultralytics as fou
import fiftyone.zoo as foz

# Load the dataset
# Note: other available arguments include 'max_samples', etc
#dataset = fouh.load_from_hub("dgural/Thermal-Person-Detector", persistent = True, num_workers = 4)
dataset = fo.load_dataset("dgural/Thermal-Person-Detector")
# The path to export the dataset
EXPORT_DIR = "/tmp/oiv7-yolo"

# YOLO format requires a common classes list
classes = dataset.default_classes

dataset.export(
    export_dir=EXPORT_DIR,
    dataset_type=fo.types.YOLOv5Dataset,
    label_field="ground_truth",
    split="train",
    classes=classes,
)

dataset.export(
    export_dir=EXPORT_DIR,
    dataset_type=fo.types.YOLOv5Dataset,
    label_field="ground_truth",
    split="val",  # Ultralytics uses 'val'
    classes=classes,
)

# Launch the App
#session = fo.launch_app(dataset)

#session.wait()

# The path to the `dataset.yaml` file we created above
YAML_FILE = "/tmp/oiv7-yolo/dataset.yaml"

# Load a model
model = YOLO("yolov8s.pt")  # load a pretrained model
# model = YOLO("yolov8s.yaml")  # build a model from scratch

# Train the model
model.train(data=YAML_FILE, epochs=10)

# Evaluate model on the validation set
metrics = model.val()

# Export the model
path = model.export(format="onnx")