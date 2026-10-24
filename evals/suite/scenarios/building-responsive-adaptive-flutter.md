# Application: building-responsive-adaptive-flutter

## User request

Fix the supplied layout strategy for a resizable Flutter web/tablet app. Keep selected account and scroll position while resizing; do not choose layouts just by OS. Give a concrete implementation approach.

## Available evidence

The host window is 1440 logical pixels wide, but this accounts panel is constrained to 420 by a split workspace. Current code uses MediaQuery.sizeOf(context).width > 900 to render a Row of account list and account detail inside the panel. Detail has width 600. A fold can occlude content. Keyboard and pointer input are used on web; phone uses touch. Navigation selection lives in the existing Cubit. No runtime or device is supplied.

