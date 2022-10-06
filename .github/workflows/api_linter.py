import ruamel.yaml

with open("manifests/api-eks/alb/prd/api-public.yaml", "r") as f:
    yaml_parser = ruamel.yaml.YAML()
    data = yaml_parser.load(f.read())

if data["stg"]["hello"]["jump"] == "no":
    print("YES")
else:
    print("NO")