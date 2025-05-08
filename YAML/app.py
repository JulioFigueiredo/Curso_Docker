import yaml


if __name__ == '__main__':
    
    stream = open('test.yaml', 'r') # r de leitura
    dictionary = yaml.safe_load(stream)
    
    for key, value in dictionary.items():
        print(key + " : " + str(value))
    