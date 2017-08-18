# Compute FVA for each cell type, store critical genes
# Perform sensitivity analsysis
# Use python2.7
# Use cobra<=0.5.11

from cobra.io import read_sbml_model, save_json_model, load_json_model
from cobra.flux_analysis import variability
from re import search, sub
from os import path, mkdir
from glob import glob

DO_ALL_MODELS = False

media = path.join('/media/sf_G_DRIVE/Dropbox/Dropbox/trabajo/paper pablo/mmb_chapter/', 'recon2_fva')

modelfolder = path.join(media, 'models')
sbmlfolder = path.join(modelfolder,'sbml')
jsonfolder = path.join(modelfolder,'json')
fvafolder = path.join(media, 'fva')

models = {'recon2_biomodels':  path.join(sbmlfolder, 'MODEL1109130000.xml'),
          'liver_hepatocytes': path.join(sbmlfolder, 'models', 'liver_hepatocytes.xml'),
          'recon2_model': path.join(sbmlfolder, 'models', 'recon2_model.xml')
          }
# gene diff expression by cell
pathf = path.join(media, 'fva', 'rpath.txt')

mynetwork = 'liver_hepatocytes'
network = models[mynetwork]


def model_list():
    ml = {}
    if DO_ALL_MODELS:
        for m in glob(path.join(sbmlfolder, '*.xml')):
            mname = path.basename(m)
            mname = sub('.xml', '', mname)
            ml[mname] = m
    else:
        # just pick one from your personalized list
        ml[mynetwork] = models[mynetwork]
    return ml


def fva(json):
    model = load_json_model(json)
    bio = {reaction: reaction.objective_coefficient
           for reaction in model.reactions if search('biomass',reaction.name)}
    biom = bio.keys()[0]
    # set the objective
    model.change_objective(biom)
    # add constraints
    model.optimize()
    f0 = model.solution.f
    # get a dictionary with all non-zero fluxes
    fluxes = {reaction.id: reaction.x for reaction in model.reactions if reaction.x != 0}
    # first time store for the wild type
    v = variability.flux_variability_analysis(model)
    return v


def store_fva(network, v):
    ow = open(path.join(fvafolder, network+'.fva'), 'w')
    for g in sorted(v):
        ow.write("%s %.f %f\n" % (g, v[g]['minimum'], v[g]['maximum']) )
    ow.close()
            
# read the model
ml = model_list()
for network in sorted(ml):
    print network    
    json = path.join(jsonfolder, network+'.json')    
    # Flux variability analysis
    v = fva(json)
    store_fva(network, v)
