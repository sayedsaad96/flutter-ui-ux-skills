Mode: REDESIGN
Complexity: MICRO
Evidence: User description available (E0); Flutter source and runtime are not provided, so the current implementation cannot be inspected.
Capabilities: Flutter widget composition; touch-target sizing.
Verification: NOT VERIFIED — no project or runtime is available.

Set the `IconButton` constraints to at least 48×48 while keeping its existing `iconSize` unchanged. For example:

```dart
IconButton(
  icon: const Icon(Icons.arrow_back),
  iconSize: existingIconSize,
  constraints: const BoxConstraints(
    minWidth: 48,
    minHeight: 48,
  ),
  onPressed: onBack,
)
```

This is the targeted change; I can’t apply or verify it against the AppBar without the Flutter source.