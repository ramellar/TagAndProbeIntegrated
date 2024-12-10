import os

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def splitInBlocks (l, n):
    """split the list l in n blocks of equal size"""
    k = len(l) / n
    r = len(l) % n

    i = 0
    blocks = []
    while i < len(l):
        if len(blocks)<r:
            blocks.append(l[i:i+k+1])
            i += k+1
        else:
            blocks.append(l[i:i+k])
            i += k

    return blocks

###########

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--inFileList", dest="inFileList",   type=str, default=None, help="Input list of files to process (should include the subfolder inside .../EgTauTagAndProbe/EgTauTagAndProbe/inputFiles)")
parser.add_option("--inJson",     dest="inJson",       type=str, default=None, help="Input list of data certification Json files")
parser.add_option("--outFolder",  dest="outFolder",    type=str, default=None, help="Output folder where to store")
parser.add_option("--nJobs",      dest="nJobs",        type=int, default=None, help="Number of jobs to run per filelist")
parser.add_option("--run",        dest="run",          type=str, default=None, help="Run2 or Run3 dataset")
parser.add_option("--queue",      dest="queue",        type=str, default=None, help="long or short queue")
parser.add_option("--no_exec",    dest="no_exec",      action='store_true', default=False, help="stop execution")

parser.add_option("--objType",    dest="objType",      type=str, default=None, help="ele, or tau objects types")
parser.add_option("--jobType",    dest="jobType",      type=str, default=None, help="AOD2MINIAOD, noTagAndProbe, noTagAndProbeAOD, noTagAndProbeMT, tagAndProbe, reEmulL1_zeroBias, reEmulL1_MC job types")
parser.add_option("--allBXs",     dest="allBXs",       type=str, default="0",  help="Store allBXs or only BX=0? (option valid only for reEmulL1_zeroBias jobs)")
parser.add_option("--caloParams", dest="caloParams",   type=str, default=None, help="Which caloParams to use")
parser.add_option("--globalTag",  dest="globalTag",    type=str, default=None, help="Which globalTag to use")

(options, args) = parser.parse_args()

infile_base  = os.getcwd()+'/../'
user = infile_base.split('/')[5]
outfile_base = "/data_CMS/cms/"+user+"/Run3_2024/"

###########

print(infile_base+'/inputFiles/'+options.inFileList)

filelist = open(infile_base+'/inputFiles/'+options.inFileList, 'r')

# for line in filelist.readlines():
#     print(line.strip())


folder = outfile_base+options.outFolder
njobs = options.nJobs
JSONfile = infile_base+'/DataCertificationJsons/'+str(options.inJson)
run = options.run
queue = options.queue

jobtype = options.jobType
allBXs = options.allBXs
caloParams = options.caloParams
globalTag = options.globalTag

os.system('mkdir -p ' + folder)
files = [f.strip() for f in filelist]
print("Input has" , len(files) , "files")
if njobs > len(files) : njobs = len(files)
filelist.close()

fileblocks = splitInBlocks (files, njobs)

for idx, block in enumerate(fileblocks):
    outRootName = folder + '/Ntuple_' + str(idx) + '.root'
    if jobtype == "AOD2MINIAOD": outRootName = folder + '/MiniAOD_Ntuple_' + str(idx) + '.root'
    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outListName = folder + "/filelist_" + str(idx) + ".txt"
    outLogName  = folder + "/log_" + str(idx) + ".txt"

    jobfilelist = open(outListName, 'w')
    for f in block: jobfilelist.write(f+"\n")
    jobfilelist.close()

    if jobtype == "noTagAndProbe":
        cmsRun = "cmsRun "+options.objType+"_noTagAndProbe.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" globalTag="+globalTag+" >& "+outLogName
    if jobtype == "noTagAndProbeMT":
        cmsRun = "cmsRun "+options.objType+"_noTagAndProbe_multipleTaus.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" globalTag="+globalTag+" >& "+outLogName

    if jobtype == "noTagAndProbeAOD":
        cmsRun = "cmsRun "+options.objType+"_noTagAndProbe_AOD.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" globalTag="+globalTag+" >& "+outLogName

    if jobtype == "tagAndProbe":
        if run == "Run3": cmsRun = "cmsRun "+options.objType+"_tagAndProbeRun3.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" JSONfile="+JSONfile+" globalTag="+globalTag+" >& "+outLogName
        if run == "Run2": cmsRun = "cmsRun "+options.objType+"_tagAndProbeRun2.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" JSONfile="+JSONfile+" globalTag="+globalTag+" >& "+outLogName

    if jobtype == "reEmulL1_zeroBias":
        cmsRun = "cmsRun reEmulL1_zeroBias.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" caloParams="+caloParams+" globalTag="+globalTag+" allBXs="+allBXs+" >& "+outLogName

    if jobtype == "reEmulL1_MC":
        cmsRun = "cmsRun reEmulL1_MC.py maxEvents=-1 inputFiles_load="+outListName+" outputFile="+outRootName+" caloParams="+caloParams+" globalTag="+globalTag+" >& "+outLogName

    if jobtype == "AOD2MINIAOD":
        cmsRun = "cmsRun "+options.objType+"_AOD2MINIAOD.py maxEvents=8000 inputFiles_load="+outListName+" outputFile="+outRootName+" >& "+outLogName

    skimjob = open (outJobName, 'w')
    skimjob.write ('#!/bin/bash\n')
    skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
    skimjob.write ('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
    skimjob.write ('cd %s\n' % os.getcwd())
    skimjob.write ('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    skimjob.write ('eval `scram r -sh`\n')
    skimjob.write ('cd %s\n'%os.getcwd())
    skimjob.write (cmsRun+'\n')
    skimjob.close ()

    os.system ('chmod u+rwx ' + outJobName)
    command = ('/home/llr/cms/'+user+'/t3submit -'+queue+' \'' + outJobName +"\'")
    print(command)
    if not options.no_exec: os.system (command)
    # break

