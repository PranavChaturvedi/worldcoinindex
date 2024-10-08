# worldcoinindex/exceptions.py

class WorldCoinIndexError(Exception):
    """Base exception for WorldCoinIndex API errors."""
    pass

class InvalidAPIKeyError(WorldCoinIndexError):
    """Exception raised for invalid API keys."""
    pass

class RateLimitError(WorldCoinIndexError):
    """Exception raised when rate limits are exceeded."""
    pass

class NotFoundError(WorldCoinIndexError):
    """Exception raised when a resource is not found."""
    pass

class ServerError(WorldCoinIndexError):
    """Exception raised for server-side errors."""
    pass
