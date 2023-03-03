import params as par


def create_dict(vals):
    return {key: val for key, val in vals}


dicat = create_dict(par.icat)
die3 = create_dict(par.ie3)


def filter_cat(inv: str):
    assert inv in [i[0] for i in par.itype]
    alis = list(par.bounds[inv].keys())
    return [(key, dicat[key]) for key in alis]


def filter_e3(inv: str, cat: str):
    assert inv in [i[0] for i in par.itype]
    fcat = filter_cat(inv)
    assert cat in [i[0] for i in fcat]
    e3li = par.bounds[inv][cat]
    return [(key, die3[key]) for key in e3li]


print(die3)
print(filter_cat('1.1'))
print(filter_e3('1.1', 'category1_1'))
