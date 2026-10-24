Remove the `FutureBuilder` and stop calling `repository.search(query)` from `build`. The screen already has an owner for search requests: `SearchCubit`. Have the existing input/event path dispatch the query to that Cubit, and let the Cubit continue to own cancellation and request ordering. This avoids starting another network request on each rebuild and keeps the repository API unchanged.

Render the Cubit's states explicitly:

- Initial: show the existing search prompt or initial screen.
- Loading: show a progress indicator while keeping the query/input intact.
- Data: show results in a lazy, bounded scrollable, such as `ListView.builder` or `CustomScrollView` with `SliverList`. Do not put 10,000 eagerly created tiles inside `SingleChildScrollView` and `Column`.
- Empty: show a deliberate no-results message.
- Error: show the error state and a retry action that dispatches the current query through the existing Cubit path; do not render the error as an empty list.

Keep the scrollable within the screen's available constraints (for example, as the body of a `Scaffold` or inside an `Expanded` region beside the search controls). If result order or selection can change, give tiles stable keys based on result identity rather than their list index. Preserve the existing state owner and callbacks; no additional state-management package is needed.

This is a focused rendering and request-ownership fix. The evidence supports the rebuild-triggered request issue and eager construction risk, but there is no runtime or profiler evidence to claim a measured performance improvement.