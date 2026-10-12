# Windows Authentication Log Investigator

**Investigation Report | Windows Security Logs | SOC Practice**

| Report detail | Value |
|---|---|
| Investigation type | Windows authentication event analysis |
| Environment | Personal Windows workstation |
| Tools | Windows Event Viewer, XML Event View |
| Assessment | Inconclusive |
| Purpose | Defensive cybersecurity learning |

---

## Investigation 001 — Workstation Unlock

### Objective
Examine a successful Windows logon event and determine what the available event details indicate.

### Evidence collected
- Event ID: 4624
- Logon Type: 7 — workstation unlock
- Account context: own Windows account
- Timing: consistent with normal laptop usage
- Related Event ID 4801: not found during this check

### Analysis
Event ID 4624 records a successful logon. Logon Type 7 is associated with unlocking an existing workstation session.

Event ID 4801 was not found during this check. Its absence does not establish malicious activity or prove that the workstation was compromised.

### Preliminary conclusion
The event appeared consistent with normal workstation use based on the limited evidence reviewed.

### Limitations
The surrounding events, auditing configuration, and additional account or session details were not fully examined.

---

## Investigation 002 — Repeated Failed Logons

### Objective
Examine repeated failed interactive logon events and identify patterns that may require further investigation.

### Evidence collected
- Event ID: 4625 — failed logon
- Logon Type: 2 — interactive logon
- Account: same account across the reviewed failures
- Source address: loopback category
- Timing: several failures occurred close together during normal laptop usage
- Caller process: same executable filename across the reviewed events
- Logon Process: User32
- Authentication Package: Negotiate
- Status: 0xC000006D
- SubStatus: 0xC0000380

### Analysis
The reviewed events contained multiple failed interactive logons associated with the same account and loopback source-address category. The events occurred close together and showed consistent caller-process information.

Status 0xC000006D indicates a general logon failure. Microsoft documents SubStatus 0xC0000380 as STATUS_SMARTCARD_WRONG_PIN. This code is recorded as observed evidence; the available event details do not independently establish the underlying cause or prove that a physical smart card was used.

The loopback source address and caller-process information provide context, but neither independently proves that the activity was benign or malicious.

### Preliminary conclusion
The repeated failures form a pattern worth documenting, but the available evidence is insufficient to attribute the activity confidently.

---

## Evidence Validation

The Status and SubStatus values were cross-checked using the event's XML View in Windows Event Viewer.

- Status matched the value recorded in the report.
- SubStatus matched the value recorded in the report.
- The interpretation remains limited to the documented code and available event context.

---

## Event Correlation — Failed Logons and Successful Unlock

### Observations
- A cluster of failed interactive logons was observed.
- A subsequent successful workstation unlock event was found for the same account.
- The successful event occurred shortly after the failed-event cluster.
- The workstation context appeared consistent with the user's normal laptop session.

### Assessment
The sequence establishes a temporal relationship between the reviewed events, but it does not establish that the failed attempts caused the successful unlock or that an unauthorized user gained access.

**Overall assessment: Inconclusive.**

Further investigation would require additional contextual evidence, such as surrounding security events, session details, and relevant system activity.

---

## Investigation Workflow

1. Open Windows Event Viewer.
2. Filter Security logs for Event IDs 4624 and 4625.
3. Review logon types and relevant event fields.
4. Compare account, source-address category, timestamps, and process information.
5. Inspect XML View to validate important fields.
6. Correlate the failed-event cluster with subsequent successful activity.
7. Document observations, uncertainties, and limitations.

## Recommendations for Further Investigation

- Review additional events surrounding the same time window.
- Confirm event-code interpretations against official Microsoft documentation.
- Examine relevant process and session context before attributing activity.
- Build a structured timeline using sanitized evidence.
- Develop repeatable analysis and detection tests.

## Disclaimer

This report documents a defensive cybersecurity learning exercise using events from a personal Windows environment. The findings are limited to the evidence examined and do not establish that a security compromise occurred. Sensitive information and raw personal logs should not be published.
