I can make a targeted improvement from the supplied source, but the reference image is not attached, so I can’t accurately reproduce its visual details. With launch today, I’d keep the shared theme and go_router setup intact; replacing either would affect six screens or broaden the release risk without evidence that it’s needed.

Update `AccountsView` only:

- Give each account row clearer hierarchy: account name as the primary label and balance as a visually distinct, right-aligned value.
- Add consistent horizontal and vertical padding, a subtle divider or restrained card treatment, and a clear pressed state. Use existing theme colors and text styles so the list remains consistent with the rest of the app.
- Preserve the existing `open(account)` tap behavior.
- Keep loading and error UI in the parent, which already owns those states. Avoid adding duplicate state handling here.
- If the list can be long, retain `ListView.builder` for lazy construction.

I’d first check the app’s existing design tokens and account model fields, then make the row-level changes and review the screen at its supported sizes. I can match the reference more closely if you attach it; without it, I’d avoid guessing at its colors, typography, or navigation.