from flask import request, render_template
from app.managers.user_manager import UserManager

def register_user_routes(app, cursor, conn, bcrypt):
    user_manager = UserManager(cursor, conn, bcrypt)

    @app.route("/auth")
    def auth_page():
        return render_template("auth_page.html")
    
    @app.route("/api/auth/register", methods=["POST"])
    def register():
        return user_manager.register_user()

    @app.route("/api/auth/login", methods=["POST"])
    def login():
        return user_manager.login_user()
