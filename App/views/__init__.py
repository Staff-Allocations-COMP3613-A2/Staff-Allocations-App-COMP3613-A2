# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin


views = [user_views, index_views, auth_views] 
# blueprints must be added to this list

from .courses_view import courses_bp
from .staff_view import staff_bp
from .staff_allocation_view import staff_allocation_bp

# Register the blueprints in the main app
def register_views(app):
    app.register_blueprint(courses_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(staff_allocation_bp)
