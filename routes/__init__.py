from routes.front.home import *      # noqa: F401,F403
from routes.front.about import *     # noqa: F401,F403
from routes.front.contact import *   # noqa: F401,F403
from routes.front.login import *     # noqa: F401,F403
from routes.front.register import *  # noqa: F401,F403
from routes.front.dashboard import * # noqa: F401,F403
from routes.front.cart import *      # noqa: F401,F403
from routes.front.checkout import *  # noqa: F401,F403

# Admin and user management routes have been disabled to make the app static-only.
# from routes.admin.users import *
# from routes.admin.auth import *

from routes.error import *           # noqa: F401,F403