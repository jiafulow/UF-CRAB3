from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'XX-LABEL-XX'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.JobType.pluginName = 'Analysis'
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'XX-CONFIG-XX'
#config.JobType.outputFiles = ['Output.root']
#config.JobType.pyCfgParams = []
config.JobType.maxMemoryMB = 3800
config.JobType.maxJobRuntimeMin = 900
#config.JobType.numCores = 4

#config.Data.inputDataset = 'XX-DATASET-XX'
#config.Data.inputDBS = 'global'
config.Data.outputPrimaryDataset = 'XX-DATASET-XX'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 1
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 10000
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000  # for ParticleGuns
#config.Data.unitsPerJob = 10000  # for single MinBias
#config.Data.unitsPerJob = 100  # for PU200 events
njobs = XX-NJOBS-XX
config.Data.totalUnits = config.Data.unitsPerJob * njobs
#config.Data.outLFNDirBase = '/store/user/jiafulow/L1MuonTrigger/P2_10_4_0/XX-LABEL-XX/'
config.Data.outLFNDirBase = '/store/group/l1upgrades/L1MuonTrigger/P2_10_4_0/XX-LABEL-XX/'
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3'

#config.Site.storageSite = 'T2_US_Florida'
config.Site.storageSite = 'T3_US_FNALLPC'

tweak_memory = False
if tweak_memory:
    label = 'XX-LABEL-XX'
    if 'PU50' in label:
        config.JobType.maxMemoryMB = 4700 + 400
    elif 'PU100' in label:
        config.JobType.maxMemoryMB = 5300 + 500
    elif 'PU140' in label:
        config.JobType.maxMemoryMB = 5900 + 600
    elif 'PU200' in label:
        config.JobType.maxMemoryMB = 6800 + 700

test_run = False
if test_run:
    #config.Data.splitting = 'EventAwareLumiBased'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 100
    config.Data.totalUnits = config.Data.unitsPerJob * 1

