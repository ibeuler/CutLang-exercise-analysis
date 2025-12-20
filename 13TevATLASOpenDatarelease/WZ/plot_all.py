import ROOT
import optparse

parser = optparse.OptionParser()

parser.add_option('-a', '--analysis', dest = 'analysis_name',
                  help = 'name of the analysis for plotting:\n Zboson, Wboson, Singletop, Zboosted, HZZ, ZZdiboson, WZ, ttbar, SUSY, HWW, Ztau') 
(options, args) = parser.parse_args()

analysis_name = options.analysis_name


def plotting(region_name, hist_name, max_range):
    scale_log = True

    region_name = str(region_name)
    hist_name = str(hist_name)

    if analysis_name == "Zboosted":
        datafile = ROOT.TFile("histoOut-dataall.root","READ")
        stopfile = ROOT.TFile("histoOut-stop.root","READ")
        Vfile = ROOT.TFile("histoOut-V.root","READ")
        dibosonfile = ROOT.TFile("histoOut-diboson.root","READ")
        ttbarfile = ROOT.TFile("histoOut-ttbar.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        Vcutflow = Vfile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name,hist_name))
        Vhist = Vfile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name,hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name,hist_name))

        ## Overflow
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))

        n_bins_V = Vhist.GetNbinsX()
        Vhist.AddBinContent(n_bins_V, Vhist.GetBinContent(n_bins_V + 1))

        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))
    
    elif analysis_name == "HZZ":
        datafile = ROOT.TFile("data.root","READ")
        sigfile = ROOT.TFile("Higgs.root","READ")
        othersfile = ROOT.TFile("V.root","READ")
        ZZfile = ROOT.TFile("Z_Z.root","READ")
        #SMfile = ROOT.TFile("histoOut-allSM.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        sigcutflow = sigfile.Get("{}/cutflow".format(region_name))
        otherscutflow = othersfile.Get("{}/cutflow".format(region_name))
        ZZcutflow = ZZfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        sighist = sigfile.Get("{}/{}".format(region_name,hist_name))
        othershist = othersfile.Get("{}/{}".format(region_name,hist_name))
        ZZhist = ZZfile.Get("{}/{}".format(region_name,hist_name))
        #SMhist = SMfile.Get("{}/{}".format(region_name,hist_name))
        ## Overflow
        n_bins_sig = sighist.GetNbinsX()
        sighist.AddBinContent(n_bins_sig, sighist.GetBinContent(n_bins_sig + 1))

        n_bins_others = othershist.GetNbinsX()
        othershist.AddBinContent(n_bins_others, othershist.GetBinContent(n_bins_others + 1))

        n_bins_ZZ = ZZhist.GetNbinsX()
        ZZhist.AddBinContent(n_bins_ZZ, ZZhist.GetBinContent(n_bins_ZZ + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "Zboson":
        datafile = ROOT.TFile("data.root","READ")
        Zfile = ROOT.TFile("zjets.root","READ")
        Wfile = ROOT.TFile("wjets.root","READ")
        stopfile = ROOT.TFile("mc_single_top.root","READ")
        ttbarfile = ROOT.TFile("ttbar.root","READ")
        dibosonfile = ROOT.TFile("diboson.root","READ")
        #SMfile = ROOT.TFile("histoOut-allSM.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        Zcutflow = Zfile.Get("{}/cutflow".format(region_name))
        Wcutflow = Wfile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        Zhist = Zfile.Get("{}/{}".format(region_name,hist_name))
        Whist = Wfile.Get("{}/{}".format(region_name,hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name,hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name,hist_name))
        #SMhist = SMfile.Get("{}/{}".format(region_name,hist_name))
        ## Overflow
        n_bins_Z = Zhist.GetNbinsX()
        Zhist.AddBinContent(n_bins_Z, Zhist.GetBinContent(n_bins_Z + 1))

        n_bins_W = Whist.GetNbinsX()
        Whist.AddBinContent(n_bins_W, Whist.GetBinContent(n_bins_W + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))
        
        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))
        
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))
    
    elif analysis_name == "Wboson":
        datafile = ROOT.TFile("histoOut-dataall.root","READ")
        stopfile = ROOT.TFile("histoOut-stopall.root","READ")
        dibosonfile = ROOT.TFile("histoOut-dibosonall.root","READ")
        zfile = ROOT.TFile("histoOut-Zll.root","READ")
        ttbarfile = ROOT.TFile("histoOut-ttbar.root","READ")
        wjetsfile = ROOT.TFile("histoOut-wjetsall.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))
        wjetscutflow = wjetsfile.Get("{}/cutflow".format(region_name))
        zcutflow = zfile.Get("{}/cutflow".format(region_name))
         
        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name,hist_name))
        zhist = zfile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name,hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name,hist_name))
        wjetshist = wjetsfile.Get("{}/{}".format(region_name,hist_name))
        
        ## Overflow
        n_bins_Z = zhist.GetNbinsX()
        zhist.AddBinContent(n_bins_Z, zhist.GetBinContent(n_bins_Z + 1))

        n_bins_W = wjetshist.GetNbinsX()
        wjetshist.AddBinContent(n_bins_W, wjetshist.GetBinContent(n_bins_W + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))
        
        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))
        
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "Singletop":
        datafile = ROOT.TFile("histoOut-dataall.root","READ")
        stopfile = ROOT.TFile("histoOut-stop_t.root","READ")
        dibosonfile = ROOT.TFile("histoOut-ZVV.root","READ")
        ttbarfile = ROOT.TFile("histoOut-tWtb.root","READ")
        wjetsfile = ROOT.TFile("histoOut-wjetsall.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))
        wjetscutflow = wjetsfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name,hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name,hist_name))
        wjetshist = wjetsfile.Get("{}/{}".format(region_name,hist_name))
        
        ## Overflow
        n_bins_W = wjetshist.GetNbinsX()
        wjetshist.AddBinContent(n_bins_W, wjetshist.GetBinContent(n_bins_W + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))
        
        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))
        
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))
    
    elif analysis_name == "ZZdiboson":
        datafile = ROOT.TFile("data.root","READ")
        topVfile = ROOT.TFile("topV.root","READ")
        WWZfile = ROOT.TFile("WWZ.root","READ")
        Z_Zfile = ROOT.TFile("Z_Z.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        topVcutflow = topVfile.Get("{}/cutflow".format(region_name))
        WWZcutflow = WWZfile.Get("{}/cutflow".format(region_name))
        Z_Zcutflow = Z_Zfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        topVhist = topVfile.Get("{}/{}".format(region_name,hist_name))
        WWZhist = WWZfile.Get("{}/{}".format(region_name,hist_name))
        Z_Zhist = Z_Zfile.Get("{}/{}".format(region_name,hist_name))
        
        ## Overflow
        n_bins_topV = topVhist.GetNbinsX()
        topVhist.AddBinContent(n_bins_topV, topVhist.GetBinContent(n_bins_topV + 1))

        n_bins_WWZ = WWZhist.GetNbinsX()
        WWZhist.AddBinContent(n_bins_WWZ, WWZhist.GetBinContent(n_bins_WWZ + 1))
        
        n_bins_ZZ = Z_Zhist.GetNbinsX()
        Z_Zhist.AddBinContent(n_bins_ZZ, Z_Zhist.GetBinContent(n_bins_ZZ + 1))
        
        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "WZ":
        datafile = ROOT.TFile("data.root","READ")
        Vfile = ROOT.TFile("V.root","READ")
        VVfile = ROOT.TFile("VV.root","READ")
        topfile = ROOT.TFile("top.root","READ")
        WZfile = ROOT.TFile("WZ.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        Vcutflow = Vfile.Get("{}/cutflow".format(region_name))
        VVcutflow = VVfile.Get("{}/cutflow".format(region_name))
        topcutflow = topfile.Get("{}/cutflow".format(region_name))
        WZcutflow = WZfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        Vhist = Vfile.Get("{}/{}".format(region_name,hist_name))
        VVhist = VVfile.Get("{}/{}".format(region_name,hist_name))
        tophist = topfile.Get("{}/{}".format(region_name,hist_name))
        WZhist = WZfile.Get("{}/{}".format(region_name,hist_name))

        ## Overflow
        n_bins_V = Vhist.GetNbinsX()
        Vhist.AddBinContent(n_bins_V, Vhist.GetBinContent(n_bins_V + 1))

        n_bins_VV = VVhist.GetNbinsX()
        VVhist.AddBinContent(n_bins_VV, VVhist.GetBinContent(n_bins_VV + 1))
        
        n_bins_top = tophist.GetNbinsX()
        tophist.AddBinContent(n_bins_top, tophist.GetBinContent(n_bins_top + 1))
        
        n_bins_WZ = WZhist.GetNbinsX()
        WZhist.AddBinContent(n_bins_WZ, WZhist.GetBinContent(n_bins_WZ + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "ttbar":
        datafile = ROOT.TFile("data.root","READ")
        dibosonfile = ROOT.TFile("histoOut-diboson.root", "READ")
        stopfile = ROOT.TFile("histoOut-stop.root", "READ")
        Vfile = ROOT.TFile("histoOut-V.root", "READ")
        ttbarfile = ROOT.TFile("histoOut-ttbar.root", "READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        Vcutflow = Vfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name, hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name, hist_name))
        Vhist = Vfile.Get("{}/{}".format(region_name, hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name, hist_name))
        
        ## Overflow
        n_bins_V = Vhist.GetNbinsX()
        Vhist.AddBinContent(n_bins_V, Vhist.GetBinContent(n_bins_V + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))
        
        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))
        
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "SUSY":
        datafile = ROOT.TFile("data.root","READ")
        dibosonfile = ROOT.TFile("diboson.root","READ")
        Wfile = ROOT.TFile("W.root","READ")
        Zfile = ROOT.TFile("Z.root","READ")
        ttbarfile = ROOT.TFile("ttbar.root","READ")
        stopfile = ROOT.TFile("stop.root","READ")
        susyfile = ROOT.TFile("susy-signal.root","READ")
        
        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))
        Zcutflow = Zfile.Get("{}/cutflow".format(region_name))
        Wcutflow = Wfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))
        susycutflow = susyfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name,hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name, hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name, hist_name))
        Zhist = Zfile.Get("{}/{}".format(region_name, hist_name))
        Whist = Wfile.Get("{}/{}".format(region_name, hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name, hist_name))
        susyhist = susyfile.Get("{}/{}".format(region_name, hist_name))

        ## Overflow
        n_bins_W = Whist.GetNbinsX()
        Whist.AddBinContent(n_bins_W, Whist.GetBinContent(n_bins_W + 1))
        
        n_bins_Z = Zhist.GetNbinsX()
        Zhist.AddBinContent(n_bins_Z, Zhist.GetBinContent(n_bins_Z + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))
        
        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))
        
        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))

    elif analysis_name == "HWW":
        datafile = ROOT.TFile("data.root","READ")
        higgsfile = ROOT.TFile("higgs.root","READ")
        ttbarfile = ROOT.TFile("ttbar.root","READ")
        dibosonfile = ROOT.TFile("diboson.root","READ")
        Vfile = ROOT.TFile("V.root","READ")
        stopfile = ROOT.TFile("stop.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        higgscutflow = higgsfile.Get("{}/cutflow".format(region_name))
        ttbarcutflow = ttbarfile.Get("{}/cutflow".format(region_name))
        dibosoncutflow = dibosonfile.Get("{}/cutflow".format(region_name))
        Vcutflow = Vfile.Get("{}/cutflow".format(region_name))
        stopcutflow = stopfile.Get("{}/cutflow".format(region_name))

        datahist = datafile.Get("{}/{}".format(region_name, hist_name))
        higgshist = higgsfile.Get("{}/{}".format(region_name, hist_name))
        ttbarhist = ttbarfile.Get("{}/{}".format(region_name, hist_name))
        dibosonhist = dibosonfile.Get("{}/{}".format(region_name, hist_name))
        Vhist = Vfile.Get("{}/{}".format(region_name, hist_name))
        stophist = stopfile.Get("{}/{}".format(region_name, hist_name))

        ## Overflow
        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))
        
        n_bins_higgs = higgshist.GetNbinsX()
        higgshist.AddBinContent(n_bins_higgs, higgshist.GetBinContent(n_bins_higgs + 1))

        n_bins_ttbar = ttbarhist.GetNbinsX()
        ttbarhist.AddBinContent(n_bins_ttbar, ttbarhist.GetBinContent(n_bins_ttbar + 1))

        n_bins_diboson = dibosonhist.GetNbinsX()
        dibosonhist.AddBinContent(n_bins_diboson, dibosonhist.GetBinContent(n_bins_diboson + 1))

        n_bins_V = Vhist.GetNbinsX()
        Vhist.AddBinContent(n_bins_V, Vhist.GetBinContent(n_bins_V + 1))

        n_bins_stop = stophist.GetNbinsX()
        stophist.AddBinContent(n_bins_stop, stophist.GetBinContent(n_bins_stop + 1))

    elif analysis_name == "Ztau":
        datafile = ROOT.TFile("data.root","READ")
        topVfile = ROOT.TFile("topV.root","READ")
        Wfile = ROOT.TFile("W.root","READ")
        Zfile = ROOT.TFile("Z.root","READ")
        Ztaufile = ROOT.TFile("Ztau.root","READ")

        datacutflow = datafile.Get("{}/cutflow".format(region_name))
        topVcutflow = topVfile.Get("{}/cutflow".format(region_name))
        Wcutflow = Wfile.Get("{}/cutflow".format(region_name))
        Zcutflow = Zfile.Get("{}/cutflow".format(region_name))
        Ztaucutflow = Ztaufile.Get("{}/cutflow".format(region_name))
        
        datahist = datafile.Get("{}/{}".format(region_name, hist_name))
        topVhist = topVfile.Get("{}/{}".format(region_name, hist_name))
        Whist = Wfile.Get("{}/{}".format(region_name, hist_name))
        Zhist = Zfile.Get("{}/{}".format(region_name, hist_name))
        Ztauhist = Ztaufile.Get("{}/{}".format(region_name, hist_name))

        ## Overflow
        n_bins_data = datahist.GetNbinsX()
        datahist.AddBinContent(n_bins_data, datahist.GetBinContent(n_bins_data + 1))


        n_bins_topV = topVhist.GetNbinsX()
        topVhist.AddBinContent(n_bins_topV, topVhist.GetBinContent(n_bins_topV + 1))

        n_bins_W = Whist.GetNbinsX()
        Whist.AddBinContent(n_bins_W, Whist.GetBinContent(n_bins_W + 1))

        n_bins_Z = Zhist.GetNbinsX()
        Zhist.AddBinContent(n_bins_Z, Zhist.GetBinContent(n_bins_Z + 1))

        n_bins_Ztau = Ztauhist.GetNbinsX()
        Ztauhist.AddBinContent(n_bins_Ztau, Ztauhist.GetBinContent(n_bins_Ztau + 1))

    ### hist title
    max_range = float(max_range)

    hist_title = datahist.GetXaxis().GetTitle()

    ROOT.gROOT.SetStyle("ATLAS")
    ROOT.gROOT.ForceStyle()

    hs = ROOT.THStack("hs",datahist.GetTitle())
    if analysis_name == "Zboosted":
        dibosonhist.SetFillColor(ROOT.kBlue-6)
        dibosonhist.SetLineColor(ROOT.kBlack)
        Vhist.SetFillColor(ROOT.kGreen-3)
        stophist.SetFillColor(ROOT.kAzure+8)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        if "hlead" not in hist_name:
            ttbarhist.Scale(0.91)
        hs.Add(dibosonhist)
        hs.Add(stophist)
        hs.Add(Vhist)
        hs.Add(ttbarhist)

    elif analysis_name == "HZZ":
        othershist.SetFillColor(ROOT.kBlue-6)
        othershist.SetLineColor(ROOT.kBlack)
        sighist.SetFillColor(ROOT.kRed)
        sighist.SetLineColor(ROOT.kBlack)
        ZZhist.SetFillColor(ROOT.kAzure+8)
        ZZhist.Scale(1.3)
        hs.Add(othershist)
        hs.Add(ZZhist)
        hs.Add(sighist)
    elif analysis_name == "Zboson":
        Zhist.SetFillColor(ROOT.kPink+9)
        Whist.SetFillColor(ROOT.kGreen-3)
        stophist.SetFillColor(ROOT.kAzure+8)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        dibosonhist.SetFillColor(ROOT.kBlue-6)
        hs.Add(Whist)
        hs.Add(stophist)
        hs.Add(ttbarhist)
        hs.Add(dibosonhist)
        hs.Add(Zhist)
    
    elif analysis_name == "Wboson":
        dibosonhist.SetFillColor(ROOT.kBlue-6)
        dibosonhist.SetLineColor(ROOT.kBlack)
        stophist.SetFillColor(ROOT.kAzure+8)
        stophist.SetLineColor(ROOT.kBlack)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        wjetshist.SetFillColor(ROOT.kGreen-3)
        zhist.SetFillColor(ROOT.kPink+9)
        #wjetshist.Scale(1.1)
        hs.Add(stophist)
        hs.Add(ttbarhist)
        hs.Add(dibosonhist)
        hs.Add(zhist)
        hs.Add(wjetshist)

    elif analysis_name == "Singletop":
        dibosonhist.SetFillColor(ROOT.kPink)
        dibosonhist.SetLineColor(ROOT.kBlack)
        stophist.SetFillColor(ROOT.kAzure+8)
        stophist.SetLineColor(ROOT.kBlack)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        wjetshist.SetFillColor(ROOT.kGreen)
        wjetshist.Scale(1.1)
        hs.Add(dibosonhist)
        hs.Add(wjetshist)
        hs.Add(ttbarhist)
        hs.Add(stophist)

    elif analysis_name == "ZZdiboson":
        WWZhist.SetFillColor(ROOT.kRed-7)
        WWZhist.SetLineColor(ROOT.kBlack)
        topVhist.SetFillColor(ROOT.kGreen-3)
        Z_Zhist.SetFillColor(ROOT.kBlue-6)
        #Z_Zhist.Scale(0.91)
        hs.Add(topVhist)
        hs.Add(WWZhist)
        hs.Add(Z_Zhist)
        hs.SetMinimum(0)
    
    elif analysis_name == "WZ":
        Vhist.SetFillColor(ROOT.kGreen-3)
        Vhist.SetLineColor(ROOT.kBlack)
        VVhist.SetFillColor(ROOT.kBlue-6)
        tophist.SetFillColor(ROOT.kOrange-3)
        WZhist.SetFillColor(ROOT.kRed-7)
        hs.Add(tophist)
        hs.Add(Vhist)
        hs.Add(VVhist)
        hs.Add(WZhist)
        hs.SetMinimum(0)

    elif analysis_name == "ttbar":
        Vhist.SetFillColor(ROOT.kGreen - 3)
        Vhist.SetLineColor(ROOT.kBlack)
        dibosonhist.SetFillColor(ROOT.kBlue - 6)
        stophist.SetFillColor(ROOT.kAzure + 8)
        ttbarhist.SetFillColor(ROOT.kOrange -3)
        hs.Add(dibosonhist)
        hs.Add(stophist)
        hs.Add(Vhist)
        hs.Add(ttbarhist)

    elif analysis_name == "SUSY":
        dibosonhist.SetFillColor(ROOT.kBlue-6)
        Whist.SetFillColor(ROOT.kGreen-3)
        Zhist.SetFillColor(ROOT.kPink+9)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        stophist.SetFillColor(ROOT.kAzure+8)
        hs.Add(Whist)
        hs.Add(stophist)
        hs.Add(ttbarhist)
        hs.Add(dibosonhist)
        hs.Add(Zhist)

    elif analysis_name == "HWW":
        higgshist.SetFillColor(ROOT.kRed)
        ttbarhist.SetFillColor(ROOT.kOrange-3)
        dibosonhist.Scale(1.3)
        dibosonhist.SetFillColor(ROOT.kBlue-6)
        Vhist.SetFillColor(ROOT.kGreen-3)
        stophist.SetFillColor(ROOT.kAzure+8)
        
        hs.Add(stophist)
        hs.Add(ttbarhist)
        hs.Add(Vhist)
        hs.Add(dibosonhist)
        hs.Add(higgshist)

    elif analysis_name == "Ztau":
        topVhist.SetFillColor(ROOT.kOrange-3)
        Whist.SetFillColor(ROOT.kGreen-3)
        Zhist.SetFillColor(ROOT.kPink+9)
        Ztauhist.SetFillColor(ROOT.kAzure+7)

        hs.Add(topVhist)
        hs.Add(Whist)
        hs.Add(Zhist)
        hs.Add(Ztauhist)

    if analysis_name == "Zboson" or analysis_name == "SUSY" or (analysis_name == "ttbar" and hist_name != "hist_Topmass"):
        hs.SetMinimum(1e-1)
    else:
        hs.SetMinimum(0)
    hs.SetMaximum(max_range)
    c1 = ROOT.TCanvas("c1","stack plot",100,100,800,700)
    c1.cd()
    #c1.SetLogy()
    datahist.SetLineColor(ROOT.kBlack)
    datahist.SetMarkerStyle(20)

    #### stack for ratio
    if analysis_name == "Zboosted":
        rstack = ttbarhist.Clone()
        rstack.Add(stophist)
        rstack.Add(dibosonhist)
        rstack.Add(Vhist)

    elif analysis_name == "HZZ":
        rstack = othershist.Clone()
        rstack.Add(othershist)
        rstack.Add(sighist)
        rstack.Add(ZZhist)
    
    elif analysis_name == "Zboson":
        rstack = ttbarhist.Clone()
        rstack.Add(Zhist)
        rstack.Add(dibosonhist)
        rstack.Add(Whist)
        rstack.Add(stophist)
    
    elif analysis_name == "Wboson":
        rstack = ttbarhist.Clone()
        rstack.Add(zhist)
        rstack.Add(dibosonhist)
        rstack.Add(wjetshist)
        rstack.Add(stophist)
    elif analysis_name == "Singletop":
        rstack = dibosonhist.Clone()
        rstack.Add(wjetshist)
        rstack.Add(stophist)
        rstack.Add(ttbarhist)
    elif analysis_name == "ZZdiboson":
        rstack = topVhist.Clone()
        rstack.Add(WWZhist)
        rstack.Add(Z_Zhist)
    elif analysis_name == "WZ":
        rstack = tophist.Clone()
        rstack.Add(Vhist)
        rstack.Add(VVhist)
        rstack.Add(WZhist)

    elif analysis_name == "ttbar":
        rstack = ttbarhist.Clone()
        rstack.Add(stophist)
        rstack.Add(dibosonhist)
        rstack.Add(Vhist)

    elif analysis_name == "SUSY":
        rstack = ttbarhist.Clone()
        rstack.Add(Zhist)
        rstack.Add(dibosonhist)
        rstack.Add(Whist)
        rstack.Add(stophist)

    elif analysis_name == "HWW":
        rstack = ttbarhist.Clone()
        rstack.Add(dibosonhist)
        rstack.Add(Vhist)
        rstack.Add(stophist)
        rstack.Add(higgshist)

    elif analysis_name == "Ztau":
        rstack = topVhist.Clone()
        rstack.Add(Whist)
        rstack.Add(Zhist)
        rstack.Add(Ztauhist)

    #### yieldlara hata eklemek lazım #####
    if analysis_name == "Zboson":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            Zyield = Zcutflow.GetBinContent(i)
            Wyield = Wcutflow.GetBinContent(i)
            ttbaryield = ttbarcutflow.GetBinContent(i)
            stopyield = stopcutflow.GetBinContent(i)
            dibosonyield = dibosoncutflow.GetBinContent(i)

        totalError_Z = 0
        totalError_W = 0
        totalError_ttbar = 0
        totalError_stop = 0
        totalError_diboson = 0
        
        for bin in range(1,dibosonhist.GetNbinsX() + 1):
            binError = dibosonhist.GetBinError(bin)
            totalError_diboson += binError**2

        for bin in range(1,Zhist.GetNbinsX() + 1):
            binError = Zhist.GetBinError(bin)
            totalError_Z += binError**2

        for bin in range(1,Whist.GetNbinsX() + 1):
            binError = Whist.GetBinError(bin)
            totalError_W += binError**2

        for bin in range(1,stophist.GetNbinsX() + 1):
            binError = stophist.GetBinError(bin)
            totalError_stop += binError**2
        
        for bin in range(1,ttbarhist.GetNbinsX() + 1):
            binError = ttbarhist.GetBinError(bin)
            totalError_ttbar += binError**2

        dibosonerror = totalError_diboson**0.5
        Zerror = totalError_Z**0.5
        Werror = totalError_W**0.5
        ttbarerror = totalError_ttbar**0.5
        stoperror = totalError_stop**0.5

        yielddata = datahist.Integral()
        yielddiboson = dibosonhist.Integral()
        yieldZ = Zhist.Integral()
        yieldW = Whist.Integral()
        yieldttbar = ttbarhist.Integral()
        yieldstop = stophist.Integral()

        datayieldstr = "DATA" #+ "  " + str(yielddata)
        dibosonyieldstr = "Diboson"# + "  " + str("{:.2f}".format(yielddiboson))
        Zyieldstr = "Z #rightarrow ll" #+ "  " + str("{:.2f}".format(yieldV))
        Wyieldstr = "W + jets" #+ "  " + str("{:.2f}".format(yieldV))
        ttbaryieldstr = "t#bar{t}" #+ "  " + str("{:.2f}".format(yieldttbar))
        stopyieldstr = "Single top" #+ "  " + str("{:.2f}".format(yieldttbar))

    elif analysis_name == "Wboson":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            stopyield = stopcutflow.GetBinContent(i)
            dibosonyield = dibosoncutflow.GetBinContent(i)
            ttbaryield = ttbarcutflow.GetBinContent(i)
            wjetsyield = wjetscutflow.GetBinContent(i)

        totalError_stop = 0
        totalError_diboson = 0
        totalError_ttbar = 0
        totalError_wjets = 0
        totalError_z = 0

        for bin in range(1,stophist.GetNbinsX() + 1):
            binError = stophist.GetBinError(bin)
            totalError_stop += binError**2

        for bin in range(1,dibosonhist.GetNbinsX() + 1):
            binError = dibosonhist.GetBinError(bin)
            totalError_diboson += binError**2

        for bin in range(1,ttbarhist.GetNbinsX() + 1):
            binError = ttbarhist.GetBinError(bin)
            totalError_ttbar += binError**2

        for bin in range(1,wjetshist.GetNbinsX() + 1):
            binError = wjetshist.GetBinError(bin)
            totalError_wjets += binError**2

        for bin in range(1,zhist.GetNbinsX() + 1):
            binError = zhist.GetBinError(bin)
            totalError_z += binError**2

        stoperror = totalError_stop**0.5
        dibosonerror = totalError_diboson**0.5
        ttbarerror = totalError_ttbar**0.5
        wjetserror = totalError_wjets**0.5
        zerror = totalError_z**0.5

        yielddata = datahist.Integral()
        yieldstop = stophist.Integral()
        yielddiboson = dibosonhist.Integral()
        yieldttbar = ttbarhist.Integral()
        yieldwjets = wjetshist.Integral()
        yieldz = zhist.Integral()

        datayieldstr = "DATA" # + "  " + str(yielddata)
        stopyieldstr = "Single top" # + "  " + str("{:.2f}".format(yieldstop))
        dibosonyieldstr = "Diboson" # + "  " + str("{:.2f}".format(yielddiboson))
        ttbaryieldstr = "t#bar{t}" # + "  " + str("{:.2f}".format(yieldttbar))
        wjetsyieldstr = "W + jets" # + "  " + str("{:.2f}".format(yieldwjets))
        zyieldstr = "Z + jets" # + " " +  str("{:.2f}".format(yieldz))

    elif analysis_name == "Singletop":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            stopyield = stopcutflow.GetBinContent(i)
            dibosonyield = dibosoncutflow.GetBinContent(i)
            ttbaryield = ttbarcutflow.GetBinContent(i)
            wjetsyield = wjetscutflow.GetBinContent(i)

        totalError_stop = 0
        totalError_diboson = 0
        totalError_ttbar = 0
        totalError_wjets = 0

        for bin in range(1,stophist.GetNbinsX() + 1):
            binError = stophist.GetBinError(bin)
            totalError_stop += binError**2

        for bin in range(1,dibosonhist.GetNbinsX() + 1):
            binError = dibosonhist.GetBinError(bin)
            totalError_diboson += binError**2

        for bin in range(1,ttbarhist.GetNbinsX() + 1):
            binError = ttbarhist.GetBinError(bin)
            totalError_ttbar += binError**2

        for bin in range(1,wjetshist.GetNbinsX() + 1):
            binError = wjetshist.GetBinError(bin)
            totalError_wjets += binError**2

        stoperror = totalError_stop**0.5
        dibosonerror = totalError_diboson**0.5
        ttbarerror = totalError_ttbar**0.5
        wjetserror = totalError_wjets**0.5

        yielddata = datahist.Integral()
        yieldstop = stophist.Integral()
        yielddiboson = dibosonhist.Integral()
        yieldttbar = ttbarhist.Integral()
        yieldwjets = wjetshist.Integral()

        datayieldstr = "DATA"# + "  " + str(yielddata)
        stopyieldstr = "tq"# + "  " + str("{:.2f}".format(yieldsig))
        dibosonyieldstr = "ZVV"# + "  " + str("{:.2f}".format(yielddiboson))
        ttbaryieldstr = "tt,Wt,tb"# + "  " + str("{:.2f}".format(yieldttbar))
        wjetsyieldstr = "W + jets"# + "  " + str("{:.2f}".format(yieldwjets))


    elif analysis_name == "Zboosted":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            dibosonyield = dibosoncutflow.GetBinContent(i)
            Vyield = Vcutflow.GetBinContent(i)
            ttbaryield = ttbarcutflow.GetBinContent(i)
            stopyield = stopcutflow.GetBinContent(i)

        totalError_diboson = 0
        totalError_V = 0
        totalError_ttbar = 0
        totalError_stop = 0

        for bin in range(1,dibosonhist.GetNbinsX() + 1):
            binError = dibosonhist.GetBinError(bin)
            totalError_diboson += binError**2

        for bin in range(1,Vhist.GetNbinsX() + 1):
            binError = Vhist.GetBinError(bin)
            totalError_V += binError**2

        for bin in range(1,ttbarhist.GetNbinsX() + 1):
            binError = ttbarhist.GetBinError(bin)
            totalError_ttbar += binError**2

        for bin in range(1,stophist.GetNbinsX() + 1):
            binError = stophist.GetBinError(bin)
            totalError_stop += binError**2

        dibosonerror = totalError_diboson**0.5
        Verror = totalError_V**0.5
        ttbarerror = totalError_ttbar**0.5
        stoperror = totalError_stop**0.5

        yielddata = datahist.Integral()
        yielddiboson = dibosonhist.Integral()
        yieldV = Vhist.Integral()
        yieldttbar = ttbarhist.Integral()
        yieldstop = stophist.Integral()

        datayieldstr = "DATA" #+ "  " + str(yielddata)
        dibosonyieldstr = "Diboson"# + "  " + str("{:.2f}".format(yielddiboson))
        Vyieldstr = "V + jets" #+ "  " + str("{:.2f}".format(yieldV))
        ttbaryieldstr = "ttbar" #+ "  " + str("{:.2f}".format(yieldttbar))
        stopyieldstr = "Single top" #+ "  " + str("{:.2f}".format(yieldstop))

    elif analysis_name == "HZZ":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            sigyield = sigcutflow.GetBinContent(i)
            othersyield = otherscutflow.GetBinContent(i)
            ZZyield = ZZcutflow.GetBinContent(i)

        totalError_sig = 0
        totalError_others = 0
        totalError_ZZ = 0

        for bin in range(1,sighist.GetNbinsX() + 1):
            binError = sighist.GetBinError(bin)
            totalError_sig += binError**2

        for bin in range(1,othershist.GetNbinsX() + 1):
            binError = othershist.GetBinError(bin)
            totalError_others += binError**2

        for bin in range(1,ZZhist.GetNbinsX() + 1):
            binError = ZZhist.GetBinError(bin)
            totalError_ZZ += binError**2

        sigerror = totalError_sig**0.5
        otherserror = totalError_others**0.5
        ZZerror = totalError_ZZ**0.5

        yieldsig = sighist.Integral()
        yieldZZ = ZZhist.Integral()
        yieldothers = othershist.Integral()
        yielddata = datahist.Integral()

        datayieldstr = "DATA" #+ "  " + str(yielddata)
        sigyieldstr = "Higgs" #+ "  " + str("{:.2f}".format(yieldsig))
        othersyieldstr = "Others"# + "  " + str("{:.2f}".format(yieldothers))
        ZZyieldstr = "ZZ" #+ "  " + str("{:.2f}".format(yieldZZ))
    
    elif analysis_name == "ZZdiboson":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            WWZyield = WWZcutflow.GetBinContent(i)
            Z_Zyield = Z_Zcutflow.GetBinContent(i)
            topVyield = topVcutflow.GetBinContent(i)

        totalError_WWZ = 0
        totalError_Z_Z = 0
        totalError_topV = 0

        for bin in range(1,WWZhist.GetNbinsX() + 1):
            binError = WWZhist.GetBinError(bin)
            totalError_WWZ += binError**2

        for bin in range(1,Z_Zhist.GetNbinsX() + 1):
            binError = Z_Zhist.GetBinError(bin)
            totalError_Z_Z += binError**2

        for bin in range(1,topVhist.GetNbinsX() + 1):
            binError = topVhist.GetBinError(bin)
            totalError_topV += binError**2

        WWZerror = totalError_WWZ**0.5
        Z_Zerror = totalError_Z_Z**0.5
        topVerror = totalError_topV**0.5

        yielddata = datahist.Integral()
        yieldWWZ = WWZhist.Integral()
        yieldZ_Z = Z_Zhist.Integral()
        yieldtopV = topVhist.Integral()

        datayieldstr = "DATA" #+ "  " + str(yielddata)
        WWZyieldstr = "WW, WZ" #+ "  " + str("{:.2f}".format(yieldWWZ))
        Z_Zyieldstr = "ZZ" #+ "  " + str("{:.2f}".format(yieldZ_Z))
        topVyieldstr = "Other"# + "  " + str("{:.2f}".format(yieldtopV))

    elif analysis_name == "WZ":
        for i in range(2,21,1):
            datayield = datacutflow.GetBinContent(i)
            Vyield = Vcutflow.GetBinContent(i)
            VVyield = VVcutflow.GetBinContent(i)
            topyield = topcutflow.GetBinContent(i)
            WZyield = topcutflow.GetBinContent(i)

        totalError_V = 0
        totalError_VV = 0
        totalError_top = 0
        totalError_WZ = 0

        for bin in range(1,Vhist.GetNbinsX() + 1):
            binError = Vhist.GetBinError(bin)
            totalError_V += binError**2

        for bin in range(1,VVhist.GetNbinsX() + 1):
            binError = VVhist.GetBinError(bin)
            totalError_VV += binError**2

        for bin in range(1,tophist.GetNbinsX() + 1):
            binError = tophist.GetBinError(bin)
            totalError_top += binError**2
        
        for bin in range(1,WZhist.GetNbinsX() + 1):
            binError = WZhist.GetBinError(bin)
            totalError_WZ += binError**2

        Verror = totalError_V**0.5
        VVerror = totalError_VV**0.5
        toperror = totalError_top**0.5
        WZerror = totalError_WZ**0.5

        yielddata = datahist.Integral()
        yieldV = Vhist.Integral()
        yieldVV = VVhist.Integral()
        yieldtop = tophist.Integral()
        yieldWZ = WZhist.Integral()

        datayieldstr = "DATA" #+ "  " + str(yielddata)
        Vyieldstr = "V" #+ "  " + str("{:.2f}".format(yieldWWZ))
        VVyieldstr = "ZZ,WW" #+ "  " + str("{:.2f}".format(yieldZ_Z))
        topyieldstr = "Other" #+ "  " + str("{:.2f}".format(yieldZ_Z))
        WZyieldstr = "WZ" #+ "  " + str("{:.2f}".format(yieldZ_Z))

    elif analysis_name == "ttbar":
        totalError_diboson = 0
        totalError_stop = 0
        totalError_V = 0
        totalError_ttbar = 0

        for bin in range(1, dibosonhist.GetNbinsX() + 1):
            binError = dibosonhist.GetBinError(bin)
            totalError_diboson += binError**2

        for bin in range(1, stophist.GetNbinsX() + 1):
            binError = stophist.GetBinError(bin)
            totalError_stop += binError**2

        for bin in range(1, Vhist.GetNbinsX() + 1):
            binError = Vhist.GetBinError(bin)
            totalError_V += binError**2

        for bin in range(1, ttbarhist.GetNbinsX() + 1):
            binError = ttbarhist.GetBinError(bin)
            totalError_ttbar += binError**2

        dibosonerror = totalError_diboson**0.5
        stoperror = totalError_stop**0.5
        Verror = totalError_V**0.5
        ttbarerror = totalError_ttbar**0.5

        yielddiboson = dibosonhist.Integral()
        yieldstop = stophist.Integral()
        yieldV = Vhist.Integral()
        yieldttbar = ttbarhist.Integral()
        yielddata = datahist.Integral()

        datayieldstr = "DATA"
        dibosonyieldstr = "diboson"
        stopyieldstr = "stop"
        Vyieldstr = "V"
        ttbaryieldstr = "ttbar"
    
    elif analysis_name == "SUSY":
        datayieldstr = "DATA"
        dibosonyieldstr = "Diboson"
        stopyieldstr = "Single top"
        ttbaryieldstr = "t#bar{t}"
        Zyieldstr = "Z + jets"
        Wyieldstr = "W + jets"

    elif analysis_name == "HWW":
        datayieldstr = "DATA"
        higgsyieldstr = "Higgs"
        stopyieldstr = "Single top"
        dibosonyieldstr = "Diboson"
        ttbaryieldstr = "t#bar{t}"
        Vyieldstr = "V + jets"

    elif analysis_name == "Ztau":
        datayieldstr = "DATA"
        Ztauyieldstr = "Z #rightarrow #tau#tau"
        Zyieldstr = "Z #rightarrow ee, #mu#mu"
        Wyieldstr = "W + jets"
        topVyieldstr = "Other"

    #c1.Print("plots.pdf")

    ##Legend

    leg = ROOT.TLegend(0.65,0.70,0.90,0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0000)
    leg.SetNColumns(2)
    leg.SetTextSize(0.025)
    if analysis_name == "Zboson":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(Zhist,Zyieldstr,"f")
        leg.AddEntry(Whist,Wyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(stophist,stopyieldstr,"f")

    elif analysis_name == "Zboosted":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(Vhist,Vyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(stophist,stopyieldstr,"f")

    elif analysis_name == "HZZ":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(sighist,sigyieldstr,"f")
        leg.AddEntry(ZZhist,ZZyieldstr,"f")
        leg.AddEntry(othershist,othersyieldstr,"f")

    elif analysis_name == "Wboson":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(stophist,stopyieldstr,"f")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(wjetshist,wjetsyieldstr,"f")
        leg.AddEntry(zhist,zyieldstr,"f")
    
    elif analysis_name == "Singletop":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(stophist,stopyieldstr,"f")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(wjetshist,wjetsyieldstr,"f")
    
    elif analysis_name == "ZZdiboson":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(WWZhist,WWZyieldstr,"f")
        leg.AddEntry(Z_Zhist,Z_Zyieldstr,"f")
        leg.AddEntry(topVhist,topVyieldstr,"f")

    elif analysis_name == "WZ":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(Vhist,Vyieldstr,"f")
        leg.AddEntry(VVhist,VVyieldstr,"f")
        leg.AddEntry(tophist,topyieldstr,"f")
        leg.AddEntry(WZhist,WZyieldstr,"f")

    elif analysis_name == "ttbar":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(Vhist,Vyieldstr,"f")
        leg.AddEntry(stophist,stopyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")

    elif analysis_name == "SUSY":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(Zhist,Zyieldstr,"f")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(stophist,stopyieldstr,"f")
        leg.AddEntry(Whist,Wyieldstr,"f")
        leg.AddEntry(susyhist,"m(#tilde{l},#chi^{0}_{1})=(600,300) GeV","l")

    elif analysis_name == "HWW":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(higgshist,higgsyieldstr,"f")
        leg.AddEntry(dibosonhist,dibosonyieldstr,"f")
        leg.AddEntry(Vhist,Vyieldstr,"f")
        leg.AddEntry(ttbarhist,ttbaryieldstr,"f")
        leg.AddEntry(stophist,stopyieldstr,"f")

    elif analysis_name == "Ztau":
        leg.AddEntry(datahist,datayieldstr,"p")
        leg.AddEntry(Ztauhist,Ztauyieldstr,"f")
        leg.AddEntry(Zhist,Zyieldstr,"f")
        leg.AddEntry(Whist,Wyieldstr,"f")
        leg.AddEntry(topVhist,topVyieldstr,"f")

    ratio = datahist.Clone()
    ratio.Divide(rstack)
    ratio.SetStats(0)
    ratio.GetYaxis().SetRangeUser(0.,2.)
    ratio.GetYaxis().SetNdivisions(504,ROOT.kFALSE)
    #ratio.GetYaxis().SetNdivisions(207)
    #ratio.GetYaxis().SetNdivisions(505) 
    ratio.SetTitle("")
    if analysis_name == "Zboson":
        #ratio.GetXaxis().SetTitle("#eta^{leadlep}")
        #ratio.GetXaxis().SetTitle("#phi^{leadlep}")
        #ratio.GetXaxis().SetTitle("p_{T}^{leadlep}[GeV]")
        #ratio.GetXaxis().SetTitle("E^{leadlep}[GeV]")
        #ratio.GetXaxis().SetTitle("m_{ll} [GeV]")
        #ratio.GetXaxis().SetTitle("m_{#mu#mu} [GeV]")
        ratio.GetXaxis().SetTitle("m_{ee} [GeV]")
    else:
        ratio.GetXaxis().SetTitle("{}".format(hist_title))
    ratio.GetXaxis().SetLabelSize(0.09) #0.09
    ratio.GetXaxis().SetLabelOffset(0.01)
    ratio.GetYaxis().SetLabelSize(0.06) #0.09
    ratio.GetYaxis().SetLabelOffset(0.01) #0.01
    ratio.GetXaxis().SetTitleSize(0.10)
    ratio.GetYaxis().SetTitle("Data/MC")
    ratio.GetYaxis().SetTitleSize(0.12)
    ratio.GetYaxis().SetTitleOffset(0.25)

    stack_pad = ROOT.TPad("stack_pad","stack_pad",0,0.30,1,1)
    stack_pad.SetBottomMargin(0.014)
    #stack_pad.SetBottomMargin(0)
    stack_pad.SetTopMargin(0.05) #0.06
    stack_pad.SetFrameBorderMode(0)
    stack_pad.Draw()
    
    ratio_pad = ROOT.TPad("ratio_pad","ratio_pad",0,0.0,1,0.30)
    ratio_pad.SetTopMargin(0.05) #0
    #ratio_pad.SetBottomMargin(0.25)
    ratio_pad.SetBottomMargin(0.4) #0.5
    ratio_pad.SetFrameBorderMode(0)
    #ratio_pad.SetFrameFillStyle(4000)
    ratio_pad.SetGridy()
    ratio_pad.SetTicky(True)
    ratio_pad.Draw()
   
    #padX = ROOT.TPad("padX", "padX", 0.08, 0.10, 0.1, 0.30, 0, 0, 0)
    #padX.SetTickx(False)
    #padX.SetTicky(False)
    #padX.SetTopMargin(0.0)
    #padX.SetBottomMargin(0.5)
    #padX.SetFrameBorderMode(0)

    #pad2X = ROOT.TPad("pad2X", "pad2X", 0.08, 0.132, 0.09, 0.16, 0, 0, 0)
    #pad2X.SetTickx(False)
    #pad2X.SetTicky(False)
    #pad2X.SetTopMargin(0.0)
    #pad2X.SetBottomMargin(0.5)
    #pad2X.SetFrameBorderMode(0)
    
    #padX.Draw()
    #pad2X.Draw()

    stack_pad.cd()
    
    if analysis_name == "Zboson" or analysis_name == "SUSY" or (analysis_name == "ttbar" and hist_name != "hist_Topmass"):
        stack_pad.SetLogy(1)
    
    #hs.Draw("hist,nostack")
    hs.Draw("hist")
    hs.GetYaxis().SetLabelSize(0.03)
    hs.GetXaxis().SetLabelSize(0)
    hs.GetXaxis().SetTitleSize(0)
    datahist.Draw("e,same")
    if analysis_name == "SUSY":
        susyhist.SetLineColor(ROOT.kRed)
        susyhist.SetFillStyle(0)
        susyhist.SetFillColor(2)
        susyhist.SetLineStyle(2)
        susyhist.Draw("same")
    leg.Draw("same")

    c1.cd()

    CLtext = ROOT.TLatex()
    CLtext.SetTextSize(0.03)
    CLtext.SetTextColor(ROOT.kBlack)
    CLtext.DrawLatex(0.20,0.85,"#it{#bf{ATLAS}} Open Data")
    CLtext.DrawLatex(0.20,0.80,"for education")
    CLtext.DrawLatex(0.20,0.70,"ibrahim's results")

    en_text = ROOT.TLatex()
    en_text.SetTextSize(0.03)
    en_text.SetTextColor(ROOT.kBlack)
    en_text.DrawLatex(0.20,0.75,"#sqrt{s} = 13 TeV, 10 fb^{-1}")


    ratio_pad.cd()
    x_min = ratio.GetXaxis().GetXmin()
    x_max = ratio.GetXaxis().GetXmax()
    line = ROOT.TLine(x_min, 1.0, x_max, 1.0)
    line.SetLineColor(ROOT.kBlack)  
    line.SetLineStyle(1)  
    ratio_pad.Update()
    ratio.Draw("e")
    line.Draw("same")

    ## Extra pads


    if analysis_name == "Zboosted":
        c1.Print("{}_Zprime.pdf".format(hist_name))

    elif analysis_name == "HZZ":
        c1.Print("{}_HZZ.pdf".format(hist_name))
    
    elif analysis_name == "Zboson":
        c1.Print("{}_Zboson.pdf".format(hist_name))

    elif analysis_name == "Wboson":
        c1.Print("{}_Wboson.pdf".format(hist_name))

    elif analysis_name == "Singletop":
        c1.Print("{}_Singletop.pdf".format(hist_name))

    elif analysis_name == "ZZdiboson":
        c1.Print("{}_ZZdiboson.pdf".format(hist_name))

    elif analysis_name == "WZ":
        c1.Print("{}_WZ.pdf".format(hist_name))

    elif analysis_name == "ttbar":
        c1.Print("{}_ttbar.pdf".format(hist_name))

    elif analysis_name == "SUSY":
        c1.Print("{}_SUSY.pdf".format(hist_name))

    elif analysis_name == "HWW":
        c1.Print("{}_HWW.pdf".format(hist_name))

    elif analysis_name == "Ztau":
        c1.Print("{}_Ztau.pdf".format(hist_name))
    #### cutflows ####
    print("%80s" % "%%%%%%%%%%%%% Cutflows for the analysis samples %%%%%%%%%%")
    if analysis_name == "Zboson":
        #print("%63s" % "DATA","\t","Z","\t\t","W","\t","stop","\t\t","ttbar", "\t\t", "diboson")
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "Z",
        "W",
        "stop",
        "ttbar",
        "diboson"
        ))
        print(" ")

        for i in range(2,27,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            error_Z = Zcutflow.GetBinError(i)
            cutvalue_Z = Zcutflow.GetBinContent(i)
            error_W = Wcutflow.GetBinError(i)
            cutvalue_W = Wcutflow.GetBinContent(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            #print("%30s"% cutnamedata,"\t","%.02e" % cutvalue_data,"+-","%.02e" % error_data," ","%.02e" % cutvalue_Z,"+-","%.02e" % error_Z,"\t\t","%.02e" % cutvalue_W,"+-","%.02e" % error_W,"\t\t","%.02e" % cutvalue_stop,"+-","%.02e" % error_stop, "\t\t","%.02e" % cutvalue_ttbar,"+-","%.02e" % error_ttbar, "\t\t","%.02e" % cutvalue_diboson,"+-","%.02e" % error_diboson)
        #print("%50s"% cutnamedata,"\t",cutvalue_data," +-","%.02f" % error_data)
            print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_Z, error_Z,
            cutvalue_W, error_W,
            cutvalue_stop, error_stop,
            cutvalue_ttbar, error_ttbar,
            cutvalue_diboson, error_diboson
            ))

        print(" ")
        
        print("{} Region Final Yields: ".format(region_name))
        print("Data:            %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("Diboson:         %.02f"% yielddiboson,"+- %.02f"% dibosonerror,"\n")
        print("Z + jets:        %.02f"% yieldZ,"+- %.02f"% Zerror,"\n")
        print("W + jets:        %.02f"% yieldW,"+- %.02f"% Werror,"\n")
        print("ttbar:           %.02f"% yieldttbar,"+- %.02f"% ttbarerror,"\n")
        print("stop:            %.02f"% yieldstop,"+- %.02f"% stoperror,"\n")

    elif analysis_name == "Wboson":
        print("%63s" % "DATA","\t","Z","\t\t","W","\t","Stop","\t\t","\t","ttbar", "\t\t", "Diboson")
        print(" ")

        for i in range(2,21,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_z = zcutflow.GetBinContent(i)
            error_z = zcutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            cutvalue_wjets = wjetscutflow.GetBinContent(i)
            error_wjets = wjetscutflow.GetBinError(i)
            print("%30s"% cutnamedata,"\t",cutvalue_data,"+-","%.04f" % error_data," ","%.04f" % cutvalue_z,"+-","%.04f" % error_z,"\t\t","%.04f" % cutvalue_wjets,"+-","%.04f" % error_wjets,"\t\t","%.04f" % cutvalue_stop,"+-","%.04f" % error_stop, "\t\t","%.04f" % cutvalue_ttbar,"+-","%.04f" % error_ttbar, "\t\t","%.04f" % cutvalue_diboson,"+-","%.04f" % error_diboson)
            #print("%50s"% cutnamedata,"\t",cutvalue_data," +-","%.02f" % error_data)

        print(" ")

        print("{} Region Final Yields: ".format(region_name))
        print("Data:        %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("Single top:  %.02f"% yieldstop,"+- %.02f"% stoperror,"\n")
        print("Diboson:     %.02f"% yielddiboson,"+- %.02f"% dibosonerror,"\n")
        print("ttbar:       %.02f"% yieldttbar,"+- %.02f"% ttbarerror,"\n")
        print("Wjets:       %.02f"% yieldwjets,"+- %.02f"% wjetserror,"\n")
        print("Zjets:       %.02f"% yieldz,"+- %.02f"% zerror,"\n")

    elif analysis_name == "Singletop":
        print("%63s" % "DATA","\t","tq","\t\t","ZVV","\t","tt,Wt,tb","\t\t","\t","wjets")
        print(" ")

        for i in range(2,21,1):
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            cutvalue_wjets = wjetscutflow.GetBinContent(i)
            error_wjets = wjetscutflow.GetBinError(i)
            print("%50s"% cutnamedata,"\t",cutvalue_data,"+-","%.02f" % error_data,"\t","%.02f" % cutvalue_stop,"+-","%.02f" % error_stop,"\t","%.02f" % cutvalue_diboson,"+-","%.02f" % error_diboson,"\t","%.02f" % cutvalue_ttbar,"+-","%.02f" % error_ttbar,"\t","\t","%.02f" % cutvalue_wjets,"+-","%.02f" % error_wjets)
            #print("%50s"% cutnamedata,"\t",cutvalue_data," +-","%.02f" % error_data)

        print(" ")

        print("{} Region Final Yields: ".format(region_name))
        print("Data:        %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("tq:          %.02f"% yieldstop,"+- %.02f"% stoperror,"\n")
        print("ZVV:         %.02f"% yielddiboson,"+- %.02f"% dibosonerror,"\n")
        print("tt,Wt,tb:    %.02f"% yieldttbar,"+- %.02f"% ttbarerror,"\n")
        print("Wjets:       %.02f"% yieldwjets,"+- %.02f"% wjetserror,"\n")


    elif analysis_name == "Zboosted":
        print("%63s" % "DATA","\t","Single top","\t\t","V","\t","Diboson","\t\t","ttbar")
        print(" ")

        for i in range(2,27,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            error_V = Vcutflow.GetBinError(i)
            cutvalue_V = Vcutflow.GetBinContent(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            print("%30s"% cutnamedata,"\t",cutvalue_data,"+-","%.04f" % error_data," ","%.04f" % cutvalue_stop,"+-","%.04f" % error_stop,"\t\t","%.04f" % cutvalue_V,"+-","%.04f" % error_V,"\t\t","%.04f" % cutvalue_diboson,"+-","%.04f" % error_diboson, "\t\t","%.04f" % cutvalue_ttbar,"+-","%.04f" % error_ttbar)
        #print("%50s"% cutnamedata,"\t",cutvalue_data," +-","%.02f" % error_data)

        print(" ")


        print("{} Region Final Yields: ".format(region_name))
        print("Data:            %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("Diboson:         %.02f"% yielddiboson,"+- %.02f"% dibosonerror,"\n")
        print("V + jets:        %.02f"% yieldV,"+- %.02f"% Verror,"\n")
        print("ttbar:           %.02f"% yieldttbar,"+- %.02f"% ttbarerror,"\n")
        print("Single top:      %.02f"% yieldstop,"+- %.02f"% stoperror,"\n")

    elif analysis_name == "HZZ":
        print("%63s" % "DATA","\t","Higgs","\t\t","Other","\t","ZZ","\t\t")
        print(" ")
        for i in range(2,21,1):
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_sig = sigcutflow.GetBinContent(i)
            error_sig = sigcutflow.GetBinError(i)
            error_others = otherscutflow.GetBinError(i)
            cutvalue_others = otherscutflow.GetBinContent(i)
            cutvalue_ZZ = ZZcutflow.GetBinContent(i)
            error_ZZ = ZZcutflow.GetBinError(i)
            #print("%50s"% cutnamedata,"\t",cutvalue_data,"+-","%.04f" % error_data," ","%.04f" % cutvalue_sig,"%.04f" % error_sig," ","\t","%.04f" % cutvalue_others,"%.04f" % error_others," ","\t","%.04f" % cutvalue_ZZ,"%.04f" % error_ZZ, " ""\t")
            print("%50s"% cutnamedata,"\t",cutvalue_data,"+-","%.04f" % error_data," ","%.04f" % cutvalue_sig,"+-","%.04f" % error_sig,"\t\t","%.04f" % cutvalue_others,"+-","%.04f" % error_others,"\t\t","%.04f" % cutvalue_ZZ,"+-","%.04f" % error_ZZ)
            #print("%50s"% cutnamedata,"\t",cutvalue_data," +-","%.02f" % error_data)

        print(" ")


        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("Higgs:        %.02f"% yieldsig,"+- %.02f"% sigerror,"\n")
        print("others:       %.02f"% yieldothers,"+- %.02f"% otherserror,"\n")
        print("ZZ:           %.02f"% yieldZZ,"+- %.02f"% ZZerror,"\n")

    elif analysis_name == "ZZdiboson":
        print(" ")
        print("{:<30} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "ZZ",
        "WW,WZ",
        "Other"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_ZZ = Z_Zcutflow.GetBinContent(i)
            error_ZZ = Z_Zcutflow.GetBinError(i)
            error_WWZ = WWZcutflow.GetBinError(i)
            cutvalue_WWZ = WWZcutflow.GetBinContent(i)
            error_topV = topVcutflow.GetBinError(i)
            cutvalue_topV = topVcutflow.GetBinContent(i)
            print("{:<30} {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_ZZ, error_ZZ,
            cutvalue_WWZ, error_WWZ,
            cutvalue_topV, error_topV
            ))

        print("")
        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("WW, WZ:       %.02f"% yieldWWZ,"+- %.02f"% WWZerror,"\n")
        print("ZZ:           %.02f"% yieldZ_Z,"+- %.02f"% Z_Zerror,"\n")
        print("Other:        %.02f"% yieldtopV,"+- %.02f"% topVerror,"\n")

    elif analysis_name == "WZ":
        print(" ")
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "V",
        "VV",
        "Other",
        "WZ"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_V = Vcutflow.GetBinContent(i)
            error_V = Vcutflow.GetBinError(i)
            error_VV = VVcutflow.GetBinError(i)
            cutvalue_VV = VVcutflow.GetBinContent(i)
            error_top = topcutflow.GetBinError(i)
            cutvalue_top = topcutflow.GetBinContent(i)
            error_WZ = WZcutflow.GetBinError(i)
            cutvalue_WZ = WZcutflow.GetBinContent(i)
            print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}  {:.2e} +- {:.2e}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_V, error_V,
            cutvalue_VV, error_VV,
            cutvalue_top, error_top,
            cutvalue_WZ, error_WZ
            ))

        print(" ")

        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("V:       %.02f"% yieldV,"+- %.02f"% Verror,"\n")
        print("VV:           %.02f"% yieldVV,"+- %.02f"% VVerror,"\n")
        print("Other:           %.02f"% yieldtop,"+- %.02f"% toperror,"\n")
        print("WZ:           %.02f"% yieldWZ,"+- %.02f"% WZerror,"\n")

    elif analysis_name == "ttbar":
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "ttbar",
        "V jets",
        "stop",
        "diboson"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            error_V = Vcutflow.GetBinError(i)
            cutvalue_V = Vcutflow.GetBinContent(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}  {:.2e} +- {:.2e}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_ttbar, error_ttbar,
            cutvalue_V, error_V,
            cutvalue_stop, error_stop,
            cutvalue_diboson, error_diboson
            ))

        print(" ")

        print("")
        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% yielddata,"+- %.02f"% yielddata**0.5,"\n")
        print("V:       %.02f"% yieldV,"+- %.02f"% Verror,"\n")
        print("ttbar:           %.02f"% yieldttbar,"+- %.02f"% ttbarerror,"\n")
        print("diboson:           %.02f"% yielddiboson,"+- %.02f"% dibosonerror,"\n")
        print("stop:           %.02f"% yieldstop,"+- %.02f"% stoperror,"\n")

    elif analysis_name == "SUSY":
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "Z",
        "Diboson",
        "ttbar",
        "Single top",
        "W"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            error_W = Wcutflow.GetBinError(i)
            cutvalue_W = Wcutflow.GetBinContent(i)
            error_Z = Zcutflow.GetBinError(i)
            cutvalue_Z = Zcutflow.GetBinContent(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}  {:.2e} +- {:.2e} {:.2e} +- {:.2e}".format(
            #print("{:<30} {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}  {:.2f} +- {:.2f} {:.2f} +- {:.2f}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_Z, error_Z,
            cutvalue_diboson, error_diboson,
            cutvalue_ttbar, error_ttbar,
            cutvalue_stop, error_stop,
            cutvalue_W,    error_W
            ))

        print(" ")

        print("")
        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% datahist.Integral())
        print("Z:       %.02f"% Zhist.Integral())
        print("Diboson:           %.02f"% dibosonhist.Integral())
        print("ttbar:           %.02f" % ttbarhist.Integral())
        print("Single top:           %.02f" % stophist.Integral())
        print("W:           %.02f" % Whist.Integral())

    elif analysis_name == "HWW":
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "Higgs",
        "Diboson",
        "V+jets",
        "ttbar",
        "Single top"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_ttbar = ttbarcutflow.GetBinContent(i)
            error_ttbar = ttbarcutflow.GetBinError(i)
            error_V = Vcutflow.GetBinError(i)
            cutvalue_V = Vcutflow.GetBinContent(i)
            error_diboson = dibosoncutflow.GetBinError(i)
            cutvalue_diboson = dibosoncutflow.GetBinContent(i)
            error_stop = stopcutflow.GetBinError(i)
            cutvalue_stop = stopcutflow.GetBinContent(i)
            error_higgs = higgscutflow.GetBinError(i)
            cutvalue_higgs = higgscutflow.GetBinContent(i)
            #print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}  {:.2e} +- {:.2e} {:.2e} +- {:.2e}".format(
            print("{:<30} {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}  {:.2f} +- {:.2f} {:.2f} +- {:.2f}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_higgs, error_higgs,
            cutvalue_diboson, error_diboson,
            cutvalue_V, error_V,
            cutvalue_ttbar, error_ttbar,
            cutvalue_stop,    error_stop
            ))

        print(" ")
        print("")
        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% datahist.Integral())
        print("V:       %.02f"% Vhist.Integral())
        print("Diboson:           %.02f"% dibosonhist.Integral())
        print("ttbar:           %.02f" % ttbarhist.Integral())
        print("Single top:           %.02f" % stophist.Integral())
        print("Higgs:           %.02f" % higgshist.Integral())

    elif analysis_name == "Ztau":
        print("{:<30} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Cut Name",
        "DATA",
        "Ztau",
        "Z",
        "W +jets",
        "Other"
        ))
        print(" ")

        for i in range(2,40,1): 
            cutnamedata = datacutflow.GetXaxis().GetBinLabel(i)
            if "Histo" in cutnamedata: continue
            cutvalue_data = datacutflow.GetBinContent(i)
            error_data = datacutflow.GetBinError(i)
            cutvalue_Ztau = Ztaucutflow.GetBinContent(i)
            error_Ztau = Ztaucutflow.GetBinError(i)
            error_Z = Zcutflow.GetBinError(i)
            cutvalue_Z = Zcutflow.GetBinContent(i)
            error_W = Wcutflow.GetBinError(i)
            cutvalue_W = Wcutflow.GetBinContent(i)
            error_topV = topVcutflow.GetBinError(i)
            cutvalue_topV = topVcutflow.GetBinContent(i)
            #print("{:<30} {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}    {:.2e} +- {:.2e}  {:.2e} +- {:.2e}".format(
            print("{:<30} {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}    {:.2f} +- {:.2f}  {:.2f} +- {:.2f}".format(
            cutnamedata,
            cutvalue_data, error_data,
            cutvalue_Ztau, error_Ztau,
            cutvalue_Z, error_Z,
            cutvalue_W, error_W,
            cutvalue_topV, error_topV
            ))

        print(" ")
        print("")
        print("{} Region Final Yields: ".format(region_name))
        print("Data:         %.02f"% datahist.Integral())
        print("Ztau:       %.02f"% Ztauhist.Integral())
        print("Z:           %.02f"% Zhist.Integral())
        print("W:           %.02f" % Whist.Integral())
        print("Other:           %.02f" % topVhist.Integral())


