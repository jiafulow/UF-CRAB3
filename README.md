### Requirements

Follow the CRAB3 tutorial: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial . Importantly, set up the CRAB3 environment by sourcing (if using SLC7):

``` shell
source /cvmfs/cms.cern.ch/crab3/crab_slc7.sh
```


For frequently asked questions, see: https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ

### Use this repository

``` shell
# Make sure to use the correct branch for the CMSSW version
git clone -b L1MuonTrigger-P2_10_6_3 git@github.com:jiafulow/UF-CRAB3.git CRAB3/P2_10_6_3
```

- Edit 'crab_template.py' to specify:
  - `config.Data.outLFNDirBase`
  - `config.Site.storageSite`
  - `config.JobType.pluginName`, `config.Data.inputDataset`, `config.Data.outputPrimaryDataset`, etc

