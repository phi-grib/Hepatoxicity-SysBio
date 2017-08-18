from cobra.io import read_sbml_model, save_json_model, load_json_model
from cobra.flux_analysis import variability
from re import search, sub
from os import path, mkdir
from glob import glob

DO_ALL_MODELS = True

media = path.join('/media/sf_G_DRIVE/Dropbox/Dropbox/trabajo/paper pablo/mmb_chapter/', 'recon2_fva')

modelfolder = path.join(media, 'models')
sbmlfolder = path.join(modelfolder,'sbml')
jsonfolder = path.join(modelfolder,'json')


def model_list_all():
   ml = {}
   for m in glob(path.join(sbmlfolder, '*.xml')):
          mname = path.basename(m)
          mname = sub('.xml', '', mname)
          ml[mname] = m    
   return ml          


ml = model_list_all()
for network in sorted(ml):
    print network    
    model = read_sbml_model(ml[network])
    print(jsonfolder)
    save_json_model(model, jsonfolder + "/" + network + ".json")
    print(model)