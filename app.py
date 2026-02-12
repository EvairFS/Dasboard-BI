from app_instance import app
from layouts.layout import layout

import callbacks.dashboard_callbacks

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
