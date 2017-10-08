"""
Name:        eLCS_OutputFileManager.py
Authors:     Ryan Urbanowicz - Written at Dartmouth College, Hanover, NH, USA
Contact:     ryan.j.urbanowicz@darmouth.edu
Created:     November 1, 2013
Description: This module contains the methods for generating the different output files generated by eLCS.  
             These files are generated at each learning checkpoint, and the last iteration.  These include...
             writePopStats:   Summary of the population statistics
             writePop:        Outputs a snapshot of the entire rule population including classifier conditions, classes, and parameters.
             
---------------------------------------------------------------------------------------------------------------------------------------------------------
eLCS: Educational Learning Classifier System - A basic LCS coded for educational purposes.  This LCS algorithm uses supervised learning, and thus is most 
similar to "UCS", an LCS algorithm published by Ester Bernado-Mansilla and Josep Garrell-Guiu (2003) which in turn is based heavily on "XCS", an LCS 
algorithm published by Stewart Wilson (1995).  

Copyright (C) 2013 Ryan Urbanowicz 
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the 
Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABLILITY 
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, 
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
---------------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Import Required Modules--------------
from Demo_4.eLCS_Constants import cons


# -------------------------------------

class OutputFileManager:
    def writePopStats(self, outFile, exploreIter, pop, correct):
        """ Makes output text file which includes all of the evaluation statistics for a complete analysis of all training and testing data on the current eLCS rule population. """
        try:
            popStatsOut = open(outFile + '_' + str(exploreIter) + '_PopStats.txt', 'w')
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            print('cannot open', outFile + '_' + str(exploreIter) + '_PopStats.txt')
            raise
        else:
            print("Writing Population Statistical Summary File...")

        # Evaluation of pop
        popStatsOut.write(
            "Population Characterization:------------------------------------------------------------------------\n")
        popStatsOut.write("MacroPopSize\tMicroPopSize\tGenerality\n")
        popStatsOut.write(str(len(pop.popSet)) + "\t" + str(pop.microPopSize) + "\t" + str(pop.aveGenerality) + "\n\n")

        popStatsOut.write("SpecificitySum:------------------------------------------------------------------------\n")
        headList = cons.env.formatData.trainHeaderList  # preserve order of original dataset

        for i in range(len(headList)):
            if i < len(headList) - 1:
                popStatsOut.write(str(headList[i]) + "\t")
            else:
                popStatsOut.write(str(headList[i]) + "\n")

        # Prints out the Specification Sum for each attribute 
        for i in range(len(pop.attributeSpecList)):
            if i < len(pop.attributeSpecList) - 1:
                popStatsOut.write(str(pop.attributeSpecList[i]) + "\t")
            else:
                popStatsOut.write(str(pop.attributeSpecList[i]) + "\n")

        popStatsOut.write("\nAccuracySum:------------------------------------------------------------------------\n")
        for i in range(len(headList)):
            if i < len(headList) - 1:
                popStatsOut.write(str(headList[i]) + "\t")
            else:
                popStatsOut.write(str(headList[i]) + "\n")

        # Prints out the Accuracy Weighted Specification Count for each attribute 
        for i in range(len(pop.attributeAccList)):
            if i < len(pop.attributeAccList) - 1:
                popStatsOut.write(str(pop.attributeAccList[i]) + "\t")
            else:
                popStatsOut.write(str(pop.attributeAccList[i]) + "\n")

                # Correct Track ---------------------------------------------------------------------------------------------------------
        popStatsOut.write(
            "\nCorrectTrackerSave:------------------------------------------------------------------------\n")
        for i in range(len(correct)):
            popStatsOut.write(str(correct[i]) + "\t")

        popStatsOut.close()

    def writePop(self, outFile, exploreIter, pop):
        """ Writes a tab delimited text file outputting the entire evolved rule population, including conditions, phenotypes, and all rule parameters. """
        try:
            rulePopOut = open(outFile + '_' + str(exploreIter) + '_RulePop.txt', 'w')
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            print('cannot open', outFile + '_' + str(exploreIter) + '_RulePop.txt')
            raise
        else:
            print("Writing Population as Data File...")

        # Write Header-----------------------------------------------------------------------------------------------------------------------------------------------
        dataLink = cons.env.formatData
        headList = dataLink.trainHeaderList
        for i in range(len(headList)):
            rulePopOut.write(str(headList[i]) + "\t")
        rulePopOut.write(
            "Phenotype\tFitness\tAccuracy\tNumerosity\tAveMatchSetSize\tTimeStampGA\tInitTimeStamp\tSpecificity\tDeletionProb\tCorrectCount\tMatchCount\n")

        # Write each classifier--------------------------------------------------------------------------------------------------------------------------------------
        for cl in pop.popSet:
            rulePopOut.write(str(cl.printClassifier()))

        rulePopOut.close()
