from DataFormats.FWLite import Events, Handle
from collections import OrderedDict

handles = OrderedDict()
handles['genp'   ] = ('genParticles', Handle('std::vector<reco::GenParticle>'))
handles['genInfo'] = ('generator'   , Handle('GenEventInfoProduct'           ))

events = Events('TSG-Phase2Spring23GS-00135.root')


for i, event in enumerate(events):

    if (i+1)>2:
        break
    
    for k, v in handles.items():
        event.getByLabel(v[0], v[1])
        setattr(event, k, v[1].product())

        for ev in event.genp:
            print(ev.pdgId())
