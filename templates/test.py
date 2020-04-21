import spec

class State(object):
    def __init__(self, name, datatype, idx):
        self.name = name
        self.datatype = datatype
        self.idx = idx


if __name__ == "__main__":
    s1 = State("theta", "real", 0)
    s2 = State("d_theta", "real", 1)
    state_list = [s1, s2]

    namespace = {"state_list":state_list}
    tmpl = spec.spec(searchList=[namespace]) 
    tmpl.respond()

    print(tmpl)


