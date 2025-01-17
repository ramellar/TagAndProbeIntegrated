import FWCore.ParameterSet.Config as cms

print("Running on MC")


HLTLIST = cms.VPSet(
    cms.PSet (
        HLT = cms.string("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu16erL1f0L2f10QL3f17QL3trkIsoFiltered0p09", "hltOverlapFilterSingleIsoMu17LooseIsoPFTau20"),
        path2 = cms.vstring ("hltPFTau20TrackLooseIsoAgainstMuon", "hltOverlapFilterSingleIsoMu17LooseIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    )
)



# filter HLT paths for T&P
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = ['HLT_IsoMu18_v5'],
    andOr = cms.bool(True), # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(True) #if True: throws exception if a trigger path is invalid
)

## good taus - apply analysis selection
goodTaus = cms.EDFilter("PATTauRefSelector",
        src = cms.InputTag("slimmedTaus"),
        cut = cms.string(
                'pt > 20 && abs(eta) < 2.1 ' #kinematics
                '&& abs(charge) > 0 && abs(charge) < 2 ' #sometimes 2 prongs have charge != 1
                '&& tauID("decayModeFinding") > 0.5 ' # tau ID
                '&& tauID("byMediumDeepTau2017v2p1VSjet") > 0.5 ' # anti-Jet medium
                
                # to be used for VBFHToTauTau and similar datasets
                # '&& tauID("byMediumDeepTau2017v2p1VSmu") > 0.5 ' # anti-Muon medium
                # '&& tauID("byLooseDeepTau2017v2p1VSe") > 0.5 ' # anti-Ele loose

                # to be used for DYLL and similar datasets
                '&& tauID("byTightDeepTau2017v2p1VSmu") > 0.5 ' # anti-Muon tight
                '&& tauID("byTightDeepTau2017v2p1VSe") > 0.5 ' # anti-Ele tight
        ),
        filter = cms.bool(True)
)

genMatchedTaus = cms.EDFilter("genMatchTauFilter",
    taus = cms.InputTag("goodTaus")
)

Ntuplizer_noTagAndProbe = cms.EDAnalyzer("TauNtuplizer_noTagAndProbe",
    treeName = cms.string("TagAndProbe"),
    genCollection = cms.InputTag("generator"),
    taus  = cms.InputTag("genMatchedTaus"),
    triggerSet = cms.InputTag("slimmedPatTrigger"),
    triggerResultsLabel = cms.InputTag("TriggerResults", "", "HLT"),
    L1Tau = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
    L1EmuTau = cms.InputTag("simCaloStage2Digis", "MP"),
    jetCollection = cms.InputTag("slimmedJets"),
    l1tJetCollection = cms.InputTag("caloStage2Digis","Jet"),
    Vertexes = cms.InputTag("offlineSlimmedPrimaryVertices"),
    triggerList = HLTLIST,
    L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "TEST"),
    L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "TEST")   
)

TAndPseq = cms.Sequence( 
    goodTaus       +
    genMatchedTaus 
)

NtupleSeq = cms.Sequence(
    Ntuplizer_noTagAndProbe
)
