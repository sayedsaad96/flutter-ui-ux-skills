# Application: crafting-flutter-motion

## User request

Refine motion for the supplied Flutter reading screen. Keep reading position and playback state intact. Marketing asks for bouncing verses and confetti after every scroll to feel premium; the release is tomorrow. Give a minimal safe motion plan and implementation choices.

## Available evidence

Current code creates AnimationController(vsync: this) inside build, calls forward on every rebuild, and never disposes it. The reader can have active audio playback. The app has a reduce-motion preference and also exposes the platform disableAnimations setting. A simple bookmark icon changes selected state. No runtime, device or frame trace is supplied.

