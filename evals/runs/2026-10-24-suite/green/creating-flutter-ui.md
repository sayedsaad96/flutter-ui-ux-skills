# Clinic appointment booking UI foundation

**Status: proposal.** No app source, runtime, patient records, or screenshots were supplied, so this defines the experience and interaction contract rather than an implemented or validated UI.

## Audience and success

Patients booking a local clinic visit on a phone or tablet, including older adults and people with limited or unreliable connectivity. Success means the patient selects a practitioner, date, and available time, explicitly confirms, and receives an authoritative booking confirmation. The interface should make the current step and next action easy to recognize.

Assumptions: the clinic supplies practitioner availability and is the authority for whether a slot is booked. Booking requires connectivity; the interface may retain the patient's selections while offline, but must not claim a reservation until the service confirms it. Arabic and English are supported, with the device or an in-screen language control determining the initial language.

## Visual direction

Use the existing brand cues in a quiet, high-contrast layout: navy for primary text, warm neutral page and card surfaces, and teal for the main action. Keep decoration restrained. Use clear headings, generous spacing, readable type, and large full-width controls on phones. Avoid communicating availability, errors, or selection by color alone; pair color with text and icons.

Use a consistent step heading and progress label, such as “Choose a practitioner · Step 1 of 3.” Keep the primary action in a predictable bottom area, above system insets, and make it clear when it is disabled and why. On tablets, use a centered, width-limited content column; where space permits, show the selection summary beside the active step rather than stretching controls across the screen.

## Primary journey

1. **Practitioner:** Show searchable practitioner cards with name, specialty, and any clinic-provided visit details. Selecting a card visibly marks it and enables Continue. Preserve the selection when navigating back.
2. **Date and time:** Show a compact date picker and clearly labeled available time buttons. The selected date and slot remain visible together. Continue is enabled only when both are selected.
3. **Review and confirm:** Summarize practitioner, date, time, and clinic-provided visit details. Provide an explicit “Confirm booking” action and an edit action for each selection. Review is not confirmation.
4. **Result:** Show a success heading and booking details only after an authoritative successful response. Offer a clear way back to the clinic or booking start. Do not create a second booking when the user revisits the result.

Provide Back at each selection step. Preserve choices when moving backward and forward. If a choice is no longer valid, explain which one changed and return the patient to the relevant step without discarding still-valid choices.

## State and interruption behavior

- **Loading:** Keep the current step and selections visible where possible, show a brief progress label, and prevent duplicate submission while a request is in flight.
- **No practitioners or no slots:** Explain that nothing is available for the current search or date, offer a way to change the date or search, and provide clinic contact guidance if supplied. Do not show unavailable times as selectable.
- **Slot conflict:** If the selected slot becomes unavailable before confirmation, keep the practitioner and date, explain that the time was taken, refresh availability, and ask the patient to choose another slot. Do not silently replace the selection or imply the booking succeeded.
- **Offline before confirmation:** Keep the chosen practitioner, date, and slot, identify the connection problem, and offer Retry. Do not present the slot as held.
- **Submission timeout or lost connection:** Explain that the booking result is unknown and that the app is checking its status. Check the existing request/result before offering another submission. Do not show success or invite a repeat confirmation until the service establishes whether the first request succeeded.
- **Confirmed failure:** State that the booking was not completed, preserve valid choices, and offer a safe retry or a way to change the slot.
- **Confirmed success:** Show the confirmed appointment details and any confirmation reference or follow-up instructions provided by the clinic. Never infer success from a review screen or a timeout.

## Language, adaptation, and inclusion

Localize all labels, dates, errors, and status messages, not only the main buttons. Arabic uses right-to-left layout and reading order; mirror directional navigation affordances while keeping familiar date/time conventions and any clinic-provided names legible. Switching language should preserve the current step and selections.

Use semantic labels for practitioner, date, time, selected state, progress, and errors. Ensure the selected state and disabled reason are available to assistive technology. Keep keyboard and switch focus visible and move focus to a newly announced error or result without unexpectedly resetting the screen. Support system text scaling by allowing content to wrap and the page to scroll rather than clipping or shrinking text. Controls should have generous touch targets and adequate contrast.

## Next handoff

Once the app repository and clinic availability/booking contract are available, map these decisions onto its navigation, theme, localization, and state conventions. Then implement the practitioner-to-confirmation path with conflict, offline, and unknown-outcome handling. Validate the layouts and behavior on phone and tablet sizes, with Arabic RTL and large text, and check semantic actions with assistive technology.

**NOT VERIFIED:** implementation, runtime behavior, phone and tablet devices, accessibility, large-text behavior, and Arabic RTL behavior.

