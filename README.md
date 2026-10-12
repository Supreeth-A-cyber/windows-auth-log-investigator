Windows Authentication Log Investigator

Project Overview

A beginner cybersecurity project focused on examining Windows Security events, interpreting authentication failures, correlating event timelines, and documenting evidence using a SOC-style investigation workflow.

Objectives

Understand Windows Security Event IDs 4624 and 4625.

Interpret logon types and authentication failure fields.

Compare repeated failed logons with subsequent successful events.

Document findings, uncertainties, and investigation limitations.

Tools Used

Windows Event Viewer

Windows Security event logs

Notepad

Git and GitHub (planned for project version control and publication)

Work Completed

Examined a successful logon event (4624) with Logon Type 7.

Examined failed logon events (4625) with Logon Type 2.

Compared account patterns, source-address categories, and caller-process filenames.

Reviewed Status and SubStatus in XML View.

Correlated failed logons with a later successful unlock event.

Created a written investigation report.

Project Structure

reports/ — written investigation reports

evidence/ — sanitized supporting evidence, if needed

screenshots/ — sanitized screenshots, if needed

Findings and Limitations

The reviewed events showed multiple failed interactive logons and a subsequent successful workstation unlock for the same account.

The observed sequence does not independently establish whether the failures were malicious or benign. Additional context would be needed for a stronger attribution.

Future Improvements

Validate event fields against official Microsoft documentation.

Add sanitized example data and reproducible analysis steps.

Develop a Python log-analysis script with test cases.

Add detection logic and document false positives.

Improve the investigation report with a structured event timeline.

Disclaimer

This project is for defensive cybersecurity learning using logs from my own Windows environment. Personal information and raw sensitive logs should not be published.