#ifdef __CLING__
#pragma cling optimize(0)
#endif
void Meff_plot()
{
//=========Macro generated from canvas: Meff_plot/Meff_plot
//=========  (Sun Feb  1 13:37:51 2026) by ROOT version 6.37.01
   TCanvas *Meff_plot = new TCanvas("Meff_plot", "Meff_plot", 0, 0, 900, 700);
   gStyle->SetOptFit(0);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(1);
   Meff_plot->SetHighLightColor(2);
   TColor::SetPalette(57, nullptr);
   Meff_plot->Range(0.125,-48.4627,3.875,43.08415);
   Meff_plot->SetFillColor(0);
   Meff_plot->SetBorderMode(0);
   Meff_plot->SetBorderSize(2);
   Meff_plot->SetTickx(1);
   Meff_plot->SetTicky(1);
   Meff_plot->SetFrameBorderMode(0);
   Meff_plot->SetFrameBorderMode(0);
   
   THStack *Meff_plot_stack = new THStack();
   Meff_plot_stack->SetName("Meff_plot_stack");
   Meff_plot_stack->SetTitle("M_{eff};M_{eff} [GeV];Events");
   
   TH1F *Meff_plot_stack_stack_4 = new TH1F("Meff_plot_stack_stack_4", "M_{eff}", 3, 0.5, 3.5);
   Meff_plot_stack_stack_4->SetMinimum(-39.30801621079445);
   Meff_plot_stack_stack_4->SetMaximum(33.92946115583182);
   Meff_plot_stack_stack_4->SetDirectory(nullptr);
   Meff_plot_stack_stack_4->SetStats(0);
   Meff_plot_stack_stack_4->SetLineColor(TColor::GetColor("#000099"));
   Meff_plot_stack_stack_4->SetLineWidth(0);
   Meff_plot_stack_stack_4->GetXaxis()->SetTitle("M_{eff} [GeV]");
   Meff_plot_stack_stack_4->GetXaxis()->SetBinLabel(1, "Meff [] 700 1300");
   Meff_plot_stack_stack_4->GetXaxis()->SetBinLabel(2, "Meff [] 1300 1900");
   Meff_plot_stack_stack_4->GetXaxis()->SetBinLabel(3, "Meff > 1900");
   Meff_plot_stack_stack_4->GetXaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_4->GetXaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_4->GetXaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_4->GetYaxis()->SetTitle("Events");
   Meff_plot_stack_stack_4->GetYaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_4->GetYaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_4->GetZaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_4->GetZaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_4->GetZaxis()->SetTitleFont(42);
   Meff_plot_stack->SetHistogram(Meff_plot_stack_stack_4);
   
   
   TH1D *Meff_plot_stack_stack_5 = new TH1D("Meff_plot_stack_stack_5", "event counts in bins ", 3, 0.5, 3.5);
   Meff_plot_stack_stack_5->SetBinContent(1,29.47107249498367);
   Meff_plot_stack_stack_5->SetBinContent(2,-41.33851623535156);
   Meff_plot_stack_stack_5->SetBinContent(3,-1.930792570114136);
   Meff_plot_stack_stack_5->SetBinError(1,15.95780768570854);
   Meff_plot_stack_stack_5->SetBinError(2,10.63625168934002);
   Meff_plot_stack_stack_5->SetBinError(3,1.930792570114136);
   Meff_plot_stack_stack_5->SetEntries(102);
   Meff_plot_stack_stack_5->SetFillColor(TColor::GetColor("#ffcc33"));
   Meff_plot_stack_stack_5->SetLineColor(TColor::GetColor("#663300"));
   Meff_plot_stack_stack_5->SetLineWidth(2);
   Meff_plot_stack_stack_5->GetXaxis()->SetBinLabel(1, "Meff [] 700 1300");
   Meff_plot_stack_stack_5->GetXaxis()->SetBinLabel(2, "Meff [] 1300 1900");
   Meff_plot_stack_stack_5->GetXaxis()->SetBinLabel(3, "Meff > 1900");
   Meff_plot_stack_stack_5->GetXaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_5->GetXaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_5->GetXaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_5->GetYaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_5->GetYaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_5->GetZaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_5->GetZaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_5->GetZaxis()->SetTitleFont(42);
   Meff_plot_stack->Add(Meff_plot_stack_stack_5, "");
   
   TH1D *Meff_plot_stack_stack_6 = new TH1D("Meff_plot_stack_stack_6", "event counts in bins ", 3, 0.5, 3.5);
   Meff_plot_stack_stack_6->SetBinContent(1,2.842700034379959);
   Meff_plot_stack_stack_6->SetBinContent(2,2.030500024557114);
   Meff_plot_stack_stack_6->SetBinContent(3,0.4061000049114227);
   Meff_plot_stack_stack_6->SetBinError(1,1.074439620417733);
   Meff_plot_stack_stack_6->SetBinError(2,0.9080672166449397);
   Meff_plot_stack_stack_6->SetBinError(3,0.4061000049114227);
   Meff_plot_stack_stack_6->SetEntries(13);
   Meff_plot_stack_stack_6->SetFillColor(TColor::GetColor("#99ccff"));
   Meff_plot_stack_stack_6->SetLineColor(TColor::GetColor("#0066cc"));
   Meff_plot_stack_stack_6->SetLineWidth(2);
   Meff_plot_stack_stack_6->GetXaxis()->SetBinLabel(1, "Meff [] 700 1300");
   Meff_plot_stack_stack_6->GetXaxis()->SetBinLabel(2, "Meff [] 1300 1900");
   Meff_plot_stack_stack_6->GetXaxis()->SetBinLabel(3, "Meff > 1900");
   Meff_plot_stack_stack_6->GetXaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_6->GetXaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_6->GetXaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_6->GetYaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_6->GetYaxis()->SetTitleFont(42);
   Meff_plot_stack_stack_6->GetZaxis()->SetLabelFont(42);
   Meff_plot_stack_stack_6->GetZaxis()->SetTitleOffset(1);
   Meff_plot_stack_stack_6->GetZaxis()->SetTitleFont(42);
   Meff_plot_stack->Add(Meff_plot_stack_stack_6, "");
   Meff_plot_stack->Draw("hist");
   
   TLegend *leg = new TLegend(0.62, 0.72, 0.88, 0.88, nullptr, "brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *legentry = leg->AddEntry("bincounts","t#bar{t} (BG)","f");
   legentry->SetFillColor(TColor::GetColor("#ffcc33"));
   legentry->SetFillStyle(1001);
   legentry->SetLineColor(TColor::GetColor("#663300"));
   legentry->SetLineWidth(2);
   legentry->SetTextFont(42);
   legentry = leg->AddEntry("bincounts","SUSY signal","f");
   legentry->SetFillColor(TColor::GetColor("#99ccff"));
   legentry->SetFillStyle(1001);
   legentry->SetLineColor(TColor::GetColor("#0066cc"));
   legentry->SetLineWidth(2);
   legentry->SetTextFont(42);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0.45875, 0.928929, 0.54125, 0.995, "blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_text1 = pt->AddText("M_{eff}");
   pt->Draw("blNDC");
   Meff_plot->Modified();
   Meff_plot->SetSelected(Meff_plot);
}
