## Flask Application Design

### HTML Files

- **index.html**: This will be the main page of the application. It will contain the links to the different categories of resources and a section to track the progress and completion of the courses.

- **courses.html**: This page will list all the courses available on Coursera and Grow.

- **progress.html**: This page will display the progress and completion of the courses that the user has enrolled in.

### Routes

- **@app.route('/')**: This route will render the **index.html** page.

- **@app.route('/courses')**: This route will render the **courses.html** page.

- **@app.route('/progress')**: This route will render the **progress.html** page.

- **@app.route('/add_course', methods=['POST'])**: This route will add a new course to the database.

- **@app.route('/update_progress', methods=['POST'])**: This route will update the progress of a course in the database.

### Supporting Files

- **database.py**: This file will contain the functions to interact with the database.

- **models.py**: This file will contain the models for the database tables.

- **app.py**: This file will contain the Flask application object and the main function to run the application.

### Bootstrap Integration

- Bootstrap will be used to style the application.
- The necessary CSS and JavaScript files will be included in the HTML files.
- The Bootstrap components will be used to create the navigation bar, buttons, and other UI elements.



### Additional Notes

- The database will store the information about the courses, the user's progress, and completion status.

- The application will use a templating engine to render the HTML pages.

- The routes will handle the user's requests and interact with the database.

- The supporting files will provide the necessary functionality for the application.

- Bootstrap integration will enhance the user interface of the application.