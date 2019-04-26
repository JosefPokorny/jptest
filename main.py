
print("Hello world from python")



from keboola import docker



# Configuration parameters
cfg_keboola = docker.Config("/data/")
with open("/data/config.json", mode="r") as config_file:
    cfg = json.load(config_file)

params = cfg["parameters"]
image = cfg["image_parameters"]


USERNAME = params["hovno"]

print(USERNAME)