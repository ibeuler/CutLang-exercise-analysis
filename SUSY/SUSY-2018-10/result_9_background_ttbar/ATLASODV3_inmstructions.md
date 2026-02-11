# ATLAS Open Data 2025 release instructions

## ttbar samples

- **ttbar noSkim**
  - **File location:** `root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/user/egramsta/mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.noskim.root`
  - **Events:** 32M
  - Bütün olayları içeren dosya, analiz nesneleri üzerine herhangi ilave filtre yok.

- **ttbar 1LMET30 skim**
  - **File location:** `root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/opendata/ODEO_FEB2025_v0_1LMET30_mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.1LMET30.root`
  - **Events:** 17M
  - En az 1 lepton ve MET > 30 GeV şartlarını sağlayan olaylar.
  - Bu dosyaları IU-CutLang cernbox alanımıza da koydum (ATLAS-OpenData-2025-Samples içerisinde)

## Notes

- Bu dosyalar doğrudan CutLang'in link okuma fonksiyonu ile kullanılabilir.
- **Metadata information:**

```text
{'dataset_number': '410470', 'physics_short': 'PhPy8EG_A14_ttbar_hdamp258p75_nonallhad', 'e_tag': 'e6337', 'cross_section_pb': 729.77, 'genFiltEff': 0.5437965, 'kFactor': 1.139756362, 'nEvents': 32890000, 'sumOfWeights': 24014984445.816772, 'sumOfWeightsSquared': 17816963736313.004, 'process': 'ttbar', 'generator': 'Powheg+Pythia8(v8.230)+EvtGen(v1.6.0)', 'keywords': ['SM', 'lepton', 'top', 'ttbar'], 'description': "POWHEG+Pythia8 ttbar production with Powheg hdamp equal 1.5*top mass, A14 tune, at least one lepton filter, ME NNPDF30 NLO, A14 NNPDF23 LO from DSID 410450 LHE files with Shower Weights added '", 'job_path': 'https://gitlab.cern.ch/atlas-physics/pmg/infrastructure/mc15joboptions/-/tree/master/share/DSID410xxx/MC15.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.py', 'CoMEnergy': None, 'GenEvents': None, 'GenTune': None, 'PDF': None, 'Release': None, 'Filters': None, 'cross_section_uncertainty': None, 'hepmc_version': None, 'release': {'name': '2025e-13tev-beta'}}
```

## Running with CutLang

- Öncelikle git'ten en güncel versiyonu çekmelisiniz: `git pull`
- Ardından sırasıyla `make clean` ve `make` adımları ile temiz compile yapmalısınız.

ATLASODR2 yerine **ATLASODV3** ile çalıştırıyoruz.

**Örnek komut:**

```bash
./CLA.sh root://eospublic.cern.ch:1094//eos/opendata/atlas/rucio/user/egramsta/mc_410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.noskim.root ATLASODV3 -i ATLAS-SUSY-2018-10_Ahmetcan.adl -e 1000
```

- İlk başta az sayıda olay üzerinden çalıştırıp herhangi bir problem olup olmadığı kontrol edebilirsiniz.
- İnternet hızınıza bağlı olarak başlaması biraz vakit alabilir.
- İsterseniz `xrdcp` (xrootd paketine ihtiyacınız var) ile bu dosyaları kendi sisteminize indirebilirsiniz.
  - noSkim: 15 GB
  - 1LMET30: 8.5 GB

## ADL weights

ADL dosyasında weight ifadesinin tanımı öncekine göre biraz farklı. Aşağıdaki satırları kullanabilirsiniz:

```adl
define Sfactor : ScaleFactor_PILEUP * ScaleFactor_BTAG * ScaleFactor_JVT * ScaleFactor_ELE * ScaleFactor_MUON
define Lumi : 139000 # 139 fb-1

define totweight : xsec * kfac * filteff * mcWeight * Sfactor * Lumi / sum_of_weights

define totweightAuto : HSTEP(channelNumber < 310000) * 1 + HSTEP(channelNumber > 310000) * totweight
# For data, total weight = 1
```

## Finding datasets with `atlasopenmagic`

Artık eskisi gibi doğrudan web sitesi üzerinden data ve MC dosyalarını bulamıyoruz. Bunun yerine `atlasopenmagic` paketi ile verisetlerine dair bilgileri ve linkleri görebileceğimiz paketi kullanmamız gerekiyor.

- Docs: https://opendata.atlas.cern/docs/atlasopenmagic

Adımlar:

1. `pip install atlasopenmagic`
2. Jupyter notebook veya python interaktif session açın
3. `import atlasopenmagic as atom`
4. `atom.available_releases()` → var olan releaseleri gösterir
5. `atom.set_release("2025e-13tev-beta")` → 2025 education setini seçiyoruz
6. `atom.available_keywords()` → anahtar kelimeleri yazdırır (W, Z, ttbar, bsm...)
   - `atom.match_metadata(field='keywords', value='ttbar')` → ttbar içeren örnekleri gösterir
7. `atom.available_datasets()` → dataset ID (DSID)'leri yazdırır
   - `atom.get_metadata("410470")` → belirli datasete ait metadata bilgileri
   - `atom.get_urls("410470")` → istediğimiz datasetin url bilgisi
   - `atom.get_urls("410470", "1lep")` → istediğimiz skim'deki datasetin url'si

Available skims: `1LMET30`, `2J2LMET30`, `2bjets`, `2muons`, `2to4lep`, `3J1LMET30`, `3lep`, `4lep`, `GamGam`, `exactly3lep`, `exactly4lep`, `noskim`

## Exercise

Ben sizin için doğrudan ttbar olaylarının linkini en üstte verdim. Yazdığım adımları kullanarak Z+jets MC örneklerini de bulup run etmeye çalışalım. Takıldığınız yerde yardımcı olurum.

## Özet yapılacak listesi

1. Eğer henüz yapmadıysanız, adl dosyalarınıza analizde kullanılan histogramları tanımlamanız lazım: `meff`, `MET/sqrt(HT)` gibi. Doğrudan makaleye veya hepdata sayfasına bakabilirsiniz.
2. SUSY-2018-10 ve SUSY-2018-22 analizleri için yazdığınız `.adl`'ler, ttbar background örneği üzerinde çalıştırılacak.
   - weight ifadesini yukarıda paylaştığım gibi değiştirmeniz gerekiyor
3. Sinyal ve background için elde ettiğiniz `histoOut-*` dosyalarındaki histogramlar aynı grafik üzerinde çizdirilecek.
   - Daha önceki opendata analizlerinde yaptığınız şeyin aynısı, sadece bu sefer tek bir background ve tek bir sinyaliniz olacak.
