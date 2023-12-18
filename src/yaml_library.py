import yaml


def yaml_to_dict(ob_yaml: str) -> dict[str, object]:
    '''
    Convierte un yaml en str en un diccionario
    '''
    return yaml.load(ob_yaml, Loader=yaml.FullLoader)


def test():
    '''
    Para probar el buen funcionamiento de la libreria
    '''
    print('hellow from Jaime library!')
