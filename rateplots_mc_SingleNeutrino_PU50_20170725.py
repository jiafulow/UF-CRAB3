# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1NtupleMC --step RAW2DIGI --mc --eventcontent RAWSIM --conditions auto:phase2_realistic --beamspot HLLHC14TeV --geometry Extended2023D17 --era Phase2C2_timing --customise L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAW --filein /store/user/l1upgrades/L1MuonTrigger/P2_9_2_3_patch1/SingleNeutrino_r281707_run2/ParticleGuns/CRAB3/170721_190723/0000/SingleNeutrino_r281707_run2_1.root --no_exec -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Phase2C2_timing)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/l1upgrades/L1MuonTrigger/P2_9_2_3_patch1/SingleNeutrino_r281707_run2/ParticleGuns/CRAB3/170721_190723/0000/SingleNeutrino_r281707_run2_1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1NtupleMC nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('l1NtupleMC_RAW2DIGI.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
#process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1simulation_step = cms.Path(process.simEcalTriggerPrimitiveDigis * process.simHcalTriggerPrimitiveDigis * process.SimL1Emulator)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step,process.RAWSIMoutput_step)
#from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
#associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW 

#call to customisation function L1TReEmulMCFromRAW imported from L1Trigger.Configuration.customiseReEmul
#process = L1TReEmulMCFromRAW(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


if True:
    from L1TMuonSimulations.Configuration.tools import *
    txt = 'L1TMuonSimulations/Configuration/data/input_SingleNeutrino_PU50.txt'
    txt = os.path.join(os.environ['CMSSW_BASE'], 'src', txt)
    fileNames_txt = loadFromFile(txt)
    process.source.fileNames = fileNames_txt
if True:
    from L1Trigger.L1TMuonEndCap.customise_Phase2C2 import customise as customise_Phase2C2
    process = customise_Phase2C2(process)
if True:
    #process.schedule.remove(process.L1TrackTrigger_step)
    process.simEmtfDigis.GEMEnable                   = False
    process.simEmtfDigis.IRPCEnable                  = False
    process.simEmtfDigis.TTEnable                    = False
if True:
    process.TFileService = cms.Service("TFileService",
        fileName = cms.string("histos.root"),
        closeFileFast = cms.untracked.bool(True),
    )
    from L1TMuonSimulations.Analyzers.rpcintegration_cfi import *
    process.load("L1TMuonSimulations.Analyzers.rpcintegration_cfi")
    process.trackcounting.outFileName = "rateplots_mc.root"
    process.trackcounting.verbosity = 1
    process.p = cms.Path(process.trackcounting)
    use_fs_trackcounting(process)

process.schedule = cms.Schedule(process.L1simulation_step, process.raw2digi_step, process.p)
#process.maxEvents.input = -1


# Configure framework report and summary
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Run in unscheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)

## Dump the full python config
#with open("dump.py", "w") as f:
#    f.write(process.dumpPython())
