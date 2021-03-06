import argparse

from scan import Scan
from local_dirs import *

parser = argparse.ArgumentParser()
parser.add_argument("--perform_scan",
                  action="store", dest="perform_scan", default=1,type=int)
parser.add_argument("--perform_postprocessing",
                  action="store", dest="perform_postprocessing", default=1,type=int)
parser.add_argument("--imc",
                  action="store", dest="imc", default=0,type=int)
parser.add_argument("--iobj",
                  action="store", dest="iobj", default=0,type=int)
parser.add_argument("--Asimov",
                  action="store", dest="Asimov", default=0,type=int)
parser.add_argument("--save_dir",
                  action="store", dest="save_dir", default="",type=str)
parser.add_argument("--load_dir",
                  action="store", dest="load_dir", default="",type=str)
parser.add_argument("--float_ps_together",
                  action="store", dest="float_ps_together", default=1,type=int)
parser.add_argument("--noJprof",
                  action="store", dest="noJprof", default=0,type=int)
parser.add_argument("--start_idx",
                  action="store", dest="start_idx", default=0,type=int)
parser.add_argument("--floatDM",
                  action="store", dest="floatDM", default=0,type=int)
parser.add_argument("--mc_dm",
                  action="store", dest="mc_dm", default=-1,type=int)
parser.add_argument("--catalog_file",
                  action="store", dest="catalog_file", default="DarkSky_ALL_200,200,200_v3.csv",type=str)
parser.add_argument("--diff",
                  action="store", dest="diff", default="p7",type=str)
parser.add_argument("--randlocs",
                  action="store", dest="randlocs", default=0,type=int)
parser.add_argument("--channel",
                  action="store", dest="channel", default="b",type=str)
parser.add_argument("--eventtype",
                  action="store", dest="eventtype", default=0,type=int)
parser.add_argument("--Burkert",
                  action="store", dest="Burkert", default=0,type=int)
parser.add_argument("--use_boost",
                  action="store", dest="use_boost", default=0,type=int)
parser.add_argument("--boost",
                  action="store", dest="boost", default=1,type=int)
parser.add_argument("--mc_string",
                  action="store", dest="mc_string", default="10000dm",type=str)
parser.add_argument("--moreA",
                  action="store", dest="moreA", default=0,type=int)
parser.add_argument("--emin",
                  action="store", dest="emin", default=0,type=int)
parser.add_argument("--emax",
                  action="store", dest="emax", default=39,type=int)
parser.add_argument("--restrict_pp",
                  action="store", dest="restrict_pp", default=0,type=int)

results = parser.parse_args()
iobj=results.iobj
imc=results.imc
Asimov=results.Asimov
save_dir=results.save_dir
load_dir=results.load_dir
float_ps_together=results.float_ps_together
noJprof=results.noJprof
start_idx=results.start_idx
floatDM=results.floatDM
perform_scan=results.perform_scan
perform_postprocessing=results.perform_postprocessing
mc_dm=results.mc_dm
catalog_file=results.catalog_file
diff=results.diff
randlocs=results.randlocs
channel=results.channel
eventtype=results.eventtype
Burkert=results.Burkert
use_boost=results.use_boost
boost=results.boost
mc_string=results.mc_string
moreA=results.moreA
emin=results.emin
emax=results.emax
restrict_pp=results.restrict_pp

if load_dir != "":
  load_dir = work_dir + '/Scan-Small-ROI/data/' + str(load_dir) + "/"
else:
  load_dir = None

print "saving in", work_dir + '/Scan-Small-ROI/data/' + str(save_dir) + "/"
Scan(perform_scan=perform_scan, 
  perform_postprocessing=perform_postprocessing, 
  imc=imc, 
  iobj=start_idx+iobj, 
  Asimov=Asimov, 
  float_ps_together=float_ps_together,
  noJprof=noJprof,
  floatDM=floatDM,
  diff=diff,
  mc_dm=mc_dm,
  load_dir=load_dir,
  verbose=True,
  catalog_file=catalog_file, 
  randlocs=randlocs,
  channel=channel,
  eventtype=eventtype,
  Burkert=Burkert,
  use_boost=use_boost,
  boost=boost,
  mc_string=mc_string,
  moreA=moreA,
  emin=emin,
  emax=emax,
  restrict_pp=restrict_pp,
  save_dir=work_dir + '/Scan-Small-ROI/data/' + str(save_dir) + "/")
