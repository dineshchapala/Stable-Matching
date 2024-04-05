Team Members:
1.Deekshith Reddy Chandupatla(chandupatla.7@wright.edu)
2.Sandeep Kumar Karnati(Karnati.18@wright.edu)
3.Manasa Kothapeta(kothapeta.2@wright.edu)

System Requirement :
1. System should have 3+ python version.

Steps to run the solution
1. First Extract the zip.
2. Open command prompt and move to the working directory.
3. run the command "python scriptFileName.py inputfileName.txt"
4. e.g for sampleInput1 , out command will be python assignment1.py stableInput1.txt
5. A file will be generated in the working directory name stableOutput.txt having two space separated number
   indicating first number as 0 or 1 (stable or unstable), second number as how many matching pair to be corrected for
   stable solution.

Algorithm for testing if given matching pair is stable or not.

for Perfect matching, each men and women should have atleast and atmost one match.
-> Each woman should gets exactly one man.
-> Each man should gets exactly one woman.
-> In matching set, an unmatched pair m1-w1 is unstable if man m1 and
   woman w1 prefer each other to current partners.
-> Unstable pair m1-w1 could each improve by interchanging their partner with other pair.
Stable matching means perfect matching with no unstable pairs.

We have given all matching pair.
1. Loop for each pair
2. two pair{(A1,B1),(A2,B2)} is said to be unstable, if below four conditions are satified.
3. If B2 comes before B1 in the preference list of A1
4. If A2 comes before A1 in the preference list of B1
5. If A1 comes before A2 in the preference list of B2
6. If B1 comes before B2 in the preference list of A2

If No unstable pair present in the Matching then Matching will be stable.





