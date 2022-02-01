There are Three Different Codes.
#Implicit Modules not Used

There is an excel(birth1.xlsx) file having Birthdates and E-MailId's of Diffeerent people.

1. In mailSend.py, The script is scheduled to run at "00:00" every day and it sends Happy Birthday message on the person's E-MailId who evers birthday is on that day.

2. In Second Code mailSendD.py, The script is scheduled to run at "00:00" every day and it sends Happy Birthday and Total Years, Months, Weeks and Days They have lived till Date      as message on the person's E-MailId who evers birthday is on that day.

3. In Third Code mailSendDA.py, The script is scheduled to run at "00:00" every day and it sends Happy Birthday and PARTICULAR PERSOSN'S NAME as message and Total Years, Months,      Weeks and Days They have lived till Date WRITTEN IN A TEXT FILE ATTACHED in the mail on the person's E-MailId who evers birthday is on that day.

   Already created dmycalculateCModule.py MODULE from MiniProjects Repository is Used for Calculations.

4. In DuplicateSend.py, The Script is scheduled to run every Hour and It checks Duplicate Files in Given folder if Duplications found it creates a Directory, Inside Directory it      creates a log.txt which maintains all names of duplicate files which are deleted(log.txt is only created if Dupliations are Found). Name of that log file contains the date and    time at which that file gets created. The log file is then sent to the Email-ID. 
        
        Mail body Contains Following Statistics about File Duplication :-
              
              Starting time of scanning
              Total number of files scanned
              Total number of duplicate files found
              Log file attached       
