HW #20

Implement in the project:

at least 2 models with links (Post, Comment)

Post and Comment models must be owned by the user (FK link)

Serializers for these models

CRUD using viewset to work with these models so that:

everyone can view posts and comments/
only logged in users could add posts and comments/
only their owners could modify or delete posts or comments (when deleting a post, all comments are deleted regardless of their owners - on_delete=Cascade)
