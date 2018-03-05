# _*_ coding:utf-8 _*_

import toml

def toml_load(file_name):
    try:
        with open(file_name, encoding="utf-8") as conf_file:
            conf = toml.load(conf_file)
        return conf
    except Exception as e:
        print(str(e))

def toml_dump(conf, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as conf_file:
            conf = toml.dump(conf, conf_file)
        return conf
    except Exception as e:
        print(str(e))

def read_file(file_name):
    try:
        with open(file_name, encoding="utf-8") as conf_file:
            toml_str = conf_file.read()
        return toml_str
    except Exception as e:
        print(str(e))

def toml_dumps(conf):
    return toml.dumps(conf)

def toml_loads(conf_str):
    try:
        return toml.loads(conf_str)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    conf = toml_load("./conf.toml")
    print("toml_load:", conf)
    conf["title"] = "TOML TEST"
    conf_dump = toml_dump(conf, "./conf.toml")
    print("conf_dump:", conf_dump)
    read_str = read_file("./conf.toml")
    print("read_str:", read_str)
    conf_loads = toml_loads(read_str)
    print("conf_loads:", conf_loads)
    conf_dumps = toml_dumps(conf_loads)
    print("conf_dumps:", conf_dumps)


