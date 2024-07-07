import yaml
import os

config_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'config.yaml')
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

if config.get('run_localhost'):
    print("Client running on localhost")
else:
    print("Client running remotely")
