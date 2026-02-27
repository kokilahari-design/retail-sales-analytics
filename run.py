#run() method of Flask class runs the application on the local development server.

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
