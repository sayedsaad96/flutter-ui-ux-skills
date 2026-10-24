---
name: creating-flutter-ui
description: Use when creating a new Flutter screen, component family, feature flow, or application UI foundation from requirements or an established product direction.
---

# Creating Flutter UI

Translate a product task into an experience before choosing widgets. Own the
CREATE sequence; specialist skills may resolve particular decisions when
installed, but this workflow must remain usable without them.

## Establish the foundation

Identify the user, primary job, content, success condition, target platforms,
languages and constraints from the request and accessible project evidence.
Inspect existing theme, navigation and state conventions when creating a new
feature inside an app. Ask only for missing information that changes the design;
otherwise state a reasonable assumption and proceed with useful work.

Scale the process: a small component needs an intent and relevant states; a new
product needs information architecture and a visual direction first. For a major
design decision, compare genuinely different hierarchy/navigation/density options.
Do not turn every request into multiple concepts or impose a house style.

Choose a direction derived from audience, domain, brand and usage context. Define
the minimum useful tokens and patterns, then prove them on a representative
screen. A new product does not automatically need a component library, state
package or architectural rewrite.

## Structure the experience

| Decision | Concrete outcome |
|---|---|
| Primary journey | Entry, meaningful steps, back/cancel and completion |
| Information hierarchy | Content order, primary action and secondary actions |
| State behavior | Relevant initial/loading/data/empty/error/offline/partial/permission states |
| Interaction | Pending/disabled feedback, retry, validation and preservation of choices |
| Adaptation | Local constraints, navigation/input changes and content limits |
| Inclusion | Large text, RTL/LTR, localized content, semantic actions and focus |

Design failures and interruption alongside success. Preserve valid user input
through retries and conflicts. Distinguish an in-flight request, confirmed
success, confirmed failure and an unknown outcome; a timeout must not silently
become success or invite an unsafe repeated action. Respect existing domain/API
ownership of persistence, authorization and request ordering.

Example: a reservation flow should keep the chosen location and date when an
item becomes unavailable, explain the conflict, and offer alternatives. A review
step is not confirmation; only the authoritative successful result is.

## Implement incrementally

Build one useful path with its realistic failure states, using focused widgets
and the existing app boundaries. Visual systems own tokens; responsive/adaptive
work owns spatial/input adaptation; inclusion owns language/access; motion owns
transition behavior; engineering owns composition and UI performance. Apply only
the decisions needed now. Name later polish and verification work without
claiming unavailable skills ran.

## Finish with evidence

Review the implementation for clarity, state completeness and product character,
then verify with available project checks and runtime/visual evidence. Report
what was built, assumptions, chosen direction, relevant states and actual
checks. If only requirements were supplied, label the result a proposal, not an
implemented or validated UI. Explicitly mark untested devices, accessibility,
large-text/RTL behavior and runtime NOT VERIFIED. Provide the next concrete
handoff instead of inventing inspection or results.
