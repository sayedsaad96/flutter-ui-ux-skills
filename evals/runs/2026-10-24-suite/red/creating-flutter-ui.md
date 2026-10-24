## UI foundation

Use a calm, high-contrast layout with warm neutral backgrounds, navy text, and teal for primary actions. Keep one clear task per screen, generous spacing, large tap targets, and plain-language labels. On phones, use a single column; on tablets, keep the booking flow centered in a readable-width panel rather than stretching controls across the screen.

### Language and direction

Offer Arabic and English throughout the feature. Mirror the layout and navigation for Arabic right-to-left reading, including back/next placement, date and slot ordering, and alignment. Keep dates, times, and practitioner names legible in either language, and ensure the selected language is consistent across every step.

### Booking flow

1. **Choose a practitioner.** Show a simple list of practitioners with names and any available identifying details. Selecting a practitioner advances to date selection.
2. **Choose a date.** Present available dates in a clear, scrollable calendar or date list. Make the selected date visually distinct and show when no dates are available.
3. **Choose a time.** List available slots for the selected date as large, clearly labeled buttons. Mark the selected slot distinctly. Keep unavailable slots out of the selectable list; if a slot becomes unavailable, explain that it is no longer available and ask the patient to choose another.
4. **Review and confirm.** Summarize the practitioner, date, and time before the final action. Use a clear primary “Confirm booking” action, with a way to go back and change a selection.
5. **Confirmation.** After a successful booking, show a clear confirmation state with the same booking details and a concise next step.

### Interaction and resilience

Disable confirmation until all required choices are present. Recheck the selected slot when the patient confirms: if it has been taken, preserve the other selections, explain what happened in plain language, and return them to slot selection. Prevent repeated taps from submitting the same confirmation more than once.

For poor connectivity, show when the app is checking availability or submitting, keep the current choices visible, and provide a retry action if the request fails. Do not show a success confirmation until the booking has actually succeeded. If the app cannot verify availability, say so and let the patient retry rather than implying the slot is reserved.

Use text and shape as well as color to show selected, unavailable, loading, and error states. Keep labels and feedback concise, use readable type and strong contrast, and make the main action easy to find on every step.