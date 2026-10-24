# Application: designing-inclusive-flutter

## User request

Give an inclusive implementation plan for this Arabic/English Flutter invoice row. Do not change the business data. Deadline is today; the designer wants exact alignment and says disabling large text and forcing LTR is fine.

## Available evidence

The supplied row uses EdgeInsets.only(left: 16), Row with fixed height 40, a 28x28 icon-only delete GestureDetector, and Text('$customerName - $invoiceId'). Arabic customer names appear next to Latin invoice IDs and amounts. Designers provided no measured contrast values. The app supports keyboard navigation on web. No screen reader, runtime or screenshot is supplied.

