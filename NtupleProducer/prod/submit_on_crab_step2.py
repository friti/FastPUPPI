from CRABClient.UserUtilities import config, ClientException
import yaml
import datetime
from fnmatch import fnmatch
from argparse import ArgumentParser
from files_path_step1_10k import files

production_tag = datetime.date.today().strftime('%Y%b%d')

config = config()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = 'multipi_step2_digirecominiado_pu0_%s' % production_tag

config.section_('Data')
config.Data.publication = False
config.Data.outLFNDirBase = '/store/group/cmst3/group/l1tr/friti/%s' % ('Multipion_Phase2Spring23GS_DIGIRECOMiniAOD_PU0_' + production_tag)
#config.Data.outLFNDirBase = '/store/user/friti/%s' % ('Multipion_PU0_Phase2Spring23GS_GEN_' +'_' + production_tag)
config.Data.inputDBS = 'global'
#config.Data.totalUnits = 10000

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'Multipion-Phase2Spring23GS_step2_v2_cfg.py'
#config.JobType.scriptExe = 'crab_script.sh'
#config.JobType.maxJobRuntimeMin = 3000
#config.JobType.allowUndistributedCMSSW = True
#config.Data.allowNonValidInputDataset = True
#config.JobType.numCores = 4
config.JobType.maxMemoryMB = 4000
#config.JobType.maxMemoryMB = 3000
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

if __name__ == '__main__':

  from CRABAPI.RawCommand import crabCommand
  from CRABClient.ClientExceptions import ClientException
  from multiprocessing import Process

  def submit(config):
          crabCommand('submit', config = config)



#config.Data.inputDataset = '/ttbarToBsToTauTau_BsFilter_TauTauFilter_TuneCP5_13TeV-pythia8-evtgen/RunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2/AODSIM'

config.Data.userInputFiles = files
config.General.requestName = 'Multipion-Phase2Spring23GS'
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 1
#globaltag = '106X_upgrade2018_realistic_v16_L1v1'
                
config.JobType.outputFiles = ['multipion_phase2_digirecominiaod_pu0.root']
        
print(config)
submit(config)
