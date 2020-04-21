import yaml
from Cheetah.Template import Template

class Proposition(object):
    def __init__(self, p_data):
        self.text = p_data["text"]
        self.f    = p_data["f"] 

class Formula(object):
    def __init__(self, f_name, f_dict):
        self.name     = f_name
        self.text     = f_dict["text"] 
        self.formula  = f_dict["formula"]

class Specification(object):
    def __init__(self, step, states, AP, formulas):
        self.step = step
        self.states = states
        self.AP = AP
        self.formulas = formulas 
    def getSearchList(self):
        return [{"state_list":self.states,"AP":self.AP,"formulas":self.formulas}]

class State(object):
    def __init__(self, name, datatype, idx):
        self.name = name
        self.datatype = datatype
        self.idx = idx


def get_formulas(spec_obj):
    formulas = {} 
    for f_name in spec_obj["formulas"].keys(): 
        f_dict = spec_obj["formulas"][f_name] 
        formulas[f_name] = Formula(f_name, f_dict)

    return formulas
        
def get_specification(states, AP, formulas, spec_obj):
    step = spec_obj["STL_Spec"]["step"]
    top_phi_name = spec_obj["STL_Spec"]["TopPhi"]
    return Specification(step, states, AP, formulas)

def get_propositions(spec_obj):
    AP = {}
    props = spec_obj["STL_Spec"]['AP']
    for p_name in props:
        AP[p_name] = Proposition(spec_obj["propositions"][p_name])
    return AP

def get_states(spec_obj):
    states = []
    i = 0
    for state_name in spec_obj["STL_Spec"]["states"]:
        states.append(State(state_name, "real", i))
        i += 1
    return states


if __name__ == "__main__":
    with open("spec.yaml", "r") as f:
        spec_obj = yaml.load(f, Loader=yaml.FullLoader)

    # Collect information from YAML
    AP       = get_propositions(spec_obj)
    formulas = get_formulas(spec_obj)
    states   = get_states(spec_obj)
    spec = get_specification(states, AP, formulas, spec_obj)

    # Open Cheetah template for writing
    with open("spec_template_lv6.tmpl", "r") as f:
        tmpl = Template(f.read(),searchList=spec.getSearchList()) 

        with open("spec_output.lus","w") as f2:
            f2.write(str(tmpl)) 

        print(tmpl)
 



