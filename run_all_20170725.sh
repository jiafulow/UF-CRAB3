#!/bin/bash

echo "[INFO] Using CMSSW_BASE: $CMSSW_BASE"

#./run.ntuple-SingleMuonPD.sh rateplots_data_SingleMuonPD_r281707_run2_20170725.py SingleMuonPD -1

./run.ntuple.sh rateplots_mc_SingleNeutrino_r281707_run2_20170725.py              ParticleGuns -1
./run.ntuple.sh rateplots_mc_SingleNeutrino_r281707_20170725.py                   ParticleGuns -1
./run.ntuple.sh rateplots_mc_SingleNeutrino_PU50_20170725.py                      ParticleGuns -1
./run.ntuple.sh rateplots_mc_SingleNeutrino_PU100_20170725.py                     ParticleGuns -1
./run.ntuple.sh rateplots_mc_SingleNeutrino_PU140_20170725.py                     ParticleGuns -1
./run.ntuple.sh rateplots_mc_SingleNeutrino_PU200_20170725.py                     ParticleGuns -1
