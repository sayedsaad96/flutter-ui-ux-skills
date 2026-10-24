Keep the invoice data unchanged. Implement the row so it follows the app’s text direction and remains usable with larger text, assistive technology, and keyboard input.

1. Replace `EdgeInsets.only(left: 16)` with direction-aware padding such as `EdgeInsetsDirectional.only(start: 16)`. Align the row’s contents to the start in the active direction; do not force LTR. Use the existing invoice ID and amount values without reordering or rewriting business data.

2. Remove the fixed 40-pixel row height. Let the row grow with its text, and allow a narrow layout to wrap or otherwise expand instead of clipping. Keep the designer’s spacing and alignment as the normal-size baseline, then check both Arabic/RTL and English/LTR layouts with large text enabled.

3. Replace the icon-only `GestureDetector` with a semantic button (for example, an appropriately styled `IconButton`) with a localized delete label and adequate touch target. Ensure it participates in web keyboard navigation and activation, and that its focus state is visible.

4. Render the customer name and Latin invoice ID as separate text spans or widgets, with deliberate bidirectional handling so mixed Arabic and Latin content reads in the intended order. Preserve the displayed values exactly; do not alter customer names, IDs, or amounts.

5. Measure the row’s foreground/background contrast and adjust its colors if needed. No contrast measurements were supplied, so compliance cannot be assumed from the available evidence.

Before delivery today, inspect the row in both directions and at enlarged text sizes, then verify keyboard focus and activation and screen-reader announcement of the delete action. No runtime, screenshot, or screen-reader evidence was supplied, so those checks remain to be performed.