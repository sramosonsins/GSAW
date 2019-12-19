from GSAW_GUI import *
import re, csv

#class workerThread(QtCore.QThread):
#    def __init__(self, parent=None):
#        QtCore.QThread.__init__(self)
#    def tun(self):
#        x = ""
#        self.emit(QtCore.SIGNAL('update(QString)'), str(x))

#class CustomDialog(QtWidgets.QDialog):
#    def __init__(self, *args, **kwargs):
#        super(CustomDialog, self).__init__(*args, **kwargs)
#        self.setWindowTitle("Are you sure?")
#
#        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
#
#        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
#        self.buttonBox.accepted.connect(self.accept)
#        self.buttonBox.rejected.connect(self.reject)
#
#        self.layout = QtWidgets.QVBoxLayout()
#        self.layout.addWidget(self.buttonBox)
#        self.setLayout(self.layout)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("GSAW")
        self.setWindowIcon(QtGui.QIcon('GSAW.png'))
        self.setFixedSize(1215, 978)

        #####################
        ## Pre-Process tab ##
        #####################

        self.frameConversion.setEnabled(False)
        self.frameIndex.setEnabled(False)
        self.frameVCF.setEnabled(False)
        self.frameJoin.setEnabled(False)
        self.frameWeight.setEnabled(False)

        self.radioFa2tFa.setEnabled(False)
        self.radioFa2ms.setEnabled(False)
        self.radioFa2Fa.setEnabled(False)
        self.radiotFa2Fa.setEnabled(False)
        self.radiotFa2ms.setEnabled(False)
        self.radioVCF2tFa.setEnabled(False)
        self.radioMerge.setEnabled(False)
        self.radioConcat.setEnabled(False)
        self.radioLongWeight.setChecked(True)
        self.radioWindowLengthConv1.setChecked(True)

        self.checkConversion.toggled.connect(self.btnstate_pre)
        self.checkIndex.toggled.connect(self.btnstate_pre)
        self.checkJoin.toggled.connect(self.btnstate_pre)
        self.checkWeight.toggled.connect(self.btnstate_pre)
        self.radioFa2tFa.toggled.connect(self.btnstate_pre)
        self.radioFa2ms.toggled.connect(self.btnstate_pre)
        self.radioFa2Fa.toggled.connect(self.btnstate_pre)
        self.radiotFa2Fa.toggled.connect(self.btnstate_pre)
        self.radiotFa2ms.toggled.connect(self.btnstate_pre)
        self.radioVCF2tFa.toggled.connect(self.btnstate_pre)
        self.radioMerge.toggled.connect(self.btnstate_pre)
        self.radioConcat.toggled.connect(self.btnstate_pre)
        self.checkGFFWeight.toggled.connect(self.btnstate_pre)
        self.checkMaskWeight.toggled.connect(self.btnstate_pre)
        self.checkRegionsWeight.toggled.connect(self.btnstate_pre)
        self.checkOutgroupWeight.toggled.connect(self.btnstate_pre)
        self.radioCode4Weight.toggled.connect(self.btnstate_pre)
        self.checkMaskConv.toggled.connect(self.btnstate_pre)
        self.checkCoordConv.toggled.connect(self.btnstate_pre)
        self.checkWeightConv.toggled.connect(self.btnstate_pre)
        self.checkOrderSamplesConv.toggled.connect(self.btnstate_pre)
        self.checkWindowSizeConv.toggled.connect(self.btnstate_pre)
        self.checkSlideConv.toggled.connect(self.btnstate_pre)

        self.openInputIndex.clicked.connect(self.on_click_getIndexfile)
        self.updateIndex.clicked.connect(self.on_click_getIndexParam)
        self.openInputJoin.clicked.connect(self.on_click_getJoinfile)
        self.updateJoin.clicked.connect(self.on_click_getJoinParam)
        self.openInputVCF.clicked.connect(self.on_click_getVCFfile)
        self.openInputRefFasta.clicked.connect(self.on_click_getRefFastafile)
        self.openScaffoldVCF.clicked.connect(self.on_click_getScaffoldVCFfile)
        self.updateVCF.clicked.connect(self.on_click_getVCFParam)
        self.openInputWeight.clicked.connect(self.on_click_getWeightfile)
        self.openGFFWeight.clicked.connect(self.on_click_getgffWeightfile)
        self.openMaskWeight.clicked.connect(self.on_click_getMaskWeightfile)
        self.openRegionsWeight.clicked.connect(self.on_click_getRegionsWeightfile)
        self.openScaffoldWeight.clicked.connect(self.on_click_getScaffoldWeightfile)
        self.updateWeight.clicked.connect(self.on_click_getWeightParam)
        self.openInputConv.clicked.connect(self.on_click_getConvfile)
        self.openScaffoldConv.clicked.connect(self.on_click_getScaffoldConvfile)
        self.openMaskConv.clicked.connect(self.on_click_getMaskConvfile)
        self.openCoordConv.clicked.connect(self.on_click_getCoordConvfile)
        self.openWeightConv.clicked.connect(self.on_click_getWeightConvfile)
        self.updateConv.clicked.connect(self.on_click_getConvParam)

        ###################
        ## mstatspop tab ##
        ###################

        self.openInput.clicked.connect(self.on_click_getinputfile)
        self.updateOutput.clicked.connect(self.on_click_getoutputfile)
        self.updateGeneralParam.clicked.connect(self.on_click_getGeneralParam)
        self.openScaffold.clicked.connect(self.on_click_getscaffoldfile)
        self.openAltSpect.clicked.connect(self.on_click_getaltspecfile)
        self.openNullSpect.clicked.connect(self.on_click_getnullspecfile)
        self.openMaskMS.clicked.connect(self.on_click_getmaskmsfile)
        self.openCoordTF.clicked.connect(self.on_click_getcoordtffile)
        self.openWeights.clicked.connect(self.on_click_getweightsfile)
        self.openGFF.clicked.connect(self.on_click_getgfffile)
        self.updateMS.clicked.connect(self.on_click_getMSParam)
        self.updateFasta.clicked.connect(self.on_click_getFastaParam)
        self.updateTFasta.clicked.connect(self.on_click_getTFastaParam)

        self.frameMS.setEnabled(False)
        self.frameFasta.setEnabled(False)
        self.frameTFasta.setEnabled(False)

        self.checkOrderSamples.setEnabled(False)
        self.labelOrderSamples1.setEnabled(False)
        self.lineOrderSamples1.setEnabled(False)
        self.labelOrderSamples2.setEnabled(False)
        self.lineOrderSamples2.setEnabled(False)
        self.checkPermWindows.setEnabled(False)
        self.linePermWindows.setEnabled(False)
        self.checkSeed.setEnabled(False)
        self.lineSeed.setEnabled(False)

        self.lineAltSpect.setEnabled(False)
        self.openAltSpect.setEnabled(False)
        self.checkNullSpect.setEnabled(False)
        self.lineNullSpect.setEnabled(False)
        self.openNullSpect.setEnabled(False)

        self.lineMSiter.setEnabled(False)
        self.lineMSratio.setEnabled(False)
        self.lineMSRev.setEnabled(False)
        self.lineMaskMS.setEnabled(False)
        self.openMaskMS.setEnabled(False)
        self.checkSlide.setEnabled(False)
        self.checkMSRev.setEnabled(False)

        self.radioWindowLengthTF1.setChecked(True)
        self.radioLong.setChecked(True)

        self.radioMS.toggled.connect(self.btnstate)
        self.radioFasta.toggled.connect(self.btnstate)
        self.radioTFasta.toggled.connect(self.btnstate)

        self.radioFormat0.toggled.connect(self.btnstate)
        self.radioFormat1.toggled.connect(self.btnstate)
        self.radioFormat2.toggled.connect(self.btnstate)
        self.radioFormat3.toggled.connect(self.btnstate)
        self.radioFormat4.toggled.connect(self.btnstate)
        self.radioFormat5.toggled.connect(self.btnstate)
        self.radioFormat6.toggled.connect(self.btnstate)
        self.radioFormat7.toggled.connect(self.btnstate)
        self.radioFormat10.toggled.connect(self.btnstate)

        self.checkOrderSamples.toggled.connect(self.btnstate)
        self.checkPermWindows.toggled.connect(self.btnstate)
        self.checkSeed.toggled.connect(self.btnstate)

        self.checkGFF.toggled.connect(self.btnstate)

        self.checkMaskMS.toggled.connect(self.btnstate)
        self.checkMSiter.toggled.connect(self.btnstate)
        self.checkMSratio.toggled.connect(self.btnstate)
        self.checkMSRev.toggled.connect(self.btnstate)
        self.checkMSoutgroup.toggled.connect(self.btnstate)

        self.radioCode4.toggled.connect(self.btnstate)

        self.radioWindowSize.toggled.connect(self.btnstate)
        self.radioCoordTF.toggled.connect(self.btnstate)
        self.checkSlide.toggled.connect(self.btnstate)
        self.checkFirstWindowTF.toggled.connect(self.btnstate)

        self.checkAltSpect.toggled.connect(self.btnstate)
        self.checkNullSpect.toggled.connect(self.btnstate)

        self.checkOutgroup.toggled.connect(self.btnstate)
        self.checkUnknownPos.toggled.connect(self.btnstate)

        ######################
        ## Post-process tab ##
        ######################

        self.tableWidget.setEnabled(False)
        self.DownloadTable.setEnabled(False)
        self.RunAll.clicked.connect(self.on_click_RunAll)
        self.DownloadTable.clicked.connect(self.on_click_DownloadTable)

        ############################################
        ## Tooltips (Informative floating message) ##
        ############################################
 
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.RunAll.setToolTip('Execute all commands')
        self.DownloadTable.setToolTip('Download the filtered table in tab-delimited CSV format')
        self.checkConversion.setToolTip('Convert between format files depending on the type\nof analysis')
        self.radioFa2tFa.setToolTip('Useful to run the analysis in sliding windows mode')
        self.radioFa2ms.setToolTip('Useful to generate mask files in case doing simulations')
        self.radioFa2Fa.setToolTip('Useful for concatenate different regions from coordenates\nfile')
        self.radiotFa2Fa.setToolTip('Useful to generate a weighting file from GFF file')
        self.radiotFa2ms.setToolTip('Useful to generate mask files in case doing simulations')
        self.radioVCF2tFa.setToolTip('Useful to run the analysis in sliding windows mode')
        self.checkWeight.setToolTip('Generate a weighting file, with the format conversion\nif the "Conversion of file formats" option is also selected\nor from a tFasta file if the option is not selected')
        self.checkIndex.setToolTip('Generate the index file from a tFasta file')
        self.checkJoin.setToolTip('Join different tFasta files from a list')
        self.checkMaskConv.setToolTip('Include a file to mask regions, it will mask these\nregions with Ns')
        self.checkCoordConv.setToolTip('Include a file with the coordinates of the windows\nto analyze')
        self.labelOutputConv.setToolTip('including the extension with .gz')
        self.lineOutputConv.setToolTip('including the extension with .gz')
        self.labelOutputVCF.setToolTip('only the output name, without the extension')
        self.lineOutputVCF.setToolTip('only the output name, without the extension')
        self.labelOutputWeight.setToolTip('including the extension with .gz')
        self.lineOutputWeight.setToolTip('including the extension with .gz')
        self.checkMaskWeight.setToolTip('Include a file to mask regions, it will mask these\nregions with Ns')
        self.checkRegionsWeight.setToolTip('Include a file with the coordinates of the windows\nto analyze')
        self.labelInputJoin.setToolTip('List with each tFasta file per line, including the path')
        self.lineInputJoin.setToolTip('List with each tFasta file per line, including the path')
        self.radioCode4Weight.setToolTip('Introduce the single letter code for the 64 triplets\nin the order UUU UUC UUA UUG ...')
        self.lineCode4Weight.setToolTip('Introduce the single letter code for the 64 triplets\nin the order UUU UUC UUA UUG ...')
        self.radioFormat0.setToolTip('Output in an extended list format with header for each\nset of statistics')
        self.radioFormat1.setToolTip('All statistics in a single line per window')
        self.radioFormat2.setToolTip('Site frequency spectrum (SFS) in a single line per window')
        self.radioFormat3.setToolTip('File format to use as input in dadi software')
        self.radioFormat4.setToolTip('All pairwise comparisons (mismatch distribution) in a\nsingle line')
        self.radioFormat5.setToolTip('Frequency of variants for each line, one window per line')
        self.radioFormat6.setToolTip('SNP genotype matrix format')
        self.radioFormat7.setToolTip('File format to use as input in SweepFiinder software')
        self.radioFormat10.setToolTip('Extended format plus dadi-format, all pairwise comparisons\nand frequency of SNPs of each line')
        self.labelOutput.setToolTip('including the .txt extension')
        self.lineOutput.setToolTip('including the .txt extension')
        self.radioCode4.setToolTip('Introduce the single letter code for the 64 triplets\nin the order UUU UUC UUA UUG ...')
        self.lineCode4.setToolTip('Introduce the single letter code for the 64 triplets\nin the order UUU UUC UUA UUG ...')
        self.checkMaskMS.setToolTip('Include a mask file to exclude regions')
        self.checkMaskFasta.setToolTip('Make a mask file with the valid positions of the Fasta file,\nwhich is useful for running subsequent ms simulations')
        self.radioWindowSize.setToolTip('Size of windows to analyze')
        self.lineWindowSize.setToolTip('Size of windows to analyze')
        self.radioCoordTF.setToolTip('File with coordinates of the windows to analyze')
        self.checkSlide.setToolTip('Distance between windows')
        self.lineSlide.setToolTip('Distance between windows')
        self.checkFirstWindowTF.setToolTip('Displacement of the first window, useful to compare\noverlapped windows')
        self.lineFirstWindowTF.setToolTip('Displacement of the first window, useful to compare\noverlapped windows')

    ##################
    ## Progress Bar ##
    ##################

    #def close_progress(self):
    #    self.progress.close()
    #    self.proc.terminate()

    #def progressBar(self, number):
    #    self.progress = QtGui.QDialog()
    #    self.progress._conf = _progressbar.Ui_ProgressBar()
    #    self.progress._conf.setupUi(self.progress)
    #    self.progress._conf.progressBar.setRange(0,0)
    #    QtCore.Qobject.connect(self.progress._conf.pushButton, QtCore.SIGNAL("clicked()"), self.close_progress)

    ##############################################
    ## Connection between widgets and functions ##
    ##############################################

    def on_click_getinputfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInput.setText(filename)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-i " in text0:
                old = re.findall("-i\s[\w\.\/\_\-\(\)]+", text0)[0]
                text = text0.replace(old, "-i " + filename)
            else:
                text = text0 + " -i " + filename
            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getoutputfile(self):
        outfile = self.lineOutput.text()
        if outfile:
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-T " in text0:
                old = re.findall("-T\s[\w\.\/\_\-\(\)]+", text0)[0]
                text = text0.replace(old, "-T " + outfile)
            else:
                text = text0 + " -T " + outfile
            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getGeneralParam(self):

        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        if "bin/mstatspop" not in textall:
            textall = textall + "\n./bin/mstatspop/bin/mstatspop"
        for line in textall.splitlines():
            if "bin/mstatspop" in line:
                text0 = line
            else:
                if textrest == "":
                    textrest = line
                else:
                    textrest += "\n" + line
        ntotalpops = self.lineTotalSamples.text()
        nsamplespops = self.lineSamplesPops.text()
        if ntotalpops and nsamplespops:
            if "-N " in text0:
                old = re.findall("-N[\s\d+]+", text0)[0].rstrip()
                text1 = text0.replace(old, "-N " + ntotalpops + " " + nsamplespops)
            else:
                text1 = text0 + " -N " + ntotalpops + " " + nsamplespops
        else:
            if "-N " in text0:
                old = re.findall("-N[\s\d+]+", text0)[0].rstrip()
                text1 = text0.replace(old, "")
            else:
                text1 = text0
        ntotalsamples = self.lineOrderSamples1.text()
        norder = self.lineOrderSamples2.text()
        if ntotalsamples and norder:
            if "-O " in text1:
                old = re.findall("-O[\s\d+]+", text1)[0].rstrip()
                text2 = text1.replace(old, "-O " + ntotalsamples + " " + norder)
            else:
                text2 = text1 + " -O " + ntotalsamples + " " + norder
        else:
            if "-O " in text1:
                old = re.findall("-O[\s\d+]+", text1)[0].rstrip()
                text2 = text1.replace(old, "")
            else:
                text2 = text1
        if self.checkUnknownPos.isChecked():
            if "-u 1" in text2:
                text3 = text2
            else:
                text3 = text2 + " -u 1"
        else:
            if "-u 1" in text2:
                text3 = text2.replace(" -u 1", "")
            else:
                text3 = text2
        if self.checkOutgroup.isChecked():
            if "-G 1" in text3:
                text4 = text3
            else:
                text4 = text3 + " -G 1"
        else:
            if "-G 1" in text3:
                text4 = text3.replace(" -G 1", "")
            else:
                text4 = text3
        if self.lineAltSpect.text():
            if "-A " in text4:
                old = re.findall("-A\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4
                text6 = text5.replace(old, "-A " + self.lineAltSpect.text())
            else:
                text5 = text4
                text6 = text5 + " -A " + self.lineAltSpect.text()
        else:
            if "-A " in text4:
                old = re.findall(" -A\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4.replace(old, "")
                if "-S " in text4:
                    old = re.findall(" -S\s[\w\.\/\_\-\(\)]+", text4)[0]
                    text6 = text5.replace(old, "")
                else:
                    text6 = text5
            else:
                text5 = text4
                text6 = text5
        if self.lineNullSpect.text():
            if "-S " in text6:
                old = re.findall("-S\s[\w\.\/\_\-\(\)]+", text6)[0]
                text7 = text6.replace(old, "-S " + self.lineNullSpect.text())
            else:
                text7 = text6 + " -S " + self.lineNullSpect.text()
        else:
            if "-S " in text6:
                old = re.findall(" -S\s[\w\.\/\_\-\(\)]+", text6)[0]
                text7 = text6.replace(old, "")
            else:
                text7 = text6
        if self.lineSeed.text():
            if "-s " in text7:
                old = re.findall("-s\s[\d]+", text7)[0]
                text8 = text7.replace(old, "-s " + self.lineSeed.text())
            else:
                text8 = text7 + " -s " + self.lineSeed.text()
        else:
            if "-s " in text7:
                old = re.findall(" -s\s[\d]+", text7)[0]
                text8 = text7.replace(old, "")
            else:
                text8 = text7
        if self.linePermWindows.text():
            if "-t " in text8:
                old = re.findall("-t\s[\d]+", text8)[0]
                text9 = text8.replace(old, "-t " + self.linePermWindows.text())
            else:
                text9 = text8 + " -t " + self.linePermWindows.text()
        else:
            if "-t " in text8:
                old = re.findall(" -t\s[\d]+", text8)[0]
                text9 = text8.replace(old, "")
            else:
                text9 = text8
        if self.lineScaffold.text():
            if "-n " in text9:
                old = re.findall("-n\s[\w\.\/\_\-\(\)]+", text9)[0]
                text10 = text9.replace(old, "-n " + self.lineScaffold.text())
            else:
                text10 = text9 + " -n " + self.lineScaffold.text()
        else:
            if "-n " in text9:
                old = re.findall(" -n\s[\w\.\/\_\-\(\)]+", text9)[0]
                text10 = text9.replace(old, "")
            else:
                text10 = text9
        self.commandRun.setText(textrest + "\n" + text10)

    def on_click_getscaffoldfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineScaffold.setText(filename)

    def on_click_getaltspecfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineAltSpect.setText(filename)

    def on_click_getnullspecfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineNullSpect.setText(filename)

    def on_click_getmaskmsfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineMaskMS.setText(filename)

    def on_click_getcoordtffile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineCoordTF.setText(filename)

    def on_click_getweightsfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineWeights.setText(filename)

    def on_click_getgfffile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineGFF.setText(filename)

    def on_click_getJoinfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputJoin.setText(filename)

    def on_click_getJoinParam(self):
        joinInput = self.lineInputJoin.text()

        if joinInput:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
       
            if self.radioMerge.isChecked():
                if "bin/mergetFasta" not in textall:
                    textall = textall + "\n./bin/mergetFasta/bin/mergetFasta"
                for line in textall.splitlines():
                    if "bin/mergetFasta" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line

                if "-i " in text0:
                    old = re.findall(" -i\s[\w\.\/\_\-\(\)]+", text0)[0]
                    text1 = text0.replace(old, " -i "  + self.lineInputJoin.text())
                else:
                    text1 = text0 + " -i " + self.lineInputJoin.text()
 
                if "-o " in text1:
                    old = re.findall(" -o\s[\w\.\/\_\-\(\)]+", text1)[0]
                    text = text1.replace(old, " -o "  + self.lineOutputJoin.text())
                else:
                    text = text1 + " -o " + self.lineOutputJoin.text()

            elif self.radioConcat.isChecked():
                for line in textall.splitlines():
                    if "bin/concatenate_tFasta" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line

                text = "sh bin/concatenate_tFasta/bin/concatenate_tFasta.sh " + self.lineInputJoin.text() + " " + self.lineOutputJoin.text()

            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getIndexfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputIndex.setText(filename)

    def on_click_getIndexParam(self):
        indexInput = self.lineInputIndex.text()

        if indexInput:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/indexingtfasta" not in textall:
                textall = textall + "\n./bin/indexingtFasta/bin/indexingtFasta"
            for line in textall.splitlines():
                if "bin/indexingtFasta" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

            if "-i " in text0:
                old = re.findall(" -i\s[\w\.\/\_\-\(\)]+", text0)[0]
                text1 = text0.replace(old, " -i "  + self.lineInputIndex.text())
            else:
                text1 = text0 + " -i " + self.lineInputIndex.text()
 
            self.commandRun.setText(textrest + "\n" + text1)

    def on_click_getConvfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputConv.setText(filename)

    def on_click_getScaffoldConvfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineScaffoldConv.setText(filename)

    def on_click_getMaskConvfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineMaskConv.setText(filename)

    def on_click_getCoordConvfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineCoordConv.setText(filename)

    def on_click_getWeightConvfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineWeightConv.setText(filename)

    def on_click_getConvParam(self):
        ConvInput = self.lineInputConv.text()
        ConvOutput = self.lineOutputConv.text()
        ConvScaffold = self.lineScaffoldConv.text()

        if ConvInput and ConvOutput and ConvScaffold:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/fastaconvtr" not in textall:
                textall = textall + "\n./bin/fastaconvtr/bin/fastaconvtr"
            for line in textall.splitlines():
                if "bin/fastaconvtr" in line:
                    text0 = line
                elif "bin/weight4tfa" in line:
                    textno = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

            if "-F " in text0:
                old = re.findall(" -F\s[\w]+", text0)[0]
                if self.radioFa2Fa.isChecked() or self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked():
                    text1 = text0.replace(old, " -F fasta")
                elif self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked():
                    text1 = text0.replace(old, " -F tfasta")
            else:
                if self.radioFa2Fa.isChecked() or self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked():
                    text1 = text0 + " -F fasta"
                elif self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked():
                    text1 = text0 + " -F tfasta"

            if "-f " in text1:
                old = re.findall(" -f\s[\w]+", text1)[0]
                if self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked():
                    text2 = text1.replace(old, " -f fasta")
                elif self.radioFa2tFa.isChecked():
                    text2 = text1.replace(old, " -f tfasta")
                elif self.radioFa2ms.isChecked() or self.radiotFa2ms.isChecked():
                    text2 = text1.replace(old, " -f ms")
            else:
                if self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked():
                    text2 = text1 + " -f fasta"
                elif self.radioFa2tFa.isChecked():
                    text2 = text1 + " -f tfasta"
                elif self.radioFa2ms.isChecked() or self.radiotFa2ms.isChecked():
                    text2 = text1 + " -f ms"

            if "-i " in text2:
                old = re.findall(" -i\s[\w\.\/\_\-\(\)]+", text2)[0]
                text3 = text2.replace(old, " -i "  + self.lineInputConv.text())
            else:
                text3 = text2 + " -i " + self.lineInputConv.text()

            if "-o " in text3:
                old = re.findall(" -o\s[\w\.\/\_\-\(\)]+", text3)[0]
                text4 = text3.replace(old, " -o "  + self.lineOutputConv.text())
            else:
                text4 = text3 + " -o " + self.lineOutputConv.text()

            if "-n " in text4:
                old = re.findall(" -n\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4.replace(old, " -n "  + self.lineScaffoldConv.text())
            else:
                text5 = text4 + " -n " + self.lineScaffoldConv.text()

            if self.lineMaskConv.text():
                if "-m " in text5:
                    old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text5)[0]
                    text6 = text5.replace(old, " -m "  + self.lineMaskConv.text())
                else:
                    text6 = text5 + " -m " + self.lineMaskConv.text()
            else:
                if "-m " in text5:
                    old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text5)[0]
                    text6 = text5.replace(old, "")
                else:
                    text6 = text5

            if self.lineCoordConv.text():
                if "-W " in text6:
                    old = re.findall(" -W\s[\w\.\/\_\-\(\)]+", text6)[0]
                    text7 = text6.replace(old, " -W "  + self.lineCoordConv.text())
                else:
                    text7 = text6 + " -W " + self.lineCoordConv.text()
            else:
                if "-W " in text6:
                    old = re.findall(" -W\s[\w\.\/\_\-\(\)]+", text6)[0]
                    text7 = text6.replace(old, "")
                else:
                    text7= text6

            if self.lineWeightConv.text():
                if "-E " in text7:
                    old = re.findall(" -E\s[\w\.\/\_\-\(\)]+", text7)[0]
                    text8 = text7.replace(old, " -E "  + self.lineCoordConv.text())
                else:
                    text8 = text7 + " -E " + self.lineCoordConv.text()
            else:
                if "-E " in text7:
                    old = re.findall(" -E\s[\w\.\/\_\-\(\)]+", text7)[0]
                    text8 = text7.replace(old, "")
                else:
                    text8 = text7

            if "-P " in text8:
                old = re.findall(" -P\s\d", text8)[0]
                if self.radioWindowLengthConv1.isChecked():
                    text9 = text8.replace(old, " -P 1")
                elif self.radioWindowLengthConv2.isChecked():
                    text9 = text8.replace(old, " -P 0")
                else:
                    self.radioWindowLengthConv1.setChecked(True)
                    text9 = text8.replace(old, " -P 1")
            else:
                if self.radioWindowLengthConv1.isChecked():
                    text9 = text8 + " -P 1"
                elif self.radioWindowLengthConv2.isChecked():
                    text9 = text8 + " -P 0"
                else:
                    self.radioWindowLengthConv1.setChecked(True)
                    text9 = text8 + " -P 1"

            ntotalpops = self.lineTotalPopsConv.text()
            nsamplespops = self.lineSamplesPopsConv.text()
            if ntotalpops and nsamplespops:
                if "-N " in text9:
                    old = re.findall("-N[\s\d+]+", text9)[0].rstrip()
                    text10 = text9.replace(old, "-N " + ntotalpops + " " + nsamplespops)
                else:
                    text10 = text9 + " -N " + ntotalpops + " " + nsamplespops
            else:
                if "-N " in text9:
                    old = re.findall("-N[\s\d+]+", text9)[0].rstrip()
                    text10 = text9.replace(old, "")
                else:
                    text10 = text9
    
            ntotalsamples = self.lineOrderSamplesConv.text()
            norder = self.lineOrderSamplesConv2.text()
            if ntotalsamples and norder:
                if "-O " in text10:
                    old = re.findall("-O[\s\d+]+", text10)[0].rstrip()
                    text11 = text10.replace(old, "-O " + ntotalsamples + " " + norder)
                else:
                    text11 = text10 + " -O " + ntotalsamples + " " + norder
            else:
                if "-O " in text10:
                    old = re.findall("-O[\s\d+]+", text10)[0].rstrip()
                    text11 = text10.replace(old, "")
                else:
                    text11 = text10

            if self.checkUnknownPosConv.isChecked():
                if "-u 1" in text11:
                    text12 = text11
                else:
                    text12 = text11 + " -u 1"
            else:
                if "-u 1" in text11:
                    text12 = text11.replace(" -u 1", "")
                else:
                    text12 = text11
    
            if self.checkOutgroupConv.isChecked():
                if "-G 1" in text12:
                    text13 = text12
                else:
                    text13 = text12 + " -G 1"
            else:
                if "-G 1" in text12:
                    text13 = text12.replace(" -G 1", "")
                else:
                    text13 = text12

            if self.checkWindowSizeConv.isChecked():
                if "-w " in text13:
                    old = re.findall(" -w\s[\d]+", text13)[0]
                    text14 = text13.replace(old, " -w "  + self.lineWindowSizeConv.text())
                else:
                    text14 = text13 + " -w " + self.lineWindowSizeConv.text()
            else:
                if "-w " in text13:
                    old = re.findall(" -w\s[\d]+", text13)[0]
                    text14 = text13.replace(old, "")
                else:
                    text14 = text13

            if self.checkSlideConv.isChecked():
                if "-s " in text14:
                    old = re.findall(" -s\s[\d]+", text14)[0]
                    text15 = text14.replace(old, " -s "  + self.lineSlideConv.text())
                else:
                    text15 = text14 + " -s " + self.lineSlideConv.text()
            else:
                if "-s " in text14:
                    old = re.findall(" -s\s[\d]+", text14)[0]
                    text15 = text14.replace(old, "")
                else:
                    text15 = text14

            if self.checkIUPACConv.isChecked():
                if "-p " in text15:
                    old = re.findall(" -p\s\d", text15)[0]
                    text = text15.replace(old, " -p 2")
                else:
                    text = text15 + " -p 2"
            else:
                if "-p " in text15:
                    old = re.findall(" -p\s\d", text15)[0]
                    text = text15.replace(old, "")
                else:
                    text = text15

            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getWeightfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputWeight.setText(filename)

    def on_click_getgffWeightfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineGFFWeight.setText(filename)

    def on_click_getMaskWeightfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineMaskWeight.setText(filename)

    def on_click_getRegionsWeightfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineRegionsWeight.setText(filename)

    def on_click_getScaffoldWeightfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineScaffoldWeight.setText(filename)

    def on_click_getWeightParam(self):
        weightInput = self.lineInputWeight.text()
        weightOutput = self.lineOutputWeight.text()
        weightScaffold = self.lineOutputWeight.text()

        ConvInput = self.lineInputConv.text()
        ConvOutput = self.lineOutputConv.text()
        ConvScaffold = self.lineOutputConv.text()

        if weightInput and weightOutput and weightScaffold:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/weight4tfa" not in textall:
                textall = textall + "\n./bin/weight4tfa/bin/weight4tfa"
            for line in textall.splitlines():
                if "bin/weight4tfa" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

            if "-i " in text0:
                old = re.findall(" -i\s[\w\.\/\_\-\(\)]+", text0)[0]
                text1 = text0.replace(old, " -i "  + self.lineInputWeight.text())
            else:
                text1 = text0 + " -i " + self.lineInputWeight.text()

            if "-o " in text1:
                old = re.findall(" -o\s[\w\.\/\_\-\(\)]+", text1)[0]
                text2 = text1.replace(old, " -o "  + self.lineOutputWeight.text())
            else:
                text2 = text1 + " -o " + self.lineOutputWeight.text()

            if self.lineOutgroupWeight.text() and self.checkOutgroupWeight.isChecked():
                if "-G " in text2:
                    old = re.findall(" -G\s\d", text2)[0]
                    text3 = text2.replace(old, " -G "  + self.lineOutgroupWeight.text())
                else:
                    text3 = text2 + " -G " + self.lineOutgroupWeight.text()
            else:
                if "-G " in text2:
                    old = re.findall(" -G\s\d", text2)[0]
                    text3 = text2.replace(old, "")
                else:
                    text3 = text2

            if "-n " in text3:
                old = re.findall(" -n\s[\w\.\/\_\-\(\)]+", text3)[0]
                text4 = text3.replace(old, " -n "  + self.lineScaffoldWeight.text())
            else:
                text4 = text3 + " -n " + self.lineScaffoldWeight.text()

            if self.lineMaskWeight.text():
                if "-m " in text4:
                    old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text4)[0]
                    text5 = text4.replace(old, " -m "  + self.lineMaskWeight.text())
                else:
                    text5 = text4 + " -m " + self.lineMaskWeight.text()
            else:
                if "-m " in text4:
                    old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text4)[0]
                    text5 = text4.replace(old, "")
                else:
                    text5 = text4

            if self.lineRegionsWeight.text() and self.checkRegionsWeight.isChecked():
                if "-C " in text5:
                    old = re.findall(" -C\s[\w\.\/\_\-\(\)]+", text5)[0]
                    text6 = text5.replace(old, " -C "  + self.lineRegionsWeight.text())
                else:
                    text6 = text5 + " -C " + self.lineRegionsWeight.text()
            else:
                if "-C " in text5:
                    old = re.findall(" -C\s[\w\.\/\_\-\(\)]+", text5)[0]
                    text6 = text5.replace(old, "")
                else:
                    text6 = text5

            gff = self.lineGFFWeight.text()
            gfftype = self.lineTypeWeight.text()

            if gff:
                if gfftype:
                    if "-g " in text6:
                        if self.radioCode1Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                            else:
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                        elif self.radioCode2Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                            else:
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                        elif self.radioCode3Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                            else:
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                        elif self.radioCode4Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c max")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c max")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c min")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c min")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c long")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c long")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c first")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c first")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            else:
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text())
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    if self.lineCode4Weight.text():
                                        text = text6.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text())
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                        else:
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype + " -c first")
                            else:
                                if "-c " in text6:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype)
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                                    text = text6.replace(old, "-g " + gff + " " + gfftype)
                    else:
                        if self.radioCode1Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first"
                            else:
                                text = text6 + " -g " + gff + " " + gfftype + " Nuclear_Universal"
                        elif self.radioCode2Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first"
                            else:
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila"
                        elif self.radioCode3Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first"
                            else:
                                text = text6 + " -g " + gff + " " + gfftype + " mtDNA_Mammals"
                        elif self.radioCode4Weight.isChecked():
                            if self.lineCode4Weight.text():
                                text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text()
                                if self.radioMaxWeight.isChecked():
                                    text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c max"
                                elif self.radioMinWeight.isChecked():
                                    text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c min"
                                elif self.radioLongWeight.isChecked():
                                    text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c long"
                                elif self.radioFirstWeight.isChecked():
                                    text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c first"
                                else:
                                    text = text6 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text()
                            else:
                                print("Error: Code for the 64 triplets is not introduced")
                        else:
                            if self.radioMaxWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text6 + " -g " + gff + " " + gfftype + " -c first"
                            else:
                                text = text6 + " -g " + gff + " " + gfftype
                else:
                    if "-g " in text6:
                        if "-c " in text6:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                            text = text6.replace(old, "-g " + gff)
                        else:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                            text = text6.replace(old, "-g " + gff)
                    else:
                        text = text6 + " -g " + gff
            else:
                if self.checkGFFWeight.isChecked():
                    print("Error: 'GFF file' checked but without any selected file")
                else:
                    if "-g " in text6:
                        if "-c " in text6:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text6)[0]
                            text = text6.replace(old.lstrip(), "")
                        else:
                            old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text6)[0]
                            text = text6.replace(old.lstrip(), "")
                    else:
                        text = text6

            self.commandRun.setText(textrest + "\n" + text)

        elif ConvInput and ConvOutput and ConvScaffold and ( self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked() or self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked() ) and self.checkConversion.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/fastaconvtr" not in textall:
                textall = textall + "\n./bin/fastaconvtr/bin/fastaconvtr"
            for line in textall.splitlines():
                if "bin/fastaconvtr" in line:
                    text0 = line
                elif "bin/weight4tfa" in line:
                    textno = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

            gff = self.lineGFFWeight.text()
            gfftype = self.lineTypeWeight.text()

            if gff:
                if gfftype:
                    if "-g " in text0:
                        if self.radioCode1Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                            else:
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                        elif self.radioCode2Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                            else:
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                        elif self.radioCode3Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                            else:
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                        elif self.radioCode4Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c max")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c max")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c min")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c min")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c long")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c long")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c first")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text() + " -c first")
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                            else:
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text())
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    if self.lineCode4Weight.text():
                                        text = text0.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4Weight.text())
                                    else:
                                        print("Error: Code for the 64 triplets is not introduced")
                        else:
                            if self.radioMaxWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c max")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c max")
                            elif self.radioMinWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c min")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c min")
                            elif self.radioLongWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c long")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c long")
                            elif self.radioFirstWeight.isChecked():
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c first")
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype + " -c first")
                            else:
                                if "-c " in text0:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype)
                                else:
                                    old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                                    text = text0.replace(old, "-g " + gff + " " + gfftype)
                    else:
                        if self.radioCode1Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first"
                            else:
                                text = text0 + " -g " + gff + " " + gfftype + " Nuclear_Universal"
                        elif self.radioCode2Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first"
                            else:
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila"
                        elif self.radioCode3Weight.isChecked():
                            if self.radioMaxWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first"
                            else:
                                text = text0 + " -g " + gff + " " + gfftype + " mtDNA_Mammals"
                        elif self.radioCode4Weight.isChecked():
                            if self.lineCode4Weight.text():
                                text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text()
                                if self.radioMaxWeight.isChecked():
                                    text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c max"
                                elif self.radioMinWeight.isChecked():
                                    text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c min"
                                elif self.radioLongWeight.isChecked():
                                    text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c long"
                                elif self.radioFirstWeight.isChecked():
                                    text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text() + " -c first"
                                else:
                                    text = text0 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4Weight.text()
                            else:
                                print("Error: Code for the 64 triplets is not introduced")
                        else:
                            if self.radioMaxWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " -c max"
                            elif self.radioMinWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " -c min"
                            elif self.radioLongWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " -c long"
                            elif self.radioFirstWeight.isChecked():
                                text = text0 + " -g " + gff + " " + gfftype + " -c first"
                            else:
                                text = text0 + " -g " + gff + " " + gfftype
                else:
                    if "-g " in text0:
                        if "-c " in text0:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                            text = text0.replace(old, "-g " + gff)
                        else:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                            text = text0.replace(old, "-g " + gff)
                    else:
                        text = text0 + " -g " + gff
            else:
                if self.checkGFFWeight.isChecked():
                    print("Error: 'GFF file' checked but without any selected file")
                else:
                    if "-g " in text0:
                        if "-c " in text0:
                            old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text0)[0]
                            text = text0.replace(old.lstrip(), "")
                        else:
                            old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0]
                            text = text0.replace(old.lstrip(), "")
                    else:
                        text = text0

            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getVCFfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputVCF.setText(filename)

    def on_click_getRefFastafile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineInputRefFasta.setText(filename)

    def on_click_getScaffoldVCFfile(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(self,'Open Input file')
        if filename:
            self.lineScaffoldVCF.setText(filename)

    def on_click_getVCFParam(self):
        vcfInput = self.lineInputVCF.text()
        vcfOutput = self.lineOutputVCF.text()
        refInput = self.lineInputRefFasta.text()
        scaffInput = self.lineScaffoldVCF.text()

        if vcfInput and refInput and scaffInput and vcfOutput:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/gVCF2tFasta" not in textall:
                textall = textall + "\n./bin/gVCF2tFasta/bin/gVCF2tFasta"
            for line in textall.splitlines():
                if "bin/gVCF2tFasta" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

            if "-v " in text0:
                old = re.findall(" -v\s[\w\.\/\_\-\(\)]+", text0)[0]
                text1 = text0.replace(old, " -v "  + self.lineInputVCF.text())
            else:
                text1 = text0 + " -v " + self.lineInputVCF.text()

            if "-r " in text1:
                old = re.findall(" -r\s[\w\.\/\_\-\(\)]+", text1)[0]
                text2 = text1.replace(old, " -r "  + self.lineInputRefFasta.text())
            else:
                text2 = text1 + " -r " + self.lineInputRefFasta.text()

            if "-o " in text2:
                old = re.findall(" -o\s[\w\.\/\_\-\(\)]+", text2)[0]
                text3 = text2.replace(old, " -o "  + self.lineOutputVCF.text())
            else:
                text3 = text2 + " -o " + self.lineOutputVCF.text()
 
            if "-n " in text3:
                old = re.findall(" -n\s[\w\.\/\_\-\(\)]+", text3)[0]
                text = text3.replace(old, " -n "  + self.lineScaffoldVCF.text())
            else:
                text = text3 + " -n " + self.lineScaffoldVCF.text()
 
            self.commandRun.setText(textrest + "\n" + text)

    def on_click_getMSParam(self):
        mslength = self.lineMSlength.text()
        msiter = self.lineMSiter.text()
        msratio = self.lineMSratio.text()
        msRev = self.lineMSRev.text()
        msMask = self.lineMaskMS.text()

        if mslength:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line


            if "-l " in text0:
                old = re.findall("-l\s[\d]+", text0)[0]
                text1 = text0.replace(old, "-l " + mslength)
            else:
                text1 = text0 + " -l " + mslength

            if msiter:
                if "-r " in text1:
                    old = re.findall("-r\s[\d]+", text1)[0]
                    text2 = text1.replace(old, "-r " + msiter)
                else:
                    text2 = text1 + " -r " + msiter
            else:
                if self.checkMSiter.isChecked():
                    print("Error: 'ms iterations' checked but without any value")
                else:
                    if "-r " in text0:
                        old = re.findall(" -r\s[\d]+", text1)[0]
                        text2 = text1.replace(old.lstrip(), "")
                    else:
                        text2 = text1

            if msratio:
                if "-v " in text2:
                    old = re.findall("-v\s\d+\.\d+|-v\s\d+", text2)[0]
                    text3 = text2.replace(old, "-v " + msratio)
                else:
                    text3 = text2 + " -v " + msratio
            else:
                if self.checkMSratio.isChecked():
                    print("Error: 'Ratio transitions/tranversions' checked but without any value")
                else:
                    if "-v " in text0:
                        old = re.findall(" -v\s\d+\.\d+|-v\s\d+", text2)[0]
                        text3 = text2.replace(old.lstrip(), "")
                    else:
                        text3 = text2

            if msRev:
                if "-q " in text3:
                    old = re.findall("-q\s\d+\.\d+|-q\s\d+", text3)[0]
                    text4 = text3.replace(old, "-q " + msRev)
                else:
                    text4 = text3 + " -q " + msRev
            else:
                if self.checkMSRev.isChecked():
                    print("Error: 'Frequency of reverted mutations' checked but without any value")
                else:
                    if "-q " in text3:
                        old = re.findall(" -q\s\d+\.\d+|-q\s\d+", text3)[0]
                        text4 = text3.replace(old.lstrip(), "")
                    else:
                        text4 = text3

            if msMask:
                if "-m " in text4:
                    old = re.findall("-m\s[\w\.\/\_\-\(\)]+", text4)[0]
                    text5 = text4.replace(old, "-m " + msMask)
                else:
                    text5 = text4 + " -m " + msMask
            else:
                if self.checkMaskMS.isChecked():
                    print("Error: 'Include mask' checked but without any selected file")
                else:
                    if "-m " in text4:
                        old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text4)[0]
                        text5 = text4.replace(old.lstrip(), "")
                    else:
                        text5 = text4

            if self.checkMSoutgroup.isChecked():
                if "-F " in text5:
                    old = re.findall("-F\s\d", text5)[0]
                    text6 = text5.replace(old, "-F 1")
                else:
                    text6 = text5 + " -F 1"
            else:
                if "-F " in text5:
                    old = re.findall(" -F\s\d", text5)[0]
                    text6 = text5.replace(old.lstrip(), "")
                else:
                    text6 = text5

            self.commandRun.setText(textrest + "\n" + text6)

    def on_click_getFastaParam(self):

        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        if "bin/mstatspop" not in textall:
            textall = textall + "\n./bin/mstatspop/bin/mstatspop"
        for line in textall.splitlines():
            if "bin/mstatspop" in line:
                text0 = line
            else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

        if self.checkIUPACFasta.isChecked():
            if "-p " in text0:
                old = re.findall("-p\s\d", text0)[0]
                text1 = text0.replace(old, "-p 2")
            else:
                text1 = text0 + " -p 2"
        else:
            if "-p " in text0:
                old = re.findall(" -p\s\d", text0)[0]
                text1 = text0.replace(old, "")
            else:
                text1 = text0

        if self.checkMaskFasta.isChecked():
            if "-K " in text1:
                old = re.findall("-K\s\d", text1)[0]
                text2 = text1.replace(old, "-K 1")
            else:
                text2 = text1 + " -K 1"
        else:
            if "-K " in text1:
                old = re.findall(" -K\s\d", text1)[0]
                text2 = text1.replace(old, "")
            else:
                text2 = text1

        gff = self.lineGFF.text()
        gfftype = self.lineType.text()

        if gff:
            if gfftype:
                if "-g " in text2:
                    if self.radioCode1.isChecked():
                        if self.radioMax.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max")
                        elif self.radioMin.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min")
                        elif self.radioLong.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long")
                        elif self.radioFirst.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first")
                        else:
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Nuclear_Universal")
                    elif self.radioCode2.isChecked():
                        if self.radioMax.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max")
                        elif self.radioMin.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min")
                        elif self.radioLong.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long")
                        elif self.radioFirst.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first")
                        else:
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Drosophila")
                    elif self.radioCode3.isChecked():
                        if self.radioMax.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max")
                        elif self.radioMin.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min")
                        elif self.radioLong.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long")
                        elif self.radioFirst.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first")
                        else:
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " mtDNA_Mammals")
                    elif self.radioCode4.isChecked():
                        if self.radioMax.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c max")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c max")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                        elif self.radioMin.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c min")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c min")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                        elif self.radioLong.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c long")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c long")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                        elif self.radioFirst.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c first")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text() + " -c first")
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                        else:
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text())
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                if self.lineCode4.text():
                                    text3 = text2.replace(old, "-g " + gff + " " + gfftype + " Other " + self.lineCode4.text())
                                else:
                                    print("Error: Code for the 64 triplets is not introduced")
                    else:
                        if self.radioMax.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c max")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c max")
                        elif self.radioMin.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c min")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c min")
                        elif self.radioLong.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c long")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c long")
                        elif self.radioFirst.isChecked():
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c first")
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype + " -c first")
                        else:
                            if "-c " in text2:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype)
                            else:
                                old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                                text3 = text2.replace(old, "-g " + gff + " " + gfftype)
                else:
                    if self.radioCode1.isChecked():
                        if self.radioMax.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c max"
                        elif self.radioMin.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c min"
                        elif self.radioLong.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c long"
                        elif self.radioFirst.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " Nuclear_Universal" + " -c first"
                        else:
                            text3 = text2 + " -g " + gff + " " + gfftype + " Nuclear_Universal"
                    elif self.radioCode2.isChecked():
                        if self.radioMax.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c max"
                        elif self.radioMin.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c min"
                        elif self.radioLong.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c long"
                        elif self.radioFirst.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila" + " -c first"
                        else:
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Drosophila"
                    elif self.radioCode3.isChecked():
                        if self.radioMax.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c max"
                        elif self.radioMin.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c min"
                        elif self.radioLong.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c long"
                        elif self.radioFirst.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Mammals" + " -c first"
                        else:
                            text3 = text2 + " -g " + gff + " " + gfftype + " mtDNA_Mammals"
                    elif self.radioCode4.isChecked():
                        if self.lineCode4.text():
                            text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text()
                            if self.radioMax.isChecked():
                                text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text() + " -c max"
                            elif self.radioMin.isChecked():
                                text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text() + " -c min"
                            elif self.radioLong.isChecked():
                                text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text() + " -c long"
                            elif self.radioFirst.isChecked():
                                text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text() + " -c first"
                            else:
                                text3 = text2 + " -g " + gff + " " + gfftype + " Other" + self.lineCode4.text()
                        else:
                            print("Error: Code for the 64 triplets is not introduced")
                    else:
                        if self.radioMax.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " -c max"
                        elif self.radioMin.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " -c min"
                        elif self.radioLong.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " -c long"
                        elif self.radioFirst.isChecked():
                            text3 = text2 + " -g " + gff + " " + gfftype + " -c first"
                        else:
                            text3 = text2 + " -g " + gff + " " + gfftype
            else:
                if "-g " in text2:
                    if "-c " in text2:
                        old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                        text3 = text2.replace(old, "-g " + gff)
                    else:
                        old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                        text3 = text2.replace(old, "-g " + gff)
                else:
                    text3 = text2 + " -g " + gff
        else:
            if self.checkGFF.isChecked():
                print("Error: 'GFF file' checked but without any selected file")
            else:
                if "-g " in text2:
                    if "-c " in text2:
                        old = re.findall("-g\s[\w\.\/\_\-\(\)]+[\s\w]+\s\-c\s[\w]+", text2)[0]
                        text3 = text2.replace(old.lstrip(), "")
                    else:
                        old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0]
                        text3 = text2.replace(old.lstrip(), "")
                else:
                    text3 = text2

        self.commandRun.setText(textrest + "\n" + text3)

    def on_click_getTFastaParam(self):

        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        if "bin/mstatspop" not in textall:
            textall = textall + "\n./bin/mstatspop/bin/mstatspop"
        for line in textall.splitlines():
            if "bin/mstatspop" in line:
                text0 = line
            else:
                if textrest == "":
                    textrest = line
                else:
                    textrest += "\n" + line

        if self.radioWindowSize.isChecked():
            if self.lineWindowSize.text():
                if "-w " in text0:
                    old = re.findall("-w\s\d+", text0)[0]
                    text1 = text0.replace(old, "-w " + self.lineWindowSize.text())
                elif "-W " in text0:
                    old = re.findall("-W\s[\w\.\/\_\-\(\)]+", text0)[0]
                    text1 = text0.replace(old, "-w " + self.lineWindowSize.text())
                else:
                    text1 = text0 + " -w " + self.lineWindowSize.text()
            else:
                print("Error: 'Window Size' checked but without any value")
        elif self.radioCoordTF.isChecked():
            self.lineWindowSize.setText("")
            if self.lineCoordTF.text():
                if "-w " in text0:
                    old = re.findall("-w\s\d+", text0)[0]
                    text1 = text0.replace(old, "-W " + self.lineCoordTF.text())
                elif "-W " in text0:
                    old = re.findall("-W\s[\w\.\/\_\-\(\)]+", text0)[0]
                    text1 = text0.replace(old, "-W " + self.lineCoordTF.text())
                else:
                    text1 = text0 + " -W " + self.lineCoordTF.text()
            else:
                print("Error: 'File with coordinates of each windows' checked but without any selected file")

        if self.checkSlide.isChecked():
            if self.lineSlide.text():
                if "-z " in text1:
                    old = re.findall("-z\s\d+", text1)[0]
                    text2 = text1.replace(old, "-z " + self.lineSlide.text())
                else:
                    text2 = text1 + " -z " + self.lineSlide.text()
            else:
                print("Error: 'Slide Size' checked but without any value")
        else:
            self.lineSlide.setText("")
            if "-z " in text1:
                old = re.findall(" -z\s\d+", text1)[0]
                text2 = text1.replace(old, "")
            else:
                text2 = text1

        if self.checkFirstWindowTF.isChecked():
            if self.lineFirstWindowTF.text():
                if "-Z " in text2:
                    old = re.findall("-Z\s\d", text2)[0]
                    text3 = text2.replace(old, "-Z " + self.lineFirstWindowTF.text())
                else:
                    text3 = text2 + " -Z " + self.lineFirstWindowTF.text()
            else:
                print("Error: 'First window size displacement' checked but without any value")
        else:
            self.lineFirstWindowTF.setText("")
            if "-Z " in text2:
                old = re.findall(" -Z\s\d", text2)[0]
                text3 = text2.replace(old, "")
            else:
                text3 = text2

        if self.radioWindowLengthTF1.isChecked():
            if "-Y " in text3:
                old = re.findall("-Y\s\d", text3)[0]
                text4 = text3.replace(old, "-Y 1")
            else:
                text4 = text3 + " -Y 1"
        elif self.radioWindowLengthTF2.isChecked():
            if "-Y " in text3:
                old = re.findall("-Y\s\d", text3)[0]
                text4 = text3.replace(old, "-Y 0")
            else:
                text4 = text3 + " -Y 0"
        else:
            if "-Y " in text3:
                old = re.findall("-Y\s\d", text3)[0]
                text4 = text3.replace(old, "")
            else:
                text4 = text3

        if self.lineWeights.text():
            if "-E " in text4:
                old = re.findall("-E\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4.replace(old, "-E " + self.lineWeights.text())
            else:
                text5 = text4 + " -E " + self.lineWeights.text()
        else:
            text5 = text4

        self.commandRun.setText(textrest + "\n" + text5)

    def btnstate_pre(self):

        ########################################
        ## Pre-Process File format conversion ##
        ########################################

        if self.checkConversion.isChecked():
            self.radioFa2tFa.setEnabled(True)
            self.radioFa2ms.setEnabled(True)
            self.radioFa2Fa.setEnabled(True)
            self.radiotFa2Fa.setEnabled(True)
            self.radiotFa2ms.setEnabled(True)
            self.radioVCF2tFa.setEnabled(True)
        else:
            self.radioFa2tFa.setChecked(False)
            self.radioFa2ms.setChecked(False)
            self.radioFa2Fa.setChecked(False)
            self.radiotFa2Fa.setChecked(False)
            self.radiotFa2ms.setChecked(False)
            self.radioVCF2tFa.setChecked(False)
            self.radioFa2tFa.setEnabled(False)
            self.radioFa2ms.setEnabled(False)
            self.radioFa2Fa.setEnabled(False)
            self.radiotFa2Fa.setEnabled(False)
            self.radiotFa2ms.setEnabled(False)
            self.radioVCF2tFa.setEnabled(False)
            self.frameConversion.setEnabled(False)
            self.frameVCF.setEnabled(False)
            self.lineInputConv.setText("")
            self.lineOutputConv.setText("")
            self.lineScaffoldConv.setText("")
            self.lineMaskConv.setText("")
            self.lineCoordConv.setText("")
            self.lineWeightConv.setText("")
            self.lineTotalPopsConv.setText("")
            self.lineSamplesPopsConv.setText("")
            self.lineOrderSamplesConv.setText("")
            self.lineOrderSamplesConv2.setText("")
            self.lineWindowSizeConv.setText("")
            self.lineSlideConv.setText("")
            self.checkMaskConv.setChecked(False)
            self.checkCoordConv.setChecked(False)
            self.checkWeightConv.setChecked(False)
            self.checkOrderSamplesConv.setChecked(False)
            self.checkUnknownPosConv.setChecked(False)
            self.checkOutgroupConv.setChecked(False)
            self.checkWindowSizeConv.setChecked(False)
            self.checkSlideConv.setChecked(False)
            self.checkIUPACConv.setChecked(False)

        if ( self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked() or self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked() ) and self.checkConversion.isChecked():
            self.frameConversion.setEnabled(True)
            self.frameVCF.setEnabled(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/gVCF2tFasta" in textall:
                for line in textall.splitlines():
                    if "bin/gVCF2tFasta" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

                self.commandRun.setText(textrest)

            if self.radioFa2tFa.isChecked():
                self.checkCoordConv.setEnabled(False)
                self.checkCoordConv.setChecked(False)
                self.lineCoordConv.setEnabled(False)
                self.lineCoordConv.setText("")
                self.openCoordConv.setEnabled(False)                

            if self.radioFa2tFa.isChecked() or self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked():
                self.checkWindowSizeConv.setEnabled(False)
                self.checkWindowSizeConv.setChecked(False)
                self.lineWindowSizeConv.setEnabled(False)
                self.lineWindowSizeConv.setText("")
                self.checkSlideConv.setEnabled(False)
                self.checkSlideConv.setChecked(False)
                self.lineSlideConv.setEnabled(False)
                self.lineSlideConv.setText("")

            if self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked() or self.radioFa2ms.isChecked() or self.radiotFa2ms.isChecked():
                self.checkCoordConv.setEnabled(True)

            if self.radioFa2ms.isChecked() or self.radiotFa2ms.isChecked():
                self.checkWindowSizeConv.setEnabled(True)
                self.checkSlideConv.setEnabled(True)

            if self.radioFa2ms.isChecked() or self.radioFa2Fa.isChecked() or self.radioFa2tFa.isChecked():
                self.checkIUPACConv.setEnabled(True)

            if self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked():
                self.checkIUPACConv.setEnabled(False)
                self.checkIUPACConv.setChecked(False)

            if self.checkWeight.isChecked():
                self.checkWeightConv.setEnabled(False)
                self.checkWeightConv.setChecked(False)
                self.lineWeightConv.setEnabled(False)
                self.lineWeightConv.setText("")
                self.openWeightConv.setEnabled(False)
            else:
                self.checkWeightConv.setEnabled(True)

                textall = self.commandRun.toPlainText()
                text0 = ""
                textrest = ""
                if "bin/weight4tfa" in textall:
                    for line in textall.splitlines():
                        if "bin/weight4tfa" in line:
                            text0 = line
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line
    
                    self.commandRun.setText(textrest)

                textall = self.commandRun.toPlainText()
                text0 = ""
                textrest = ""
                if "bin/fastaconvtr" in textall:
                    for line in textall.splitlines():
                        if "bin/fastaconvtr" in line:
                            text0 = line
                            if "-g " in text0:
                                old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text0)[0].rstrip()
                                text1 = text0.replace(old, "")
                            else:
                                text1 = text0
                            if "-c " in text1:
                                old = re.findall(" -c\s[\w]+", text1)[0].rstrip()
                                text2 = text1.replace(old, "")
                            else:
                                text2 = text1
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line
    
                    self.commandRun.setText(text2 + "\n" + textrest)

            if self.checkMaskConv.isChecked():
                self.lineMaskConv.setEnabled(True)
                self.openMaskConv.setEnabled(True)
            else:
                self.lineMaskConv.setEnabled(False)
                self.lineMaskConv.setText("")
                self.openMaskConv.setEnabled(False)

            if self.checkCoordConv.isChecked():
                self.lineCoordConv.setEnabled(True)
                self.openCoordConv.setEnabled(True)
            else:
                self.lineCoordConv.setEnabled(False)
                self.lineCoordConv.setText("")
                self.openCoordConv.setEnabled(False)

            if self.checkWeightConv.isChecked():
                self.lineWeightConv.setEnabled(True)
                self.openWeightConv.setEnabled(True)
            else:
                self.lineWeightConv.setEnabled(False)
                self.lineWeightConv.setText("")
                self.openWeightConv.setEnabled(False)

            if self.checkOrderSamplesConv.isChecked():
                self.labelOrderSamplesConv.setEnabled(True)
                self.lineOrderSamplesConv.setEnabled(True)
                self.labelOrderSamplesConv2.setEnabled(True)
                self.lineOrderSamplesConv2.setEnabled(True)
            else:
                self.labelOrderSamplesConv.setEnabled(False)
                self.lineOrderSamplesConv.setEnabled(False)
                self.lineOrderSamplesConv.setText("")
                self.labelOrderSamplesConv2.setEnabled(False)
                self.lineOrderSamplesConv2.setEnabled(False)
                self.lineOrderSamplesConv2.setText("")

            if self.checkWindowSizeConv.isChecked():
                self.lineWindowSizeConv.setEnabled(True)
            else:
                self.lineWindowSizeConv.setEnabled(False)
                self.lineWindowSizeConv.setText("")

            if self.checkSlideConv.isChecked():
                self.lineSlideConv.setEnabled(True)
            else:
                self.lineSlideConv.setEnabled(False)
                self.lineSlideConv.setText("")

        elif self.radioVCF2tFa.isChecked() and self.checkConversion.isChecked():
            self.frameVCF.setEnabled(True)
            self.frameConversion.setEnabled(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/fastaconvtr" in textall:
                for line in textall.splitlines():
                    if "bin/fastaconvtr" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

                self.commandRun.setText(textrest)
        else:
            self.frameConversion.setEnabled(False)
            self.frameVCF.setEnabled(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/gVCF2tFasta" in textall or "bin/fastaconvtr" in textall:
                for line in textall.splitlines():
                    if "bin/gVCF2tFasta" in line or "bin/fastaconvtr" in textall:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

                self.commandRun.setText(textrest)

        ####################################
        ## Pre-Process Weights parameters ##
        ####################################

        if self.checkWeight.isChecked():
            self.frameWeight.setEnabled(True)

            if self.checkGFFWeight.isChecked():
                self.lineGFFWeight.setEnabled(True)
                self.openGFFWeight.setEnabled(True)
                self.labelTypeWeight.setEnabled(True)
                self.lineTypeWeight.setEnabled(True)
                self.labelCodeWeight.setEnabled(True)
                self.radioCode1Weight.setEnabled(True)
                self.radioCode2Weight.setEnabled(True)
                self.radioCode3Weight.setEnabled(True)
                self.radioCode4Weight.setEnabled(True)
                self.lineCode4Weight.setEnabled(True)
                self.labelCriteriaWeight.setEnabled(True)
                self.radioFirstWeight.setEnabled(True)
                self.radioMinWeight.setEnabled(True)
                self.radioMaxWeight.setEnabled(True)
                self.radioLongWeight.setEnabled(True)
            else:
                self.lineGFFWeight.setEnabled(False)
                self.lineGFFWeight.setText("")
                self.openGFFWeight.setEnabled(False)
                self.labelTypeWeight.setEnabled(False)
                self.lineTypeWeight.setEnabled(False)
                self.lineTypeWeight.setText("")
                self.labelCodeWeight.setEnabled(False)
                self.radioCode1Weight.setEnabled(False)
                self.radioCode2Weight.setEnabled(False)
                self.radioCode3Weight.setEnabled(False)
                self.radioCode4Weight.setEnabled(False)
                self.lineCode4Weight.setEnabled(False)
                self.lineCode4Weight.setText("")
                self.labelCriteriaWeight.setEnabled(False)
                self.radioFirstWeight.setEnabled(False)
                self.radioMinWeight.setEnabled(False)
                self.radioMaxWeight.setEnabled(False)
                self.radioLongWeight.setEnabled(False)
    
            if ( self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked() or self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked() ) and self.checkConversion.isChecked():
                self.labelInputWeight.setEnabled(False)
                self.lineInputWeight.setEnabled(False)
                self.lineInputWeight.setText("")
                self.openInputWeight.setEnabled(False)
                self.labelOutputWeight.setEnabled(False)
                self.lineOutputWeight.setEnabled(False)
                self.lineOutputWeight.setText("")
                self.labelScaffoldWeight.setEnabled(False)
                self.lineScaffoldWeight.setEnabled(False)
                self.lineScaffoldWeight.setText("")
                self.openScaffoldWeight.setEnabled(False)
                self.checkOutgroupWeight.setEnabled(False)
                self.checkOutgroupWeight.setChecked(False)
                self.labelOutgroupWeight.setEnabled(False)
                self.lineOutgroupWeight.setEnabled(False)
                self.lineOutgroupWeight.setText("")
                self.checkMaskWeight.setEnabled(False)
                self.checkMaskWeight.setChecked(False)
                self.lineMaskWeight.setEnabled(False)
                self.lineMaskWeight.setText("")
                self.openMaskWeight.setEnabled(False)
                self.checkRegionsWeight.setEnabled(False)
                self.checkRegionsWeight.setChecked(False)
                self.lineRegionsWeight.setEnabled(False)
                self.lineRegionsWeight.setText("")
                self.openRegionsWeight.setEnabled(False)
            else:
                self.labelInputWeight.setEnabled(True)
                self.lineInputWeight.setEnabled(True)
                self.labelOutputWeight.setEnabled(True)
                self.lineOutputWeight.setEnabled(True)
                self.openInputWeight.setEnabled(True)
                self.labelScaffoldWeight.setEnabled(True)
                self.lineScaffoldWeight.setEnabled(True)
                self.openScaffoldWeight.setEnabled(True)
                self.checkOutgroupWeight.setEnabled(True)
                self.checkMaskWeight.setEnabled(True)
                self.checkRegionsWeight.setEnabled(True)

            if self.checkMaskWeight.isChecked():
                self.lineMaskWeight.setEnabled(True)
                self.openMaskWeight.setEnabled(True)
            else:
                self.lineMaskWeight.setEnabled(False)
                self.lineMaskWeight.setText("")
                self.openMaskWeight.setEnabled(False)
   
            if self.checkRegionsWeight.isChecked():
                self.lineRegionsWeight.setEnabled(True)
                self.openRegionsWeight.setEnabled(True)
            else:
                self.lineRegionsWeight.setEnabled(False)
                self.lineRegionsWeight.setText("")
                self.openRegionsWeight.setEnabled(False)
    
            if self.checkOutgroupWeight.isChecked():
                self.lineOutgroupWeight.setEnabled(True)
                self.labelOutgroupWeight.setEnabled(True)
            else:
                self.lineOutgroupWeight.setEnabled(False)
                self.lineOutgroupWeight.setText("")
                self.labelOutgroupWeight.setEnabled(False)

            if self.radioCode4Weight.isChecked():
                self.lineCode4Weight.setEnabled(True)
            else:
                self.lineCode4Weight.setEnabled(False)

        else:
            self.frameWeight.setEnabled(False)
            self.checkGFFWeight.setChecked(False)
            self.checkOutgroupWeight.setChecked(False)
            self.checkMaskWeight.setChecked(False)
            self.checkRegionsWeight.setChecked(False)
            self.lineInputWeight.setText("")
            self.lineOutputWeight.setText("")
            self.lineScaffoldWeight.setText("")
            self.lineGFFWeight.setText("")
            self.lineTypeWeight.setText("")
            self.lineCode4Weight.setText("")
            self.lineOutgroupWeight.setText("")
            self.lineMaskWeight.setText("")
            self.lineRegionsWeight.setText("")

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            textrest2 = ""

            if not ( self.radioFa2tFa.isChecked() or self.radioFa2ms.isChecked() or self.radioFa2Fa.isChecked() or self.radiotFa2Fa.isChecked() or self.radiotFa2ms.isChecked() ) and not self.checkConversion.isChecked():

                if "bin/weight4tfa" in textall:
                    for line in textall.splitlines():
                        if "bin/weight4tfa" in line:
                            text0 = line
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line

                    self.commandRun.setText(textrest)


            else:
                if "bin/weight4tfa" in textall:
                    for line in textall.splitlines():
                        if "bin/weight4tfa" in line:
                            text0 = line
                        else:
                            if textrest == "":
                                textrest = line
                            else:
                                textrest += "\n" + line

                    self.commandRun.setText(textrest)


        ################################
        ## Pre-Process Joining tFasta ##
        ################################

        if self.checkJoin.isChecked():
            self.radioMerge.setEnabled(True)
            self.radioConcat.setEnabled(True)
            self.frameJoin.setEnabled(True)
        else:
            self.radioMerge.setEnabled(False)
            self.radioConcat.setEnabled(False)
            self.radioMerge.setChecked(False)
            self.radioConcat.setChecked(False)
            self.frameJoin.setEnabled(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/concatenate_tFasta" in textall or "bin/mergetFasta" in textall:
                for line in textall.splitlines():
                    if "bin/concatenate_tFasta" in line or "bin/mergetFasta" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

                self.commandRun.setText(textrest)

        #################################
        ## Pre-Process Indexing tFasta ##
        #################################

        if self.checkIndex.isChecked():
            self.frameIndex.setEnabled(True)
        else:
            self.frameIndex.setEnabled(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/indexingtFasta" in textall:
                for line in textall.splitlines():
                    if "bin/indexingtFasta" in line:
                        text0 = line
                    else:
                        if textrest == "":
                            textrest = line
                        else:
                            textrest += "\n" + line

                self.commandRun.setText(textrest)

    def btnstate(self):
        if self.radioMS.isChecked():
            self.frameMS.setEnabled(True)
            self.frameFasta.setEnabled(False)
            self.frameTFasta.setEnabled(False)

            self.checkOrderSamples.setEnabled(False)
            self.labelOrderSamples1.setEnabled(False)
            self.lineOrderSamples1.setEnabled(False)
            self.labelOrderSamples2.setEnabled(False)
            self.lineOrderSamples2.setEnabled(False)
            self.checkPermWindows.setEnabled(False)
            self.linePermWindows.setEnabled(False)
            self.checkSeed.setEnabled(False)
            self.lineSeed.setEnabled(False)

            self.checkOrderSamples.setChecked(False)
            self.checkIUPACFasta.setChecked(False)
            self.checkMaskFasta.setChecked(False)
            self.checkGFF.setChecked(False)
            self.radioWindowSize.setChecked(False)
            self.radioCoordTF.setChecked(False)
            self.checkSlide.setChecked(False)
            self.checkFirstWindowTF.setChecked(False)
            self.radioWindowLengthTF1.setChecked(False)
            self.radioWindowLengthTF2.setChecked(False)
            self.lineWeights.setText("")

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-p " in text0:
                old = re.findall(" -p\s\d", text0)[0]
                text1 = text0.replace(old, "")
            else:
                text1 = text0
            if "-K " in text1:
                old = re.findall(" -K\s\d", text1)[0]
                text2 = text1.replace(old, "")
            else:
                text2 = text1
            if "-g " in text2:
                old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text2)[0].rstrip()
                text3 = text2.replace(old, "")
            else:
                text3 = text2
            if "-c " in text3:
                old = re.findall(" -c\s[\w]+", text3)[0].rstrip()
                text4 = text3.replace(old, "")
            else:
                text4 = text3
            if "-w " in text4:
                old = re.findall(" -w\s[\d]+", text4)[0].rstrip()
                text5 = text4.replace(old, "")
            else:
                text5 = text4
            if "-W " in text5:
                old = re.findall(" -W\s[\w\.\/\_\-\(\)]+", text5)[0]
                text6 = text5.replace(old, "")
            else:
                text6 = text5
            if "-z " in text6:
                old = re.findall(" -z\s[\d]+", text6)[0].rstrip()
                text7 = text6.replace(old, "")
            else:
                text7 = text6
            if "-Z " in text7:
                old = re.findall(" -Z\s[\d]+", text7)[0].rstrip()
                text8 = text7.replace(old, "")
            else:
                text8 = text7
            if "-Y " in text8:
                old = re.findall(" -Y\s\d", text8)[0].rstrip()
                text9 = text8.replace(old, "")
            else:
                text9 = text8
            if "-E " in text9:
                old = re.findall(" -E\s[\w\.\/\_\-\(\)]+", text9)[0]
                text10 = text9.replace(old, "")
            else:
                text10 = text9
            if "-s " in text10:
                old = re.findall(" -s\s[\d]+", text10)[0]
                text11 = text10.replace(old, "")
            else:
                text11 = text10
            if "-t " in text11:
                old = re.findall(" -t\s[\d]+", text11)[0]
                text12 = text11.replace(old, "")
            else:
                text12 = text11
            if "-O " in text12:
                old = re.findall(" -O[\s\d+]+", text12)[0]
                text13 = text12.replace(old, "")
            else:
                text13 = text12

            if "-f fasta" in text13:
                text = text13.replace("-f fasta", "-f ms")
            elif "-f tfa" in text13:
                text = text13.replace("-f tfa", "-f ms")
            elif "-f ms" in text13:
                text = text13
            else:
                text = text13 + " -f ms"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFasta.isChecked():
            self.frameFasta.setEnabled(True)
            self.frameMS.setEnabled(False)
            self.frameTFasta.setEnabled(False)

            self.checkOrderSamples.setEnabled(True)
            self.checkSeed.setEnabled(True)

            self.lineMSlength.setText("")
            self.checkMSiter.setChecked(False)
            self.checkMSratio.setChecked(False)
            self.checkMSRev.setChecked(False)
            self.checkMSoutgroup.setChecked(False)
            self.checkMaskMS.setChecked(False)
            self.radioWindowSize.setChecked(False)
            self.radioCoordTF.setChecked(False)
            self.checkSlide.setChecked(False)
            self.checkFirstWindowTF.setChecked(False)
            self.radioWindowLengthTF1.setChecked(False)
            self.radioWindowLengthTF2.setChecked(False)
            self.lineWeights.setText("")

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-l " in text0:
                old = re.findall(" -l\s[\d]+", text0)[0]
                text1 = text0.replace(old, "")
            else:
                text1 = text0
            if "-r " in text1:
                old = re.findall(" -r\s[\d]+", text1)[0]
                text2 = text1.replace(old, "")
            else:
                text2 = text1
            if "-v " in text2:
                old = re.findall(" -v\s\d+\.\d+|-v\s\d+", text2)[0]
                text3 = text2.replace(old, "")
            else:
                text3 = text2
            if "-q " in text3:
                old = re.findall(" -q\s\d+\.\d+|-q\s\d+", text3)[0]
                text4 = text3.replace(old, "")
            else:
                text4 = text3
            if "-m " in text4:
                old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4.replace(old, "")
            else:
                text5 = text4
            if "-F " in text5:
                old = re.findall(" -F\s\d", text5)[0]
                text6 = text5.replace(old, "")
            else:
                text6 = text5
            if "-w " in text6:
                old = re.findall(" -w\s[\d]+", text6)[0].rstrip()
                text7 = text6.replace(old, "")
            else:
                text7 = text6
            if "-W " in text7:
                old = re.findall(" -W\s[\w\.\/\_\-\(\)]+", text7)[0]
                text8 = text7.replace(old, "")
            else:
                text8 = text7
            if "-z " in text8:
                old = re.findall(" -z\s[\d]+", text8)[0].rstrip()
                text9 = text8.replace(old, "")
            else:
                text9 = text8
            if "-Z " in text9:
                old = re.findall(" -Z\s[\d]+", text9)[0].rstrip()
                text10 = text9.replace(old, "")
            else:
                text10 = text9
            if "-Y " in text10:
                old = re.findall(" -Y\s\d", text10)[0].rstrip()
                text11 = text10.replace(old, "")
            else:
                text11 = text10
            if "-E " in text11:
                old = re.findall(" -E\s[\w\.\/\_\-\(\)]+", text11)[0]
                text12 = text11.replace(old, "")
            else:
                text12 = text11

            if "-f ms" in text12:
                text = text12.replace("-f ms", "-f fasta")
            elif "-f tfa" in text12:
                text = text12.replace("-f tfa", "-f fasta")
            elif "-f fasta" in text12:
                text = text12
            else:
                text = text12 + " -f fasta"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioTFasta.isChecked():
            self.frameTFasta.setEnabled(True)
            self.frameMS.setEnabled(False)
            self.frameFasta.setEnabled(False)

            self.checkOrderSamples.setEnabled(True)
            self.checkSeed.setEnabled(True)

            self.lineMSlength.setText("")
            self.checkMSiter.setChecked(False)
            self.checkMSratio.setChecked(False)
            self.checkMSRev.setChecked(False)
            self.checkMSoutgroup.setChecked(False)
            self.checkMaskMS.setChecked(False)
            self.checkIUPACFasta.setChecked(False)
            self.checkMaskFasta.setChecked(False)
            self.checkGFF.setChecked(False)

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-l " in text0:
                old = re.findall(" -l\s[\d]+", text0)[0]
                text1 = text0.replace(old, "")
            else:
                text1 = text0
            if "-r " in text1:
                old = re.findall(" -r\s[\d]+", text1)[0]
                text2 = text1.replace(old, "")
            else:
                text2 = text1
            if "-v " in text2:
                old = re.findall(" -v\s\d+\.\d+|-v\s\d+", text2)[0]
                text3 = text2.replace(old, "")
            else:
                text3 = text2
            if "-q " in text3:
                old = re.findall(" -q\s\d+\.\d+|-q\s\d+", text3)[0]
                text4 = text3.replace(old, "")
            else:
                text4 = text3
            if "-m " in text4:
                old = re.findall(" -m\s[\w\.\/\_\-\(\)]+", text4)[0]
                text5 = text4.replace(old, "")
            else:
                text5 = text4
            if "-F " in text5:
                old = re.findall(" -F\s\d", text5)[0]
                text6 = text5.replace(old, "")
            else:
                text6 = text5
            if "-p " in text6:
                old = re.findall(" -p\s\d", text6)[0]
                text7 = text6.replace(old, "")
            else:
                text7 = text6
            if "-K " in text7:
                old = re.findall(" -K\s\d", text7)[0]
                text8 = text7.replace(old, "")
            else:
                text8 = text7
            if "-g " in text8:
                old = re.findall(" -g\s[\w\.\/\_\-\(\)]+[\s\w]+", text8)[0].rstrip()
                text9 = text8.replace(old, "")
            else:
                text9 = text8
            if "-c " in text9:
                old = re.findall(" -c\s[\w]+", text9)[0].rstrip()
                text10 = text9.replace(old, "")
            else:
                text10 = text9

            if "-f fasta" in text10:
                text = text10.replace("-f fasta", "-f tfa")
            elif "-f ms" in text10:
                text = text10.replace("-f ms", "-f tfa")
            elif "-f tfa" in text10:
                text = text10
            else:
                text = text10 + " -f tfa"

            self.commandRun.setText(textrest + "\n" + text)

        if self.radioFormat0.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 0")
            else:
                text = text0 + " -o 0"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat1.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 1")
            else:
                text = text0 + " -o 1"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat2.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 2")
            else:
                text = text0 + " -o 2"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat3.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 3")
            else:
                text = text0 + " -o 3"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat4.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 4")
            else:
                text = text0 + " -o 4"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat5.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 5")
            else:
                text = text0 + " -o 5"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat6.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 6")
            else:
                text = text0 + " -o 6"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat7.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 7")
            else:
                text = text0 + " -o 7"

            self.commandRun.setText(textrest + "\n" + text)

        elif self.radioFormat10.isChecked():
            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
            if "bin/mstatspop" not in textall:
                textall = textall + "\n./bin/mstatspop/bin/mstatspop"
            for line in textall.splitlines():
                if "bin/mstatspop" in line:
                    text0 = line
                else:
                    if textrest == "":
                        textrest = line
                    else:
                        textrest += "\n" + line

            if "-o " in text0:
                old = re.findall("-o\s[\d]+", text0)[0]
                text = text0.replace(old, "-o 10")
            else:
                text = text0 + " -o 10"

            self.commandRun.setText(textrest + "\n" + text)

        if self.checkPermWindows.isChecked():
            self.linePermWindows.setEnabled(True)
        else:
            self.linePermWindows.setEnabled(False)
            self.linePermWindows.setText("")

        if self.checkSeed.isChecked():
            self.lineSeed.setEnabled(True)
        else:
            self.lineSeed.setEnabled(False)
            self.lineSeed.setText("")

        if self.checkGFF.isChecked():
            self.lineGFF.setEnabled(True)
            self.openGFF.setEnabled(True)
            self.labelType.setEnabled(True)
            self.lineType.setEnabled(True)
            self.labelCode.setEnabled(True)
            self.radioCode1.setEnabled(True)
            self.radioCode2.setEnabled(True)
            self.radioCode3.setEnabled(True)
            self.radioCode4.setEnabled(True)
            self.lineCode4.setEnabled(True)
            self.labelCriteria.setEnabled(True)
            self.radioFirst.setEnabled(True)
            self.radioMin.setEnabled(True)
            self.radioMax.setEnabled(True)
            self.radioLong.setEnabled(True)
        else:
            self.lineGFF.setEnabled(False)
            self.lineGFF.setText("")
            self.openGFF.setEnabled(False)
            self.labelType.setEnabled(False)
            self.lineType.setEnabled(False)
            self.lineType.setText("")
            self.labelCode.setEnabled(False)
            self.radioCode1.setEnabled(False)
            self.radioCode2.setEnabled(False)
            self.radioCode3.setEnabled(False)
            self.radioCode4.setEnabled(False)
            self.lineCode4.setEnabled(False)
            self.lineCode4.setText("")
            self.labelCriteria.setEnabled(False)
            self.radioFirst.setEnabled(False)
            self.radioMin.setEnabled(False)
            self.radioMax.setEnabled(False)
            self.radioLong.setEnabled(False)

        if self.checkAltSpect.isChecked():
            self.lineAltSpect.setEnabled(True)
            self.openAltSpect.setEnabled(True)
            self.checkNullSpect.setEnabled(True)
        else:
            self.lineAltSpect.setEnabled(False)
            self.lineAltSpect.setText("")
            self.openAltSpect.setEnabled(False)
            self.checkNullSpect.setEnabled(False)
            self.checkNullSpect.setChecked(False)
            self.lineNullSpect.setText("")

        if self.checkNullSpect.isChecked():
            self.lineNullSpect.setEnabled(True)
            self.openNullSpect.setEnabled(True)
        else:
            self.lineNullSpect.setEnabled(False)
            self.lineNullSpect.setText("")
            self.openNullSpect.setEnabled(False)

        if self.checkOrderSamples.isChecked():
            self.labelOrderSamples1.setEnabled(True)
            self.lineOrderSamples1.setEnabled(True)
            self.labelOrderSamples2.setEnabled(True)
            self.lineOrderSamples2.setEnabled(True)
        else:
            self.labelOrderSamples1.setEnabled(False)
            self.lineOrderSamples1.setEnabled(False)
            self.lineOrderSamples1.setText("")
            self.labelOrderSamples2.setEnabled(False)
            self.lineOrderSamples2.setEnabled(False)
            self.lineOrderSamples2.setText("")

        if self.radioWindowSize.isChecked():
            self.checkSlide.setEnabled(True)
            self.lineWindowSize.setEnabled(True)
        else:
            self.lineWindowSize.setEnabled(False)

        if self.radioCoordTF.isChecked():
            self.lineCoordTF.setEnabled(True)
            self.openCoordTF.setEnabled(True)
        else:
            self.lineCoordTF.setEnabled(False)
            self.openCoordTF.setEnabled(False)

        if self.checkSlide.isChecked():
            self.lineSlide.setEnabled(True)
        else:
            self.lineSlide.setEnabled(False)

        if self.checkFirstWindowTF.isChecked():
            self.lineFirstWindowTF.setEnabled(True)
        else:
            self.lineFirstWindowTF.setEnabled(False)

        if self.radioCode4.isChecked():
            self.lineCode4.setEnabled(True)
        else:
            self.lineCode4.setEnabled(False)

        if self.checkMaskMS.isChecked():
            self.lineMaskMS.setEnabled(True)
            self.openMaskMS.setEnabled(True)
        else:
            self.lineMaskMS.setEnabled(False)
            self.lineMaskMS.setText("")
            self.openMaskMS.setEnabled(False)

        if self.checkMSoutgroup.isChecked():
            self.checkMSRev.setEnabled(True)
        else:
            self.checkMSRev.setEnabled(False)
            self.lineMSRev.setEnabled(False)
            self.lineMSRev.setText("")

        if self.checkMSRev.isChecked():
            self.lineMSRev.setEnabled(True)
        else:
            self.lineMSRev.setEnabled(False)
            self.lineMSRev.setText("")

        if self.checkMSratio.isChecked():
            self.lineMSratio.setEnabled(True)
        else:
            self.lineMSratio.setEnabled(False)
            self.lineMSratio.setText("")

        if self.checkMSiter.isChecked():
            self.lineMSiter.setEnabled(True)
        else:
            self.lineMSiter.setEnabled(False)
            self.lineMSiter.setText("")

        if self.checkUnknownPos.isChecked():
            if self.radioTFasta.isChecked():
                self.checkPermWindows.setEnabled(True)
            elif self.radioFasta.isChecked():
                self.checkPermWindows.setEnabled(True)
        else:
            self.checkPermWindows.setEnabled(False)
            self.linePermWindows.setEnabled(False)
            self.linePermWindows.setText("")

    def FinishRun(self):
        self.workerThread.terminate()
        self.progress.close()

    def on_click_RunAll(self):

        ##########################
        ## Running all programs ##
        ##########################

        msgRun = QtWidgets.QMessageBox()
        msgRun.setIcon(QtWidgets.QMessageBox.Warning)
        msgRun.setText("The execution of the programs could take a long time depending on the files sizes and the selected analysis.\n\nAre you sure to perform the analysis?")
        msgRun.setWindowTitle("Are you sure?")
        msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msgRun.exec_()
        if retval == QtWidgets.QMessageBox.Ok:

            textall = self.commandRun.toPlainText()
            text0 = ""
            textrest = ""
    
            for line in textall.splitlines():
                if "bin/gVCF2tFasta" in line:
                    self.Run_vcf = QtCore.QProcess(self)
                    self.Run_vcf.start(line)
                    self.Run_vcf.readyReadStandardOutput.connect(self.procStdOut_vcf)
    
                elif "bin/fastaconvtr" in line:
                    self.Run_fastaconvtr = QtCore.QProcess(self)
                    self.Run_fastaconvtr.start(line)
                    self.Run_fastaconvtr.readyReadStandardOutput.connect(self.procStdOut_fastaconvtr)
    
                elif "bin/weight4tfa" in line:
                    self.Run_weight = QtCore.QProcess(self)
                    self.Run_weight.start(line)
                    self.Run_weight.readyReadStandardOutput.connect(self.procStdOut_weight)

                elif "bin/indexingtFasta" in line:
                    self.Run_indexing = QtCore.QProcess(self)
                    self.Run_indexing.start(line)
                    self.Run_indexing.readyReadStandardOutput.connect(self.procStdOut_indexing)
    
                elif "bin/concatenate_tFasta" in line:
                    self.Run_concatenate = QtCore.QProcess(self)
                    self.Run_concatenate.start(line)
                    self.Run_concatenate.readyReadStandardOutput.connect(self.procStdOut_concatenate)
    
                elif "bin/mergetFasta" in line:
                    self.Run_merge = QtCore.QProcess(self)
                    self.Run_merge.start(line)
                    self.Run_merge.readyReadStandardOutput.connect(self.procStdOut_merge)
    
                elif "bin/mstatspop" in line:
                    self.Run_mstatspop = QtCore.QProcess(self)
                    self.Run_mstatspop.start(line)
                    self.Run_mstatspop.finished.connect(self.procStdOut_mstatspop)

    def procStdOut_vcf(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/gVCF2tFasta" in line:
                text0 = line

        if "-v " in text0 and "-r " in text0 and "-o " in text0 and "-n " in text0:
            self.Run_vcf.waitForFinished()
            self.Run_vcf.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Conversion from gVCF to tFasta finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and "-r " in text0 and "-o " in text0 and "-n " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and "-r " in text0 and not "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and "-r " in text0 and not "-o " in text0 and "-n " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and not "-r " in text0 and "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Reference Fasta file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and not "-r " in text0 and not "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n-No Reference Fasta file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and not "-r " in text0 and not "-o " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n-No Reference Fasta file selected\n-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-v " in text0 and not "-r " in text0 and "-o " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Reference Fasta file selected\n-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and "-r " in text0 and "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and not "-r " in text0 and "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Reference Fasta file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and not "-r " in text0 and not "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n-No Reference Fasta file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and "-r " in text0 and "-o " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and "-r " in text0 and not "-o " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-v " in text0 and not "-r " in text0 and not "-o " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n-No Reference Fasta file selected\n-No File with scaffold(s) selected\n\nConversion from gVCF to tFasta cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_fastaconvtr(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/fastaconvtr" in line:
                text0 = line

        if "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " in text0:
            self.Run_fastaconvtr.waitForFinished()
            self.Run_fastaconvtr.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Conversion between file formats finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " not in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " not in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " not in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " not in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and not "-o " in text0 and not "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and not "-o " in text0 and not "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and "-o " in text0 and not "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-f " in text0 and "-o " in text0 and not "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and "-o " in text0 and not "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and "-o " in text0 and not "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-f " in text0 and not "-o " in text0 and "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and not "-o " in text0 and not "-n " in text0 and "-F " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-f " in text0 and not "-o " in text0 and not "-n " in text0 and "-F " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nConversion between file formats cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_weight(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/weight4tfa" in line:
                text0 = line

        if "-i " in text0 and "-g " in text0 and "-c " in text0 and "-n " in text0:
            self.Run_weight.waitForFinished()
            self.Run_weight.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Calculation of weights finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-g " in text0 and "-c " in text0 and "-n " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-g " in text0 and not "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-g " in text0 and not "-c " in text0 and "-n " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-g " in text0 and "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No GFF file selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-g " in text0 and not "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No GFF file selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-g " in text0 and not "-c " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No GFF file selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-g " in text0 and "-c " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No GFF file selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-g " in text0 and "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-g " in text0 and "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No GFF file selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-g " in text0 and not "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No GFF file selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-g " in text0 and "-c " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-g " in text0 and not "-c " in text0 and "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-g " in text0 and not "-c " in text0 and not "-n " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n-No GFF file selected\n-Criteria to consider transcripts not selected\n\nCalculation of weights cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_concatenate(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/concatenate" in line:
                text0 = line

        if "-i " in text0 and "-o " in text0:
            self.Run_concatenate.waitForFinished()
            self.Run_concatenate.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Joining of tFasta files finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n\nJoining of files (concatenation) cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-o " in text0 and "-i " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nJoining of files (concatenation) cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        else:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n\nJoining of files (concatenation) cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_merge(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/mergetFasta" in line:
                text0 = line

        if "-i " in text0 and "-o " in text0:
            self.Run_merge.waitForFinished()
            self.Run_merge.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Joining of tFasta files finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n\nJoining of files cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-o " in text0 and "-i " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nJoining of files cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        else:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n\nJoining of files cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_indexing(self):
        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/indexingtFasta" in line:
                text0 = line

        if "-i " in text0:
            self.Run_indexing.waitForFinished()
            self.Run_indexing.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Indexing of tFasta file finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        else:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nFile indexing cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

    def procStdOut_mstatspop(self):
        self.Run_mstatspop.waitForFinished()
        self.Run_mstatspop.close()

        textall = self.commandRun.toPlainText()
        text0 = ""
        textrest = ""
        for line in textall.splitlines():
            if "bin/mstatspop" in line:
                text0 = line

        if "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            self.Run_mstatspop.waitForFinished()
            self.Run_mstatspop.close()

            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Information)
            msgRun.setText("Analysis of variability finished")
            msgRun.setWindowTitle("Finished")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " not in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " not in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " not in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " not in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " not in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " not in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " not in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " not in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No File with scaffold(s) selected\n-No Output format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif "-i " in text0 and not "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and "-o " in text0 and not "-T " in text0 and "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()
        elif not "-i " in text0 and not "-o " in text0 and not "-T " in text0 and not "-n " in text0 and "-f " not in text0 and "-N " not in text0:
            msgRun = QtWidgets.QMessageBox()
            msgRun.setIcon(QtWidgets.QMessageBox.Warning)
            msgRun.setText("-No Input file selected\n-No Input format file selected\n-No File with scaffold(s) selected\n-No Output format file selected\n-No Output file selected\n-Number of populations and samples not specified\n\nAnalysis of variability cannot be performed.")
            msgRun.setWindowTitle("Error")
            msgRun.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msgRun.exec_()

        #################################
        ## Generating the output table ##
        #################################

        if "-o 1" in text0:

            if "-T" in text0:

                self.tableWidget.setEnabled(True)
                self.DownloadTable.setEnabled(True)

                for i,w in enumerate(text0.split()):
                    if w == "-T":
                        outmstatspop = text0.split()[i+1]

                header = []
                lines = 0
                for line in open(outmstatspop):
                    if lines == 0:
                        for i,w in enumerate(line.split()):
                            if (i % 2) == 0:
                                header.append(w.rstrip(':'))
                    lines += 1
                
                columns = len(header)

                self.tableWidget.setRowCount(lines)
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setHorizontalHeaderLabels(header)
                self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

                lines = 0
                for line in open(outmstatspop):
                    for i,w in enumerate(line.split()):
                        if (i % 2) != 0:
                            j = int((i-1)/2)
                            self.tableWidget.setItem(lines, j, QtWidgets.QTableWidgetItem(w))
                    lines += 1

                QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget,2)
        else:
            self.tableWidget.setEnabled(False)

    def on_click_DownloadTable(self):

        filename, extension = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', '.csv')
        if filename != '':
            with open(filename + extension,'w') as stream:
                writer = csv.writer(stream, delimiter = '\t')
                header = []
                for column in range(self.tableWidget.columnCount()):
                    col = self.tableWidget.horizontalHeaderItem(column)
                    item = self.tableWidget.item(0, column)
                    if item.isSelected():
                        header.append(col.text())
                writer.writerow(header)
                for row in range(self.tableWidget.rowCount()):
                    rowdata = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item.isSelected():
                            if item is not None:
                                rowdata.append(item.text())
                            else:
                                rowdata.append('')
                    writer.writerow(rowdata)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
