## Diagnosis

The accessible excerpt shows a loaded account list with each account’s name, balance, and tap-to-open callback. There is no evidence here of a layout defect or of how the reference looks; the reference image, runtime, screenshot, and wider repository are unavailable. The shared theme serves six screens, and the parent owns loading and error states.

## Targeted implementation proposal

Keep the existing `ListView.builder`, account data, `open(account)` callback, go_router navigation, Cubit ownership, and parent loading/error handling. Do not replace the shared theme or navigation for a list-level visual update.

Refine each row using the current theme:

- Group the account name and balance into a clear, aligned row, with the name as the primary label and the balance styled as secondary information.
- Add consistent vertical spacing and directional horizontal padding; use a subtle divider or existing list surface treatment to distinguish rows.
- Preserve the full row as the tap target and make the existing open action visually legible with the app’s current affordance conventions.
- Keep the list lazy and handle long account names and balances with sensible wrapping or ellipsis, without hiding the balance’s meaning.

Before implementation, inspect the actual row’s surrounding screen and available theme components; the excerpt alone does not establish which colors, typography, spacing tokens, or affordances already exist. Avoid introducing new shared tokens unless their effects across all six screens are reviewed.

## Verification

No code change or runtime check was possible from the supplied evidence. Before launch, compare the same account data in the current and revised row, and check row taps, long names/balances, RTL direction, large text, and constrained width. Static proposal only; visual and runtime behavior are NOT VERIFIED.