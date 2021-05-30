from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem'))


#The directory structure for this app and the use of some resources, like Python packages and use of Jinja for front-end rendering,
#were inspired by the video tutorial “Python Website Full Tutorial - Flask, Authentication, Databases & More” (https://www.youtube.com/watch?v=dam0GPOAvVI).
