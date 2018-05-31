import os
from .Base import Base
from ..tools import run_de_analysis, Logging

class DeAnalysis(Base):
    """
Perform DE analysis.

Usage:
  scrtools de_analysis [--labels <attr> -p <threads> --alpha <alpha> --fisher --mwu --roc] <input_h5ad_file> <output_spreadsheet>
  scrtools de_analysis -h

Arguments:
  input_h5ad_file        Single cell data with clustering calculated. DE results would be written back.
  output_spreadsheet     Output spreadsheet with DE results.

Options:
  --labels <attr>                  <attr> used as cluster labels. [default: louvain_labels]
  --alpha <alpha>                  Control false discovery rate at <alpha>. [default: 0.05]
  --fisher                         Calculate Fisher's exact test.
  --mwu                            Calculate Mann-Whitney U test.
  --roc                            Calculate area under cuver in ROC curve.
  -p <threads>                     Use <threads> threads. [default: 1]
  -h, --help                       Print out help information.

Examples:
  scrtools de_analysis --labels louvain_labels -p 26 --fisher --mwu --roc manton_bm.h5ad manton_bm_de.xlsx
    """

    def execute(self):
        run_de_analysis(self.args['<input_h5ad_file>'], self.args['<output_spreadsheet>'], self.args['--labels'], int(self.args['-p']), float(self.args['--alpha']), self.args['--fisher'], self.args['--mwu'], self.args['--roc'])

        logger = Logging(os.path.splitext(self.args['<input_h5ad_file>'])[0] + ".log")
        logger.add_output(self.args['<input_h5ad_file>'])
        logger.add_output(self.args['<output_spreadsheet>'])
