# Import blueprints explicitly
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .courses_view import courses_bp
from .staff_view import staff_bp
from .staff_allocation_view import staff_allocation_bp

# Add all blueprints to the views list
views = [
    user_views,
    index_views,
    auth_views,
    courses_bp,
    staff_bp,              # Include the staff blueprint
    staff_allocation_bp     # Include the staff allocation blueprint
]

# Register the blueprints in the main app
def register_views(app):
    for view in views:
        app.register_blueprint(view)  # Register each view blueprint
