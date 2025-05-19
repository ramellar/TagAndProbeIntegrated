import ROOT
from DataFormats.FWLite import Events, Handle

# Load the ROOT file
events = Events("50e6fec5-e3ea-4ce5-9dfd-b2e56b7fb35b.root")

# Handle for slimmedTaus
tauHandle = Handle("std::vector<pat::Tau>")
tauLabel = ("slimmedTaus", "", "PAT")


# Loop over events
for event in events:
    event.getByLabel(tauLabel, tauHandle)
    taus = tauHandle.product()
    for tau in taus:
        dir(tau)
	print(f"Tau pt: {tau.pt()}, eta: {tau.eta()}, phi: {tau.phi()}")
        print(f"Decay Mode: {tau.decayMode()}")
        # print(f"Isolation: {tau.tauID('byLooseIsolationMVArun2v1DBoldDMwLT')}")
