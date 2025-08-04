role_scope_map = {
    "User": [
        "read: profile",
        "search: mentors",
        "match: mentors",
        "request: match",
        "edit: profile"
    ],
    "Mentor": [
        "read: profile",
        "search: mentors",
        "match: mentors",
        "request: match",
        "edit: profile"
    ],
    "Admin": [
        "read: profile",
        "search: mentors",
        "search: users",
        "admin: users",
        "admin: mentors",
        "edit: profile"
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
    "edit:profile": "Edit your profile"
}
