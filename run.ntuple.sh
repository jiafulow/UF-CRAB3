#!/bin/bash

customise_for_ntuple() {
cat <<EOF >>crab.py
# customise for ntuple
import os
import imp
cfgBaseName = os.path.basename('$config').replace('.py', '')
file, pathname, description = imp.find_module(cfgBaseName)
pset = imp.load_module(cfgBaseName, file, pathname, description)
#
config.JobType.pluginName = 'Analysis'
delattr(config.JobType, "maxMemoryMB")
delattr(config.JobType, "maxJobRuntimeMin")
delattr(config.JobType, "numCores")
config.Data.userInputFiles = list(pset.process.source.fileNames)
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 20
config.Data.totalUnits = len(config.Data.userInputFiles)
#
config.Data.ignoreLocality = True
config.Site.whitelist = ['T3_US_FNALLPC']
config.Site.ignoreGlobalBlacklist = True
EOF
}


config=$1
dataset=$2
njobs=$3
label=`echo $config | sed "s/^\(.*\)_[0-9]\+\.py/\1/"`
projdir=crab_${label}
echo "Run config=$config dataset=$dataset njobs=$njobs label=$label"

mkdir -p crab_projects crab_projects_old
rm -rf crab_projects_old/${projdir}

if [ -d crab_projects/${projdir} ]; then
  taskname=`grep 'Task name' crab_projects/${projdir}/crab.log | head -1 | sed -e 's/.* \([0-9]\+_[0-9]\+\):.*/\1/'`
  mv crab_projects/${projdir} crab_projects_old/${projdir}_${taskname}
fi

sed "s@XX-LABEL-XX@$label@g" crab_template.py | sed "s@XX-DATASET-XX@$dataset@g" | sed "s@XX-CONFIG-XX@$config@g" | sed "s@XX-NJOBS-XX@$njobs@g"  > crab.py

customise_for_ntuple

crab submit -c crab.py
#crab submit -c crab.py --dryrun
cp crab.py crab_projects/${projdir}/
