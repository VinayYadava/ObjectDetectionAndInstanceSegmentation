# loading yolov9c.pt file and yolov9c-seg.pt file replace the weight of backbone weight of yolov9c-seg.pt from backbone weight of yolov9c.pt and proceed.

import torch
from ultralytics import YOLO
import yaml

def replace_backbone_weights(source_model_path, target_model_path, backbone_layers='model.model.9'):
    # Load the source and target models
    source_model = YOLO(source_model_path)
    target_model = YOLO(target_model_path)

    # Extract the backbone weights from the source model
    backbone_state_dict = {}
    for key, value in source_model.state_dict().items():
        if key.startswith(backbone_layers):
            backbone_state_dict[key] = value

    # Load the backbone weights onto the target model
    target_model.load_state_dict(backbone_state_dict, strict=False)

    # Save the modified target model
    modified_model_path = target_model_path.replace('.pt', '_modified.pt')
    target_model.save(modified_model_path)

    # Save the modified model's architecture to a YAML file
    with open(target_model_path.replace('.pt', '_modified.yaml'), 'w') as f:
        yaml.safe_dump(target_model.model.yaml, f, default_flow_style=False, indent=4)

    return modified_model_path, target_model_path.replace('.pt', '_modified.yaml')

if __name__ == '__main__':
  # Example usage:
  source_model_path = 'yolov9c.pt'
  target_model_path = 'yolov9c-seg.pt'
  modified_model_path, modified_yaml_path = replace_backbone_weights(source_model_path, target_model_path)
  print("Modified model saved at:", modified_model_path)
  print("Modified YAML saved at:", modified_yaml_path)
