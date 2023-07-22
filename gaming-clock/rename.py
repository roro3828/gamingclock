import pcbnew
import re

def _get_selected_modules():
    modules = pcbnew.GetBoard().GetModules()
    return filter(lambda m: m.IsSelected(), modules)

def _replace_leading_number(target, new):
    match = re.search(r'[0-9]', target)
    idx = match.start()
    return target[:idx] + '{}'.format(new) + target[idx+1:]

def rename_leading_number_selected(new_number):
    selected = _get_selected_modules()
    for module in selected:
        refdes = module.GetReference()
        new_refdes = _replace_leading_number(refdes, new_number)
        print('rename: ' + refdes + ' -> ' + new_refdes)
        module.SetReference(new_refdes)