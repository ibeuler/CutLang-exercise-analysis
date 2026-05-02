# Run the command

locationlist = [
    "root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/user/egramsta/mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.noskim.root",
    "root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/opendata/ODEO_FEB2025_v0_1LMET30_mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.1LMET30.root"]
CLA locationlist[0] ATLASODV3 -i analysis_V9_ttbar.adl

# 1:
# - **ttbar noSkim**
#  - **File location:** `root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/user/egramsta/mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.noskim.root`
#  - **Events:** 32M
#  - Bütün olayları içeren dosya, analiz nesneleri üzerine herhangi ilave filtre yok.

# 2:
# - **ttbar 1LMET30 skim**
#  - File location:`root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/opendata/ODEO_FEB2025_v0_1LMET30_mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.1LMET30.root`
#  - **Events:** 17M
#  - En az 1 lepton ve MET > 30 GeV şartlarını sağlayan olaylar.
#  - Bu dosyaları IU-CutLang cernbox alanımıza da koydum (ATLAS-OpenData-2025-Samples içerisinde)