# Windows Authentication Log Investigator

## Investigation 001 — Workstation Unlock

**Objective:** Investigate a Windows successful-logon event.

**Evidence collected**
- Event ID: 4624
- Logon Type: 7 (Unlock)
- Account assessment: Own Windows account
- Timing assessment: Consistent with normal laptop usage
- Related Event ID 4801: Not found during this check

**Analysis**

Event ID 4624 with Logon Type 7 indicates a successful logon associated with unlocking an existing session. The account and timing appear consistent with expected workstation use.

Event ID 4801 was not found during this check. Its absence does not establish malicious activity or prove that the workstation was never unlocked.

**Preliminary conclusion:** Activity appears consistent with normal workstation use based on the limited evidence reviewed.

**Limitations:** The surrounding events, auditing configuration and additional account or session details have not yet been examined.

**Next steps:** Review related security events and timestamps to strengthen or revise the assessment.





## Investigation 002 — Repeated Failed Logons

**Event ID:** 4625  
**Logon Type:** 2 — Interactive  
**Failure status:** 0xC000006D  
**Failure substatus:** 0xC0000380  
**Source address:** Loopback  
**Account pattern:** Same account across multiple failures  
**Timing pattern:** Several failures close together  
**Caller process:** Same executable filename across the reviewed events  
**Authentication package:** Negotiate  
**Logon process:** User32

### Preliminary assessment

Multiple failed interactive logons were observed against the same account, with a loopback source address and a consistent caller-process filename.

The status and substatus codes require careful interpretation. The evidence collected so far does not establish whether the activity is benign or malicious.

### Next steps

Correlate the events by timestamp, examine the process identity and context, and review any relevant surrounding Windows security events before reaching a final conclusion.




Evidence Validation

Validation method: Reviewed the XML View of the Windows Event ID 4625 record.

Result: The Status and SubStatus values matched the values recorded in the investigation report.

Remaining uncertainty: The authentication failure's precise cause has not been independently established. Microsoft documents SubStatus 0xC0000380 as STATUS_SMARTCARD_WRONG_PIN. This code is recorded as observed evidence; the available event details do not independently establish the underlying cause or prove that a physical smart card was used.

Next action: Preserve the relevant event fields and correlate the failed logons with surrounding activity before making a final determination.


Event Correlation — Failed Logons and Successful Unlock

Observed sequence

Multiple Event ID 4625 interactive logon failures occurred close together.

The failures involved the same account and the same loopback source address.

The caller-process filename was consistent across the reviewed failures.

A later Event ID 4624 with Logon Type 7 was recorded for the same account shortly afterward.

The successful unlock appeared consistent with normal workstation use.

Assessment

The successful unlock provides context for the timeline but does not establish that the preceding failures were resolved by that event. The failures and unlock may be separate activities within the same workstation session.

Conclusion: The activity remains inconclusive. Further attribution would require additional corroborating evidence, including surrounding events and process context.

Evidence limitation: No definitive evidence of account compromise has been established by the events reviewed so far.
