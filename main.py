import tensorflow as tf
import yaml
import torch.nn as nn

from tensorflow import Module

class MyModel(Module):
    def __init__(self,config):
        super(MyModel, self).__init__()
        self.config = config
        print(dir(self.config["head"]))
        self.head = self._build_head(self.config["head"])

    def _build_head(self,head_config):
        head = nn.ModuleDict()
        for key, value in head_config.items():
            layers = self._build_layers(value)
            head[key] = nn.Sequential(*layers)
        return head

    
    def _build_layers(self, layer_configs):
        layers = []
        for config in layer_configs:
            layer_type = config[2]  # Index 2 specifies the type of layer
            if hasattr(nn, layer_type):
                layer_class = getattr(nn, layer_type)
                layer_params = config[3] if len(config) > 3 else {}
                layer = layer_class(*layer_params)
                layers.append(layer)
            else:
                # Custom layer construction logic goes here
                pass
        return layers

if __name__ == '__main__':
    with open('model.yaml', 'r') as file:
        config = yaml.safe_load(file)
    model = MyModel(config=config)

    print(config.keys())