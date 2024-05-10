import torch
import pprint
import yaml

with open("../model.yaml" ,"r") as f1:
    
    config1 = yaml.safe_load(f1)
    
f1.close()
print(config1.keys())
with open("yolov9-c.yaml" ,"r") as f2:

    config2 = yaml.safe_load(f2)
    
f2.close()
print(config2.keys())



pprint.pprint(f"{config2['backbone']}")


class MyModel(torch.nn.Module):
    def __init__(self, config):
        super(MyModel, self).__init__()
        self.config = config
        print(dir(self.config["backbone"]))
        self.head = self._build_head(self.config["head"])
    def self._build_backbone(self,cnf):
        for num , a,b,c,d in enumerate(cnf):
        