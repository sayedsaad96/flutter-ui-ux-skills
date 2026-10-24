Here’s a pure Dart implementation and boundary-focused tests. It accepts latitude and longitude in decimal degrees and returns kilometers.

`haversine.dart`:

```dart
import 'dart:math' as math;

/// Calculates the great-circle distance between two coordinates in kilometers.
///
/// Coordinates are decimal degrees. Latitudes must be in [-90, 90] and
/// longitudes in [-180, 180].
double haversineDistanceKm({
  required double latitude1,
  required double longitude1,
  required double latitude2,
  required double longitude2,
}) {
  _validateCoordinate(latitude1, longitude1, 'first');
  _validateCoordinate(latitude2, longitude2, 'second');

  const earthRadiusKm = 6371.0088;
  final lat1 = _degreesToRadians(latitude1);
  final lat2 = _degreesToRadians(latitude2);
  final deltaLat = _degreesToRadians(latitude2 - latitude1);
  final deltaLon = _degreesToRadians(longitude2 - longitude1);

  final sinHalfLat = math.sin(deltaLat / 2);
  final sinHalfLon = math.sin(deltaLon / 2);
  final a = sinHalfLat * sinHalfLat +
      math.cos(lat1) * math.cos(lat2) * sinHalfLon * sinHalfLon;

  // Clamp against floating-point drift outside [0, 1].
  final boundedA = a.clamp(0.0, 1.0);
  final centralAngle =
      2 * math.atan2(math.sqrt(boundedA), math.sqrt(1 - boundedA));

  return earthRadiusKm * centralAngle;
}

double _degreesToRadians(double degrees) => degrees * math.pi / 180;

void _validateCoordinate(double latitude, double longitude, String label) {
  if (!latitude.isFinite ||
      !longitude.isFinite ||
      latitude < -90 ||
      latitude > 90 ||
      longitude < -180 ||
      longitude > 180) {
    throw ArgumentError.value(
      (latitude, longitude),
      label,
      'must contain finite latitude [-90, 90] and longitude [-180, 180]',
    );
  }
}
```

`haversine_test.dart` (using `package:test`):

```dart
import 'dart:math' as math;

import 'package:test/test.dart';
import 'package:your_package/haversine.dart';

void main() {
  group('haversineDistanceKm', () {
    test('returns zero for identical coordinates', () {
      expect(
        haversineDistanceKm(
          latitude1: 0,
          longitude1: 0,
          latitude2: 0,
          longitude2: 0,
        ),
        0,
      );
    });

    test('handles a one-degree equatorial arc', () {
      expect(
        haversineDistanceKm(
          latitude1: 0,
          longitude1: 0,
          latitude2: 0,
          longitude2: 1,
        ),
        closeTo(111.195, 0.01),
      );
    });

    test('takes the short path across the antimeridian', () {
      expect(
        haversineDistanceKm(
          latitude1: 0,
          longitude1: 179.5,
          latitude2: 0,
          longitude2: -179.5,
        ),
        closeTo(111.195, 0.01),
      );
    });

    test('handles opposite poles', () {
      expect(
        haversineDistanceKm(
          latitude1: 90,
          longitude1: 0,
          latitude2: -90,
          longitude2: 0,
        ),
        closeTo(math.pi * 6371.0088, 0.001),
      );
    });

    test('handles antipodal points without floating-point overflow', () {
      expect(
        haversineDistanceKm(
          latitude1: 0,
          longitude1: 0,
          latitude2: 0,
          longitude2: 180,
        ),
        closeTo(math.pi * 6371.0088, 0.001),
      );
    });

    test('accepts coordinate boundary values', () {
      expect(
        haversineDistanceKm(
          latitude1: -90,
          longitude1: -180,
          latitude2: 90,
          longitude2: 180,
        ),
        closeTo(math.pi * 6371.0088, 0.001),
      );
    });

    test('rejects coordinates outside the allowed ranges', () {
      expect(
        () => haversineDistanceKm(
          latitude1: 90.001,
          longitude1: 0,
          latitude2: 0,
          longitude2: 0,
        ),
        throwsArgumentError,
      );
      expect(
        () => haversineDistanceKm(
          latitude1: 0,
          longitude1: 0,
          latitude2: 0,
          longitude2: -180.001,
        ),
        throwsArgumentError,
      );
    });

    test('rejects non-finite coordinates', () {
      expect(
        () => haversineDistanceKm(
          latitude1: double.nan,
          longitude1: 0,
          latitude2: 0,
          longitude2: 0,
        ),
        throwsArgumentError,
      );
    });
  });
}
```

Replace `your_package` with the package name from your `pubspec.yaml`.