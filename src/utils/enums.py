from enum import Enum, unique


@unique
class UserRole(Enum):
    ADMIN = "admin"
    DEV = "developer"
    PREMIUM = "premium"
    FREE = "free"

@unique
class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"
    SUSPENDED = "suspended"
    PENDING = "pending"
    REJECTED = "rejected"
    BLOCKED = "blocked"
    BANNED = "banned"
    ARCHIVED = "archived"
    UNKNOWN = "unknown"