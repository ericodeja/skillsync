role_scope_map = {
    "User": [
        "read: profile",
        "write: profile",
        "search: mentors",
        "match: mentors",
        "request: match",
    ],
    "Mentor": [
        "read: profile",
        "write: profile",
        "search: mentors",
        "match: mentors",
        "request: match",
    ],
    "Admin": [
        "read: profile",
        "write: profile",
        "search: mentors",
        "search: users",
        "admin: users",
        "admin: mentors",
    ]
}

all_scopes = {
    "read:profile": "View your profile",
    "search:mentors": "Search for mentors",
    "search:users": "Search for users",
    "match:mentors": "Match your profile",
    "request:match": "Request a match",
    "admin:users": "Manage users",
    "admin:mentors": "Manage mentors",
    "write:profile": "Write your profile"
}
