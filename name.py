import gpxpy
import gpxpy.gpx


def calculate_elevation_gain_and_distance(gpx_file):
    gpx = gpxpy.parse(open(gpx_file, "r"))

    elevation_gain = 0
    total_distance = 0

    for track in gpx.tracks:
        for segment in track.segments:
            previous_point = None
            for point in segment.points:
                if previous_point is not None:
                    total_distance += point.distance_2d(previous_point)
                    if point.elevation > previous_point.elevation:
                        elevation_gain += point.elevation - previous_point.elevation
                previous_point = point

    return elevation_gain, total_distance


# Example usage:
gpx_file = "Pidherny_Loop_01.gpx"
elevation_gain, total_distance = calculate_elevation_gain_and_distance(gpx_file)
print("Elevation Gain:", elevation_gain)
print("Total Distance:", total_distance)