if __name__ == "__main__":
    if analysis_name == "Zboosted":
        #plotting("Zprime","hleadLRpt",23000)
        #plotting("Zprime","hleadLReta",15000)
        #plotting("Zprime","hleadLRphi",13000)
        #plotting("Zprime","hleadLRm",11000)
        #plotting("Zprime","hMasstopLRjet",2300)
        #plotting("Zprime","hEtatopLRjet",3000)
        #plotting("Zprime","hPhitopLRjet",2500)
        #plotting("Zprime","hPttopLRjet",3200)
        plotting("Zprime","httbarm",2500)

    elif analysis_name == "HZZ":
        #plotting("HZZ","hZ1mass",140)
        #plotting("HZZ","hZ2mass",100)
        #plotting("HZZ","h4lmass",40)
        #plotting("HZZ","hZ2mass",100)
        #plotting("HZZ","hNjet",450)
        #plotting("HZZ","hEtalep",500)
        #plotting("HZZ","hPhilep",400)
        #plotting("HZZ","hPtlep",1900)
        plotting("HZZ","hElep",900)

    elif analysis_name == "Zboson":
        #plotting("Zll","hPtleadlep",1e10)
        #plotting("Zll","hPtleadlep",1e10)
        #plotting("Zll","hEtaleadlep",1e10)
        #plotting("Zll","hPhileadlep",1e10)
        #plotting("Zll","hEleadlep",1e10)
        plotting("Zll","hZllMass1",1e10)
        #plotting("Zmumu","hZmmMass1",1e10)
        #plotting("Zee","hZeeMass1",1e10)

    elif analysis_name == "Wboson":
        #plotting("Wl","hNjet",70e6)
        #plotting("Wl","hMET",35e6)
        #plotting("Wl","hPtleadlep",50e6)
        #plotting("Wl","hEtaleadlep",5e6)
        #plotting("Wl","hPhileadlep",3.5e6)
        #plotting("Wl","hEleadlep",18e6)
        #plotting("We","hMTWe",6.5e6)
        plotting("Wmu","hMTWmu",8e6)

    elif analysis_name == "Singletop":
        #plotting("singletop","histleadjeteta",4500)
        #plotting("singletop","histleadjetpt",5000)
        #plotting("singletop","histleadbjeteta",4500)
        #plotting("singletop","histleadbjetpt",5000)
        #plotting("Preselection","hMET",5000)
        #plotting("Preselection","hMTW",3500)
        #plotting("Preselection","hHT",3500)
        plotting("Preselection","hMlb",2000)

    elif analysis_name == "ZZdiboson":
        #plotting("ZZ","hEtalep",160)
        #plotting("ZZ","hPhilep",70)
        #plotting("ZZ","hPtlep",200)
        #plotting("ZZ","hElep",130)
        #plotting("ZZ","hZ1mass",70)
        #plotting("ZZ","hZ2mass",70)
        plotting("ZZ","h4lpt",50)

    elif analysis_name == "WZ":
        plotting("WZ","hist_etmiss",350)
        plotting("WZ","hist_threelepteta",600)
        plotting("WZ","hist_threeleptphi",400)
        plotting("WZ","hist_threeleptpt",1900)
        plotting("WZ","hist_threeleptE",1100)
        plotting("WZ","hist_mtw",400)
        plotting("WZ","hist_mLL",400)
        plotting("WZ","hist_ptLL",400)

    elif analysis_name == "ttbar":
        plotting("TTbar","hist_leadjet_pt",1e8)
        #plotting("TTbar","hist_etmiss",1e8)
        #plotting("TTbar","hist_n_jets",1e8)
        #plotting("TTbarWjjHist","hist_mtw",1e8)
        #plotting("TTbarTopjjjHist","hist_Topmass",10e3)

    elif analysis_name == "SUSY":
        #plotting("SFOS","histleadleptPt_SFOS",1e11)
        #plotting("SFOS","histleadleptEta_SFOS",1e11)
        #plotting("SFOS","histleadleptphi_SFOS",1e11)
        #plotting("SFOS","histleadleptE_SFOS",1e11)
        #plotting("SR2loose","histmt2_SR2_loose",1e5)
        #plotting("SR2loose","histetmiss_SR2_loose",1e5)
        plotting("SR2tight","histmt2_SR2_tight",1e5)
        #plotting("SR2tight","histetmiss_SR2_tight",1e5)

    elif analysis_name == "HWW":
        #plotting("HWW","histI_dPhi_LL",30e3)
        #plotting("HWW","histI_ptLL",35e3)
        #plotting("HWW","histI_etmiss",50e3)
        #plotting("HWW","histI_mt",24e3)
        #plotting("HWW","hist_dPhi_LL",600)
        #plotting("HWW","hist_ptLL",1100)
        plotting("HWW","hist_etmiss",1200)
        #plotting("HWW","hist_mt",900)

    elif analysis_name == "Ztau":
        #plotting("tautau","hist_taueta",3000)
        #plotting("tautau","hist_tauphi",1900)
        #plotting("tautau","hist_taupt",5500)
        plotting("tautau","hist_tauE",7500)
