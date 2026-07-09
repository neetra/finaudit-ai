class DataLayerError(Exception):
    """Base exception for data-layer failures."""


class DatabaseDependencyError(DataLayerError):
    """Raised when an optional database dependency is missing."""
