# Single responsibility principle

# EXAMPLE BAD WAY - A class with too many responsibilities

class SystemMonitor:
    def load_activity(self):
        """Get the events from a source, to be processed."""

    def identify_events(self):
        """Parse the source raw data into events (domain objects)."""

    def stream_events(self):
        """Send the parsed events to an external agent."""


# BEST WAY

# Distributing responsibilities


class ActivityReader:
    def load_activity(self):
        """Get the events from a source, to be processed."""
        pass


class EventParser:
    def identify_events(self, raw_data):
        """Parse the source raw data into events (domain objects)."""
        pass


class OutputStreamer:
    def stream_events(self, events):
        """Send the parsed events to an external agent."""
        pass


class SystemMonitorBetter:
    def __init__(self, activity_reader, event_parser, output_streamer):
        self.activity_reader = activity_reader
        self.event_parser = event_parser
        self.output_streamer = output_streamer

    def monitor_system(self):
        raw_data = self.activity_reader.load_activity()
        events = self.event_parser.identify_events(raw_data)
        self.output_streamer.stream_events(events)
