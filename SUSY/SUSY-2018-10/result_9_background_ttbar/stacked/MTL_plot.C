#ifdef __CLING__
#pragma cling optimize(0)
#endif
void MTL_plot()
{
//=========Macro generated from canvas: MTL_plot/MTL_plot
//=========  (Sun Feb  1 13:37:51 2026) by ROOT version 6.37.01
   TCanvas *MTL_plot = new TCanvas("MTL_plot", "MTL_plot", 0, 0, 900, 700);
   gStyle->SetOptFit(0);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(1);
   MTL_plot->SetHighLightColor(2);
   TColor::SetPalette(57, nullptr);
   MTL_plot->Range(4.999997,-16.52771,455,148.7494);
   MTL_plot->SetFillColor(0);
   MTL_plot->SetBorderMode(0);
   MTL_plot->SetBorderSize(2);
   MTL_plot->SetTickx(1);
   MTL_plot->SetTicky(1);
   MTL_plot->SetFrameBorderMode(0);
   MTL_plot->SetFrameBorderMode(0);
   
   THStack *MTL_plot_stack = new THStack();
   MTL_plot_stack->SetName("MTL_plot_stack");
   MTL_plot_stack->SetTitle("M_{T}^{\\ell};M_{T}^{\\ell} [GeV];Events");
   
   TH1F *MTL_plot_stack_stack_7 = new TH1F("MTL_plot_stack_stack_7", "M_{T}^{\\ell}", 18, 50, 410);
   MTL_plot_stack_stack_7->SetMinimum(0);
   MTL_plot_stack_stack_7->SetMaximum(132.2216760903597);
   MTL_plot_stack_stack_7->SetDirectory(nullptr);
   MTL_plot_stack_stack_7->SetStats(0);
   MTL_plot_stack_stack_7->SetLineColor(TColor::GetColor("#000099"));
   MTL_plot_stack_stack_7->SetLineWidth(0);
   MTL_plot_stack_stack_7->GetXaxis()->SetTitle("M_{T}^{\\ell} [GeV]");
   MTL_plot_stack_stack_7->GetXaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_7->GetXaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_7->GetXaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_7->GetYaxis()->SetTitle("Events");
   MTL_plot_stack_stack_7->GetYaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_7->GetYaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_7->GetZaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_7->GetZaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_7->GetZaxis()->SetTitleFont(42);
   MTL_plot_stack->SetHistogram(MTL_plot_stack_stack_7);
   
   
   TH1D *MTL_plot_stack_stack_8 = new TH1D("MTL_plot_stack_stack_8", "\"Transverse Mass", 18, 50, 410);
   MTL_plot_stack_stack_8->SetBinContent(1,76.24167257547379);
   MTL_plot_stack_stack_8->SetBinContent(2,124.3010057806969);
   MTL_plot_stack_stack_8->SetBinContent(3,13.50499069690704);
   MTL_plot_stack_stack_8->SetBinContent(4,3.111961781978607);
   MTL_plot_stack_stack_8->SetBinContent(5,2.484361529350281);
   MTL_plot_stack_stack_8->SetBinContent(6,10.75687098503113);
   MTL_plot_stack_stack_8->SetBinContent(7,5.457763075828552);
   MTL_plot_stack_stack_8->SetBinContent(8,1.132846236228943);
   MTL_plot_stack_stack_8->SetBinContent(9,5.530314564704895);
   MTL_plot_stack_stack_8->SetBinError(1,21.64431483597074);
   MTL_plot_stack_stack_8->SetBinError(2,23.02190212519462);
   MTL_plot_stack_stack_8->SetBinError(3,12.14455553147783);
   MTL_plot_stack_stack_8->SetBinError(4,12.83719614852837);
   MTL_plot_stack_stack_8->SetBinError(5,8.568135935433029);
   MTL_plot_stack_stack_8->SetBinError(6,8.393729754980084);
   MTL_plot_stack_stack_8->SetBinError(7,8.459917393990342);
   MTL_plot_stack_stack_8->SetBinError(8,2.935947567225416);
   MTL_plot_stack_stack_8->SetBinError(9,3.193291774501699);
   MTL_plot_stack_stack_8->SetEntries(404);
   MTL_plot_stack_stack_8->SetFillColor(TColor::GetColor("#ffcc33"));
   MTL_plot_stack_stack_8->SetLineColor(TColor::GetColor("#663300"));
   MTL_plot_stack_stack_8->SetLineWidth(2);
   MTL_plot_stack_stack_8->GetXaxis()->SetTitle(" M^{L}_{T} [GeV]");
   MTL_plot_stack_stack_8->GetXaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_8->GetXaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_8->GetXaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_8->GetYaxis()->SetTitle("Events / bin\"");
   MTL_plot_stack_stack_8->GetYaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_8->GetYaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_8->GetZaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_8->GetZaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_8->GetZaxis()->SetTitleFont(42);
   MTL_plot_stack->Add(MTL_plot_stack_stack_8, "");
   
   TH1D *MTL_plot_stack_stack_9 = new TH1D("MTL_plot_stack_stack_9", "\"Transverse Mass", 18, 50, 410);
   MTL_plot_stack_stack_9->SetBinContent(1,0.8122000098228455);
   MTL_plot_stack_stack_9->SetBinContent(2,1.624400019645691);
   MTL_plot_stack_stack_9->SetBinContent(3,1.624400019645691);
   MTL_plot_stack_stack_9->SetBinContent(4,0.8122000098228455);
   MTL_plot_stack_stack_9->SetBinContent(5,1.218300014734268);
   MTL_plot_stack_stack_9->SetBinContent(6,0.4061000049114227);
   MTL_plot_stack_stack_9->SetBinContent(7,1.624400019645691);
   MTL_plot_stack_stack_9->SetBinError(1,0.5743121346255146);
   MTL_plot_stack_stack_9->SetBinError(2,0.8122000098228455);
   MTL_plot_stack_stack_9->SetBinError(3,0.8122000098228455);
   MTL_plot_stack_stack_9->SetBinError(4,0.5743121346255146);
   MTL_plot_stack_stack_9->SetBinError(5,0.7033858414605548);
   MTL_plot_stack_stack_9->SetBinError(6,0.4061000049114227);
   MTL_plot_stack_stack_9->SetBinError(7,0.8122000098228455);
   MTL_plot_stack_stack_9->SetEntries(20);
   MTL_plot_stack_stack_9->SetFillColor(TColor::GetColor("#99ccff"));
   MTL_plot_stack_stack_9->SetLineColor(TColor::GetColor("#0066cc"));
   MTL_plot_stack_stack_9->SetLineWidth(2);
   MTL_plot_stack_stack_9->GetXaxis()->SetTitle(" M^{L}_{T} [GeV]");
   MTL_plot_stack_stack_9->GetXaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_9->GetXaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_9->GetXaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_9->GetYaxis()->SetTitle("Events / bin\"");
   MTL_plot_stack_stack_9->GetYaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_9->GetYaxis()->SetTitleFont(42);
   MTL_plot_stack_stack_9->GetZaxis()->SetLabelFont(42);
   MTL_plot_stack_stack_9->GetZaxis()->SetTitleOffset(1);
   MTL_plot_stack_stack_9->GetZaxis()->SetTitleFont(42);
   MTL_plot_stack->Add(MTL_plot_stack_stack_9, "");
   MTL_plot_stack->Draw("hist");
   
   TLegend *leg = new TLegend(0.62, 0.72, 0.88, 0.88, nullptr, "brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *legentry = leg->AddEntry("hist_mtl","t#bar{t} (BG)","f");
   legentry->SetFillColor(TColor::GetColor("#ffcc33"));
   legentry->SetFillStyle(1001);
   legentry->SetLineColor(TColor::GetColor("#663300"));
   legentry->SetLineWidth(2);
   legentry->SetTextFont(42);
   legentry = leg->AddEntry("hist_mtl","SUSY signal","f");
   legentry->SetFillColor(TColor::GetColor("#99ccff"));
   legentry->SetFillStyle(1001);
   legentry->SetLineColor(TColor::GetColor("#0066cc"));
   legentry->SetLineWidth(2);
   legentry->SetTextFont(42);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0.466004, 0.921786, 0.533996, 0.995, "blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_text2 = pt->AddText("M_{T}^{\\ell}");
   pt->Draw("blNDC");
   MTL_plot->Modified();
   MTL_plot->SetSelected(MTL_plot);
}
