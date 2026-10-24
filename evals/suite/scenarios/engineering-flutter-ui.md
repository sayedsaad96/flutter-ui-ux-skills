# Application: engineering-flutter-ui

## User request

Propose a focused fix for this Flutter results screen. Preserve existing Cubit ownership and repository APIs. We need it today; adding a new state-management package is acceptable if faster.

## Available evidence

Accessible excerpt:
```dart
Widget build(BuildContext context) {
  final future = repository.search(query);
  return FutureBuilder<List<Result>>(
    future: future,
    builder: (context, snap) => SingleChildScrollView(
      child: Column(children: [
        for (final item in snap.data ?? []) ResultTile(item: item),
      ]),
    ),
  );
}
```
Existing SearchCubit already emits initial/loading/data/empty/error states and owns cancellation/request ordering. repository.search performs a network request. Up to 10,000 results occur. No runtime/profiler is supplied.

